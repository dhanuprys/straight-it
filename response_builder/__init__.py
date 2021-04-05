def success(request_type, properties={}):
    return {
        "success": True,
        "type": request_type,
        **properties
    }

def fail(request_type, reason, properties={}):
    return {
        "success": False,
        "reason": reason,
        "type": request_type,
        **properties
    }