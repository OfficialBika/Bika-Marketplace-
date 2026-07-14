ROLES = {
    'admin': ['manage_characters','manage_users','manage_marketplace'],
    'moderator': ['review_reports'],
    'user': ['trade','purchase','bid']
}


def has_permission(role: str, permission: str):
    return permission in ROLES.get(role, [])
