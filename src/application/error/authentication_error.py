class AuthenticationError(Exception):
    @staticmethod
    def wrong_password() -> 'AuthenticationError':
        raise AuthenticationError('Wrong password')

    @staticmethod
    def invalid_refresh_token() -> 'AuthenticationError':
        raise AuthenticationError('Invalid refresh token')

    @staticmethod
    def revoked_refresh_token() -> 'AuthenticationError':
        raise AuthenticationError('Revoked refresh token')

    @staticmethod
    def invalid_access_token() -> 'AuthenticationError':
        raise AuthenticationError('Invalid access token')