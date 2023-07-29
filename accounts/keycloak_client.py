from keycloak_auth import settings
from keycloak import KeycloakOpenID


class KeycloakClient:
    def __init__(self, redirect_uri):
        self.keycloak_openid = KeycloakOpenID(
            server_url=settings.KEYCLOAK_SERVER_URL,
            client_id=settings.KEYCLOAK_CLIENT_ID,
            realm_name=settings.KEYCLOAK_REALM,
            client_secret_key=settings.KEYCLOAK_CLIENT_SECRET,
        )

    def get_login_url(self, redirect_uri):
        return self.keycloak_openid.auth_url(redirect_uri=redirect_uri)

    def get_token(self, code, redirect_uri):
        token = self.keycloak_openid.token(
            code=code, redirect_uri=redirect_uri
        )
        return token

    def get_user_info(self, token):
        user_info = self.keycloak_openid.userinfo(token=token)
        return user_info
