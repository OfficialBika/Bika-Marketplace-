
ADMIN_ROLES = {'admin'}


def is_admin(role: str):
    return role in ADMIN_ROLES


def can_manage_marketplace(role: str):
    return is_admin(role)
