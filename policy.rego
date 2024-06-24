package authz

default allow = false

# Roles
roles = {
    "admin": {
        "permissions": ["view", "add", "delete"],
    },
    "guest": {
        "permissions": ["view"],
    },
}

# Permission check
allow {
    some role in roles
    input.subject.role == role
    role_has_permission(role, input.action, input.resource)
}

role_has_permission(role, action, resource) {
    roles[role].permissions[_] == action
}
