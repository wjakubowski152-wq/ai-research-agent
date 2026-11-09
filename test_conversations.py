from conversation import trim_history


def test_trim_history_keeps_last_10_messages():
    history = list(range(14))

    result = trim_history(history)

    assert len(result) == 10
    assert result == [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def test_trim_history_keeps_even_number_of_messages():
    history = list(range(13))

    result = trim_history(history)

    assert len(result) % 2 == 0

def test_trim_history_with_empty_list():
    history = []

    result = trim_history(history)

    assert result == []


def test_trim_history_with_custom_limit():
    history = list(range(10))

    result = trim_history(history, max_messages=4)

    assert result == [6, 7, 8, 9]