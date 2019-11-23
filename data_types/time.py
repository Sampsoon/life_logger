from life_logger_utils import user_enter, function_maker

def build_time_function(definition):
    """
    Builds a function that gets the the data for a time from the user.
    Raises an error if the definition is not valid.
    str -> () -> int or error
    """
    return function_maker(user_enter_time, 
                          definition, is_valid_time_definition, 
                          "Not a time value definition: " + definition)

def is_valid_time_definition(definition):
    """
    Returns true if the time definition is valid.
    str -> bool
    """
    return True

def user_enter_time(definition):
    """
    Get a time from the user.
    Returns it along with label for the value.
    A time is a float.
    Signature in config: time label
    str -> (label: str, value: float)
    """
    
    question = 'How long did you {}?'
    valid = 'A valid response is a number >= 0'

    return user_enter(get_time_label, 
                      user_enter_time_response,
                      get_time_from_response,
                      is_valid_time_response,
                      question,
                      valid,
                      definition)


def get_time_from_response(response):
    """
    Gets the time from a valid time response.
    str -> float
    """
    return float(response)
    
def is_valid_time_response(response):
    """
    Returns true if a time response is valid.
    str -> bool
    """
    try:
        return float(response) >= 0
    except ValueError:
        return False

def user_enter_time_response():
    """
    Prompts the user to enter a time response.
    nothing -> str
    """
    return input('hours: ')
    
def get_time_label(definition):
    """
    Given a valid time definition, returns its label.
    str -> str
    """
    return definition