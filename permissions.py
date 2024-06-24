from permit import Permit

# Initialize the Permit instance
permit = Permit(
    pdp="http://localhost:7766",
    token="",
)

def check_permission(subject, action, resource):
    try:
        result = permit.check(action=action, resource=resource, subject=subject)
        print(f"Permission check for subject='{subject}', action='{action}', resource='{resource}': {result}")
        return result
    except TypeError as e:
        print(f"TypeError: {e}")
        return False

def is_admin(subject):
    return check_permission(subject, "add", "weather") and check_permission(subject, "delete", "weather")

def is_user(subject):
    return check_permission(subject, "view", "weather")
