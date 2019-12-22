def new_line_pad(string):
    """
    Returns a string padded with newlines.
    str -> str
    """
    new_line = '\n'
    return new_line + string + new_line

def quote_pad(string):
    """
    Returns a string padded with quotes.
    str -> str
    """
    quote = "'"
    return quote + string + quote