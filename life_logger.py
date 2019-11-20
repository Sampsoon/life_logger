import sys
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
        print('Please enter a valid response')
        print(valid_respones_text)
        response = user_enter_response()

    value = get_data_from_response(response)

    return (label, value)

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
    question = inclusive_exclusive + 'how would you rate your {}'

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

def user_enter_time(definition):
    """
    Get a time from the user.
    Returns it along with label for the value.
    A time is a float.
    Signature in config: time label
    str -> (label: str, value: float)
    """
    
    question = 'How long did you {}?'
    valid = 'A valid response is a number'

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
        float(response)
        return True
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

def user_enter_did_do(definition):
    """
    Gets a did_do from the user.
    Returns it along with label for the value.
    A did_do is a bool.
    Signature in config: did_do label
    str -> (label: str, value: bool)
    """
    
    question = 'Did you {}?'
    valid = 'A valid response is eather "y" for True or "n" for False.'

    return user_enter(get_did_do_label, 
                      user_enter_boolean_response, 
                      get_bool_from_response,
                      is_valid_boolean_response,
                      question,
                      valid,
                      definition)


def user_enter_boolean_response():
    """
    Prompts the user to enter a boolean response and returns its value in lower case.
    nothing -> str
    """
    return input('(y/n)').lower()
    

def get_did_do_label(definition):
    """
    Given a valid did do definition, returns its label.
    str -> str
    """
    return definition


def get_bool_from_response(response):
    """
    Given a valid bool response, returns the response in boolean form.
    str -> bool
    """
    return response == 'y'


def is_valid_boolean_response(response):
    """
    Returns true if a boolean response is valid.
    str -> bool
    """
    return response == 'n' or response == 'y'

def user_enter_note(definition):
    """
    Gets a note from the user.
    Returns it along with label for the value.
    A note is a str.
    Signature in config: note label
    str -> (label: str, value: str)
    """
    
    question = 'What notes if any do you have for {}?'
    valid = 'A valid response is a anything...I don\'t know how you got here'

    return user_enter(get_note_label, 
                      user_enter_note_response, 
                      get_note_from_response,
                      is_valid_note_response,
                      question,
                      valid,
                      definition)


def get_note_from_response(response):
    """
    Gets the note from a valid note response.
    str -> float
    """
    return float(response)

def is_valid_note_response(response):
    """
    Returns true if a note response is valid.
    str -> bool
    """
    return True

def user_enter_note_response():
    """
    Prompts the user to enter a note response.
    nothing -> str
    """
    return input('>> ')
    
def get_note_label(definition):
    """
    Given a valid note definition, returns its label.
    str -> str
    """
    return definition

def user_enter_key_event(definition):
    """
    Gets a key_event from the user.
    Returns it along with label for the value.
    A key_event is a str.
    Signature in config: key_event label
    str -> (label: str, value: str)
    """
    
    update_question = 'Have any important events occurred consurning {}?'
    valid_update_respones = 'A valid response is eather "y" for True or "n" for False.'
    
    update = user_enter(get_key_event_label, 
                      user_enter_boolean_response, 
                      get_bool_from_response,
                      is_valid_boolean_response,
                      update_question,
                      valid_update_respones,
                      definition)
    
    # If the user enters "yes"
    if update[1]:
        return (update[0], '')
    
    question = 'Enter your event(s)?'
    valid = 'A valid response is a any text.'

    return user_enter(get_key_event_label, 
                      user_enter_key_event_response, 
                      get_key_event_from_response,
                      is_valid_key_event_response,
                      question,
                      valid,
                      definition)

def get_key_event_label(definition):
    """
    Given a valid key event definition, returns its label.
    str -> str
    """
    return definition

def user_enter_key_event_response():
    """
    Prompts the user to enter a key event response.
    nothing -> str
    """
    return input('>> ')

def get_key_event_from_response(response):
    """
    Gets the key event from a valid key event response.
    str -> float
    """
    return response

def is_valid_key_event_response(response):
    """
    Returns true if a key event response is valid.
    str -> bool
    """
    return len(response) > 0

def user_enter_state_change(definition):
    """
    Gets a state_change from the user.
    Returns it along with label for the value.
    A state_change is a str.
    Signature in config: state_change label
    str -> (label: str, value: str)
    """
    update_question = 'Have any important events occurred consurning {}?'
    valid_update_respones = 'A valid response is eather "y" for True or "n" for False.'
    
    update = user_enter(get_key_event_label, 
                      user_enter_boolean_response, 
                      get_bool_from_response,
                      is_valid_boolean_response,
                      update_question,
                      valid_update_respones,
                      definition)
    
    # If the user enters "yes"
    if update[1]:
        return (update[0], '')
    
    question = 'Enter your event(s)?'
    valid = 'A valid response is a any text.'

    return user_enter(get_state_change_label, 
                      user_enter_state_change_response, 
                      get_state_change_from_response,
                      is_valid_state_change_response,
                      question,
                      valid,
                      definition)

def get_state_change_label(definition):
    """
    Given a valid key event definition, returns its label.
    str -> str
    """
    return definition

def user_enter_state_change_response():
    """
    Prompts the user to enter a key event response.
    nothing -> str
    """
    return input('>> ')

def get_state_change_from_response(response):
    """
    Gets the key event from a valid key event response.
    str -> float
    """
    return response

def is_valid_state_change_response(response):
    """
    Returns true if a key event response is valid.
    str -> bool
    """
    return len(response) > 0

def config_to_functions(config):
    """
    Takes in the data for a config and returns a list of functions to call the meet it's criteria.
    list of str -> list of (none -> str)
    """
    type_to_input_functions = get_type_map()

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
    if type not in get_type_map():
        raise ValueError(type + ' is not a valid type')


def check_config_line(line):
    """
    Checks that a given line in the config is valid.
    If not, throw an exception.
    str -> none or error
    """
    if len(line.split(' ', 1)) == 1:
        raise ValueError('Invalid config line: ' + line)


def get_type_map():
    """
    Returns a map of type names to input functions.
    none -> map of str to (str -> anything)
    """
    return {
        'value' : user_enter_value,
        'time' : user_enter_time,
        'did_do' : user_enter_did_do,
        'note' : user_enter_note,
        'key_event' : user_enter_key_event,
        'state_change' : user_enter_state_change
        }


def main():
    """
    Runs the program.
    """

    mock_config = ['value (0,10) stuff", "time Some stuff", "did_do otherStuff', 'key_event event', 'state_change change', 'note notworthy thing']

    input_functions = config_to_functions(mock_config)

    for func in input_functions:
        func()