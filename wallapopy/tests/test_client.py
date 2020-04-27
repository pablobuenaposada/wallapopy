from unittest.mock import patch

from wallapopy.src.client import WallapopClient
from wallapopy.tests import fixtures


class TestClient:
    def test_instantiation(self):
        """just checking that client can be instantiated"""
        assert type(WallapopClient()) == WallapopClient

    def test_user(self):
        client = WallapopClient()
        with patch('wallapopy.src.client.requests.get') as m_get:
            m_get.return_value.json.return_value = fixtures.USER_RESPONSE
            assert client.user(40000000) == fixtures.USER_RESPONSE

    def test_user_reviews_received(self):
        client = WallapopClient()
        with patch('wallapopy.src.client.requests.get') as m_get:
            m_get.return_value.json.return_value = fixtures.USER_REVIEWS_RECEIVED
            assert client.user_reviews_received(40000000) == fixtures.USER_REVIEWS_RECEIVED
