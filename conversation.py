def trim_history(history, max_messages=10):
    max_messages = max_messages - (max_messages % 2)

    return history[-max_messages:]