import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import ClientError, ServerError

from config import MODEL_NAME
from prompts import SYSTEM_PROMPT, build_prompt
from context_builder import build_context
from memory import add_user_message, add_assistant_message
import traceback
import time

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def stream_llm(message: str):
    """
    Stream a response from Gemini while persisting the conversation.
    """

    # Save the user's message
    add_user_message(message)

    # Build the knowledge context
    context = build_context(message)
    print("=" * 80)
    print("CONTEXT LENGTH:", len(context))
    print("=" * 80)
    print(context[:3000])   # Print the first 3000 characters
    print("=" * 80)

    prompt = build_prompt(
    user_message=message,
    knowledge=context
    )

    full_response = ""

    try:
        stream = client.models.generate_content_stream(
            model=MODEL_NAME,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=0.3,
            ),
        )

        for chunk in stream:
            if chunk.text:
                print(repr(chunk.text))
                full_response += chunk.text
                yield chunk.text
                time.sleep(0.2)   # Temporary test only

        # Save the assistant's complete response
        if full_response:
            add_assistant_message(full_response)


    except ClientError as e:
        print(e)

        message = str(e)

        if "RESOURCE_EXHAUSTED" in message:
            yield (
                yield """⚠️ Gemini is temporarily unavailable due to API usage limits.

                  In the meantime, you can continue exploring my interactive machine learning portfolio.

                [[ACTION:portfolio]]
                """
            )
        else:
            yield f"Gemini returned an error: {message}"

    except ServerError as e:
        print(e)
        yield f"Gemini server error: {e}"
    except Exception as e:
        traceback.print_exc()
        raise
        