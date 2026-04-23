def greeter(argument: str) -> str:
    """Return a greeting for a single alphanumeric name.

    Returns "Hi <argument>" when the provided argument is alphanumeric.
    Otherwise returns "Not sure who you are.".
    """
    if not argument.isalnum():
        return "Not sure who you are."

    return f"Hi {argument}"
