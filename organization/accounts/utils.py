

def jwt_response_payload_handler(token, user=None, request=None, issued_at=None):
    response = {
        'token': token,
        'user': user.id,
        'user_name': user.name,
        'permissions': user.permissions.keys(),
        'role': user.roles.first().role.name
    }
    return response


def get_jwt_secret_key(user):
    return user.jwt_secret
