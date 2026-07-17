# Copyright (c) 2026 Splunk Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from pathlib import Path


ROOT = Path(__file__).parent


def test_api_key_is_sent_in_a_header_and_not_persisted_in_transport_errors():
    source = (ROOT / "canary_connector.py").read_text()

    assert 'headers["X-Canary-Auth-Token"] = self._api_key' in source
    assert '{"auth_token": self._api_key}' not in source
    assert "except requests.exceptions.RequestException:" in source
    assert "Details: {e!s}" not in source
