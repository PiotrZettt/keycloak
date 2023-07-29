from keycloak_auth import settings
from keycloak import KeycloakOpenID, KeycloakAdmin, KeycloakOpenIDConnection

keycloak_openid = KeycloakOpenID(
    server_url=settings.KEYCLOAK_BASE_URL,
    realm_name=settings.KEYCLOAK_USER_REALM,
    client_id=settings.KEYCLOAK_CLIENT_ID,
    client_secret_key=settings.KEYCLOAK_CLIENT_SECRET)

keycloak_connection = KeycloakOpenIDConnection(
                        server_url=settings.KEYCLOAK_BASE_URL,
                        realm_name=settings.KEYCLOAK_REALM,
                        username=settings.KEYCLOAK_ADMIN_USERNAME,
                        password=settings.KEYCLOAK_ADMIN_PASSWORD,
                        client_id=settings.KEYCLOAK_CLIENT_ID,
                        client_secret_key=settings.KEYCLOAK_CLIENT_SECRET,
                        verify=True)
keycloak_admin = KeycloakAdmin(connection=keycloak_connection)
