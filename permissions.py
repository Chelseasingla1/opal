from permit import Permit

# Initialize the Permit instance
permit = Permit(
    pdp="http://localhost:7766",
    token="permit_key_Mfhhl1IiHOVtTx4BZL4taAvOCuiQRiGzB2Wyb79HipHs1RHhl79rN7xNH7v4x2K7CHNZA5BgngEuLNcfZLXgA2",
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
