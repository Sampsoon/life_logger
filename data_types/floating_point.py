from config_utils import user_enter, function_maker

def build_floating_point_function(definition):
    """
    Builds a function that gets the the data for a floating_point from the user.
    Raises an error if the definition is not valid.
    str -> () -> int or error
    """
    return function_maker(user_enter_floating_point, 
                          definition, is_valid_floating_point_definition, 
                          "Not a valid floating_point definition: " + definition)

def is_valid_floating_point_definition(definition):
    """
    Returns true if the floating_point definition is valid.
    str -> bool
    """
    return True

def user_enter_floating_point(definition):
    """
    Get a floating_point from the user.
    Returns it along with label for the floating_point.
    A floating_point is a float.
    Signature in config: floating_point label
    str -> (label: str, floating_point: float)
    """
    
    question = 'What is the value for {}?'
    valid = 'A valid response is any floating point number'

    return user_enter(get_floating_point_label, 
                      user_enter_floating_point_response,
                      get_floating_point_from_response,
                      is_valid_floating_point_response,
                      question,
                      valid,
                      definition)


def get_floating_point_from_response(response):
    """
    Gets the floating_point from a valid floating_point response.
    str -> float
    """
    return float(response)
    
def is_valid_floating_point_response(response):
    """
    Returns true if a floating_point response is valid.
    str -> bool
    """
    try:
        return float(response)
    except ValueError:
        return False

def user_enter_floating_point_response():
    """
    Prompts the user to enter a floating_point response.
    nothing -> str
    """
    return input('float: ')
    
def get_floating_point_label(definition):
    """
    Given a valid floating_point definition, returns its label.
    str -> str
    """
    return definition