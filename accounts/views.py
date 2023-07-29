from django.shortcuts import render
from .keycloak_admin import KeycloakOpenID, keycloak_admin
from keycloak_auth import settings

# Create your views here.


def connect(request):
    keycloak_openid = KeycloakOpenID(server_url=settings.KEYCLOAK_SERVER_URL,
                                     client_id=settings.KEYCLOAK_CLIENT_ID,
                                     realm_name=settings.KEYCLOAK_REALM,
                                     client_secret_key=settings.KEYCLOAK_CLIENT_SECRET)

    data = {"email": "piotrzet@me.com",
            "username": "piotrzet@me.com",
            "enabled": True,
            "firstName": "Piotr",
            "lastName": "Zet",
            "credentials": [{"value": "4r5t5tr45rr", "type": "password"}]}

    new_user = keycloak_admin.get_users()

    config_well_known = keycloak_openid.well_known()
    realm_name = keycloak_admin.realm_name
    print(new_user)
    return render(request, 'connect.html')
