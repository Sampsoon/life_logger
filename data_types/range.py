from functools import reduce
from config_utils import user_enter, function_maker

def build_range_function(definition):
    """
    Builds a function that gets the the data for a range from the user.
    Raises an error if the definition is not valid.
    str -> () -> int or error
    """
    return function_maker(user_enter_range, 
                          definition, is_valid_range_definition, 
                          "Not a valid range definition: " + definition)
    
def user_enter_range(definition):
    """
    Get a range from the user.
    Returns it along with label for the range.
    A range is a int from a to b inclusive.
    Signature in config: range (a,b) label
    str -> (label: str, range: int)
    """

    number_range = get_bounds(definition)
    a = number_range[0]
    b = number_range[1]

    inclusive_exclusive = 'From a scale from {} inclusive to {} exclusive, '.format(a,b)
    question = inclusive_exclusive + 'how would you rate your {}?'

    valid = 'A valid response is a integer ' + inclusive_exclusive.lower()
    
    is_valid = lambda response: is_valid_range(response, a, b)
    
    return user_enter(get_range_label, 
                      user_enter_range_response,
                      get_range_from_response,
                      is_valid,
                      question,
                      valid,
                      definition)

def is_valid_range_definition(definition):
    """
    Returns true if the range definition is valid.
    str -> bool
    """
    split = definition.split(" ")
    try:
        range_definition = split[0]
        
        if not len(split) == 2:
            return False
        
        if not string_has_parentheses_around_it(range_definition):
            return False
            
        range_definition = remove_first_range(range_definition)
        range_definition = remove_last_range(range_definition)
       
        if not string_has_one_comma_inside_it(range_definition):
            return False
        
        range_definition = range_definition.replace(',', '')
        
        if not range_definition.isdigit():
            return False
        
        bounds = get_bounds(definition)
        
        return bounds[0] < bounds[1]
    
    except:
        return False

def string_has_parentheses_around_it(string):
    """
    Returns true if a given string has parentheses around it.
    str -> bool
    """
    try:
        return get_front_range(string) == '(' and get_last_range(string) == ')'
    except:
        return False

def string_has_one_comma_inside_it(string):
    """
    Returns true if a string has one common side it (not on eather end of it.)
    str -> bool
    """
    try:
        if get_front_range(string) == ',' or get_last_range(string) == ',':
            return False
        return string.count(',') == 1
    except:
        return False

def get_front_range(some_list):
    """
    Returns the front range of a list.
    list -> any
    """
    return some_list[0]

def get_last_range(some_list):
    """
    Returns the last range of a list.
    list -> any
    """
    return some_list[-1]

def remove_first_range(some_list):
    """
    Returns a given list with its first range removed.
    list -> list
    """
    return some_list[1:]

def remove_last_range(some_list):
    """
    Returns a given list with its last range removed.
    list -> list
    """
    return some_list[:-1]

def user_enter_range_response():
    """
    Prompts the user to enter a range response.
    nothing -> str
    """
    return input('range: ')

def get_range_label(definition):
    """
    Given a range definition, returns its label.
    str -> str
    """
    return definition.split(' ')[1]

def get_bounds(definition):
    """
    Given a range definition, returns its bounds.
    str -> (int, int)
    """
    bounds = definition.split(' ')[0]
    values = bounds.split(',')
    a = values[0][1:]
    b = values[1][:-1]
    return (int(a), int(b))

def is_valid_range(response, a, b):
    """
    Given a user response and a range of numbers,
    Returns if the response in a int and that in falls in range of [a, b).
    str, number, number -> bool
    """
    if response.isdigit():
        range = get_range_from_response(response)
        return range >= a and range < b
    return False

def get_range_from_response(response):
    """
    Returns true if a boolean response is valid.
    str -> int
    """
    return int(response)