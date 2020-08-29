import uuid


def generate_uuid_token():
    token = uuid.uuid1()
    return token
    