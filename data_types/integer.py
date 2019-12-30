from config_utils import user_enter, function_maker

def build_integer_function(definition):
    """
    Builds a function that gets the the data for a integer from the user.
    Raises an error if the definition is not valid.
    str -> () -> int or error
    """
    return function_maker(user_enter_integer, 
                          definition, is_valid_integer_definition, 
                          "Not a valid integer definition: " + definition)

def is_valid_integer_definition(definition):
    """
    Returns true if the integer definition is valid.
    str -> bool
    """
    return True

def user_enter_integer(definition):
    """
    Get a integer from the user.
    Returns it along with label for the integer.
    A integer is a int.
    Signature in config: integer label
    str -> (label: str, integer: int)
    """
    
    question = 'What is the value for {}?'
    valid = 'A valid response is any integer'

    return user_enter(get_integer_label, 
                      user_enter_integer_response,
                      get_integer_from_response,
                      is_valid_integer_response,
                      question,
                      valid,
                      definition)


def get_integer_from_response(response):
    """
    Gets the value from a valid integer response.
    str -> int
    """
    return int(response)
    
def is_valid_integer_response(response):
    """
    Returns true if a integer response is valid.
    str -> bool
    """
    try:
        return int(response)
    except ValueError:
        return False

def user_enter_integer_response():
    """
    Prompts the user to enter a integer response.
    nothing -> str
    """
    return input('int: ')
    
def get_integer_label(definition):
    """
    Given a valid integer definition, returns its label.
    str -> str
    """
    return definition