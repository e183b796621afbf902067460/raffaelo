def string_to_bytes32(string: str) -> bytes:
    """Converts a string to a fixed-length bytes32 representation.

    Truncates the string to 32 characters if it exceeds the length,
    or pads the string with zeros to reach a length of 32 if it is shorter.

    Args:
    ----
        string (str): The input string to be converted.

    Returns:
    -------
        bytes: The bytes32 representation of the input string.
    """
    return bytes(string[:32] if len(string) > 32 else string.ljust(32, "0"), "utf-8")
