from pathlib import Path


ROOT = Path(__file__).parent


def test_api_key_is_sent_in_a_header_and_not_persisted_in_transport_errors():
    source = (ROOT / "canary_connector.py").read_text()

    assert 'headers["X-Canary-Auth-Token"] = self._api_key' in source
    assert '{"auth_token": self._api_key}' not in source
    assert 'except requests.exceptions.RequestException:' in source
    assert "Details: {e!s}" not in source
