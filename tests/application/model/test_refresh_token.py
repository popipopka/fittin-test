from datetime import datetime
from unittest import TestCase

from src.application.model import RefreshToken


class TestRefreshToken(TestCase):
    def test_equality(self):
        # Given
        first = RefreshToken(id=1, user_id=1, value='{value}', expires_at=datetime.now())
        second = RefreshToken(id=1, user_id=1, value='{value}', expires_at=datetime.now())

        # When, Then
        self.assertEqual(first, second)

    def test_inequality(self):
        # Given
        first = RefreshToken(id=1, user_id=1, value='{value}', expires_at=datetime.now())
        second = RefreshToken(id=2, user_id=2, value='{2}', expires_at=datetime.now())

        # When, Then
        self.assertNotEqual(first, second)

    def test_hash_password_not_in_repr(self):
        # Given
        refresh_token = RefreshToken(id=1, user_id=1, value='{value}', expires_at=datetime.now())

        # When
        repr_str = repr(refresh_token)

        # Then
        self.assertNotIn(f"value='{refresh_token.value}'", repr_str)