
import pytest
import config

def test_config_raises_error_when_api_key_is_missing(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.setattr(config, "load_dotenv", lambda: None)

    with pytest.raises(ValueError, match="OPENAI_API_KEY is not configured"):
        config.load_config()

def test_config_raises_error_when_model_is_missing(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.delenv("OPENAI_MODEL", raising=False)
    monkeypatch.setattr(config, "load_dotenv", lambda: None)

    with pytest.raises(ValueError, match="OPENAI_MODEL is not configured"):
        config.load_config()

def test_load_config_returns_values(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setenv("OPENAI_MODEL", "test-model")
    monkeypatch.setattr(config, "load_dotenv", lambda: None)

    api_key, model = config.load_config()

    assert api_key == "test-key"
    assert model == "test-model"