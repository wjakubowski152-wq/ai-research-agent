def trim_history(history, max_messages=10):
    if max_messages < 0:
        raise ValueError("max_messages cannot be negative")

    if max_messages == 0:
        return []

    max_messages = max_messages - (max_messages % 2)
    return history[-max_messages:]