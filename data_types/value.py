from life_logger_utils import user_enter

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