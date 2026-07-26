conversation_history = []

def add_user_message(message):
    conversation_history.append({
        "role": "user",
        "text": message
    })
    
def add_assistant_message(message):
    conversation_history.append({
        "role": "assistant",
        "text": message
    })
def get_history():
    return conversation_history


def clear_history():
    conversation_history.clear()