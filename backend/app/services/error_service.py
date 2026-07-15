def api_error(message: str):
    return {
        "success": False,
        "error": message
    }
