from google.cloud.firestore_v1.client import Client


def authorize(user: str, account: str, entity: str, permission: str, db_connection: Client) -> bool:
    permissions = db_connection.collection("Permissions").where("user", "==", user).where("entity", "==", entity).where("account", "==", account).get()

    if len(permissions) > 1:
        raise ValueError(f"Could not identify one set of permissions for the request, found {len(permissions)}")
    if len(permissions) == 0:
        return False

    permissions = permissions[0].to_dict()
    return permissions[permission]

