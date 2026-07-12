def validate_message(message):

    if message is None:
        return False

    if not isinstance(message, str):
        return False

    if len(message.strip()) == 0:
        return False

    return True