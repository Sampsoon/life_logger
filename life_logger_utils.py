import constants

# TODO: CHECK VALIDITY OF DEFINITIONS... probs put in a function call that returns user_enter***

# A definition is the text following space after the type name.

def user_enter(get_label,
                user_enter_response, 
                get_data_from_response,
                is_valid_data,
                opening_question_text, 
                valid_respones_text,
                definition):
    """
    Asks the user to enter data to be logged.
    Returns the data along with label for the data.
    Parameters
    ----------
    get_label : str -> str
        gets the data's label from the definition.
    user_enter_response : nothing -> str
        Prompts the user to enter a data response.
    is_valid_data : str -> bool
        Returns true if the data is valid.
    opening_question_text : str
        The text for the question prompted the user the user somthing.
        This would come with a spot: {} for the data label.
    valid_respones_text : str
        The text that define a valid response.
    definition : str
        The definition for the data.
    ----------
    str -> (label: str, value: int)
    """

    label = get_label(definition)
    
    print(opening_question_text.format(label))
    response = user_enter_response()

    while not is_valid_data(response):
        print()
        print('Please enter a valid response.')
        print(valid_respones_text)
        response = user_enter_response()

    value = get_data_from_response(response)

    return (label, value)

def config_to_functions(config):
    """
    Takes in the data for a config and returns a list of functions to call the meet it's criteria.
    list of str -> list of (none -> str)
    """
    type_to_input_functions = constants.TYPE_MAP

    functions = []

    for line in config:

        # Skip the lines that are commented out.
        if is_line_commented(line):
            continue

        check_config_line(line)

        type = get_command_type(line)
        check_type(type)

        definition = get_command_definition(line)

        # Have to do binding because Python is retarded: https://stackoverflow.com/questions/58667027/string-values-are-passed-in-as-reference-to-a-python-lambda-for-some-reason?noredirect=1#comment103636999_58667027
        functions.append(function_maker(type_to_input_functions[type], definition))

    return functions


def get_command_type(line):
    """
    Returns the command type.
    str -> str
    """
    line = line.split(' ', 1)
    return line[0]


def get_command_definition(line):
    """
    Returns the command definition.
    str -> str
    """
    line = line.split(' ', 1)
    return line[1]


def is_line_commented(line):
    """
    Returns true if the given line was commented out.
    str -> bool
    """
    return len(line) >= 2 and line[0:2] == constants.COMMENT_OUT_STRING


def function_maker(input_func, perameter):
    """
    Given a function and it's perameter returns a function object.
    (str -> anything), str -> (none -> anything)
    """
    return lambda: input_func(perameter)


def check_type(type):
    """
    Checks that a given type is valid.
    If not, throw an exception.
    str -> none or error
    """
    if type not in constants.TYPE_MAP:
        raise ValueError(type + ' is not a valid type')


def check_config_line(line):
    """
    Checks that a given line in the config is valid.
    If not, throw an exception.
    str -> none or error
    """
    if len(line.split(' ', 1)) == 1:
        raise ValueError('Invalid config line: ' + line)