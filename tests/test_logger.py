from logger_config import logger


def test_logger_exception(caplog):
    with caplog.at_level("ERROR"):
        try:
            raise ValueError("Test error")
        except ValueError:
            logger.exception("Unexpected error during research")

    assert "Unexpected error during research" in caplog.text
    assert "ValueError: Test error" in caplog.text