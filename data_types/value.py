from functools import reduce
from life_logger_utils import user_enter, function_maker

def build_value_function(definition):
    """
    Builds a function that gets the the data for a value from the user.
    Raises an error if the definition is not valid.
    str -> () -> int or error
    """
    return function_maker(user_enter_value, 
                          definition, is_valid_value_definition, 
                          "Not a valid value definition: " + definition)

def is_valid_value_definition(definition):
    """
    Returns true if the value definition is valid.
    str -> bool
    """
    split = definition.split(" ")
    try:
        first_value = split[0]
        
        return (len(split) == 2 and 
                string_has_parentheses_around_it(first_value) and 
                string_has_one_comma_inside_it(first_value) and
                range_has_only_int_values(first_value))
    except:
        return False

def range_has_only_int_values(range_string):
    """
    Returns true if a given range only has int in its definition: (int,int)
    str -> bool
    """
    
    # Removes the items in a range that are not numbers.
    range_string = remove_first_value(range_string)
    range_string = remove_last_value(range_string)
    range_string = remove_element(range_string, ',')

    return all_values_in_string_int(range_string)
    
def all_values_in_string_int(string):
    """
    Returns true if all the values in a string are integers.
    str -> bool
    """
    is_digit_accumulator = lambda current, char: char.isdigit and current
    return reduce(is_digit_accumulator, string, True)

def remove_element(some_list, value):
    """
    Returns a new list with an element removed from it.
    list -> list
    """
    return [item for item in some_list if item != value]

def string_has_parentheses_around_it(string):
    """
    Returns true if a given string has parentheses around it.
    str -> bool
    """
    try:
        return get_front_value(string) == '(' and get_last_value(string) == ')'
    except:
        return False

def string_has_one_comma_inside_it(string):
    """
    Returns true if a string has one common side it (not on eather end of it.)
    str -> bool
    """
    try:
        if get_front_value(string) == ',' or get_last_value(string) == ',':
            return False
        return string.count(',') == 1
    except:
        return False

def get_front_value(some_list):
    """
    Returns the front value of a list.
    list -> any
    """
    return some_list[0]

def get_last_value(some_list):
    """
    Returns the last value of a list.
    list -> any
    """
    return some_list[-1]

def remove_first_value(some_list):
    """
    Returns a given list with its first value removed.
    list -> list
    """
    return some_list[1:]

def remove_last_value(some_list):
    """
    Returns a given list with its last value removed.
    list -> list
    """
    return some_list[:-1]

def user_enter_value(definition):
    """
    Get a value from the user.
    Returns it along with label for the value.
    A value is a int from a to b inclusive.
    Signature in config: value (a,b) label
    str -> (label: str, value: int)
    """

    number_range = get_value_range(definition)
    a = number_range[0]
    b = number_range[1]

    inclusive_exclusive = 'From a scale from {} inclusive to {} exclusive, '.format(a,b)
    question = inclusive_exclusive + 'how would you rate your {}?'

    valid = 'A valid response is a integer ' + inclusive_exclusive.lower()
    
    is_valid = lambda response: is_valid_value(response, a, b)
    
    return user_enter(get_value_label, 
                      user_enter_value_response,
                      get_value_from_response,
                      is_valid,
                      question,
                      valid,
                      definition)

def user_enter_value_response():
    """
    Prompts the user to enter a value response.
    nothing -> str
    """
    return input('Value: ')

def get_value_label(definition):
    """
    Given a value definition, returns its label.
    str -> str
    """
    return definition.split(' ')[1]

def get_value_range(definition):
    """
    Given a value definition, returns its range.
    str -> (int, int)
    """
    range = definition.split(' ')[0]
    values = range.split(',')
    a = values[0][1:]
    b = values[1][:-1]
    return (int(a), int(b))

def is_valid_value(response, a, b):
    """
    Given a user response and a range of numbers,
    Returns if the response in a int and that in falls in range of [a, b).
    str, number, number -> bool
    """
    if response.isdigit():
        value = get_value_from_response(response)
        return value >= a and value < b
    return False

def get_value_from_response(response):
    """
    Returns true if a boolean response is valid.
    str -> int
    """
    return int(response)