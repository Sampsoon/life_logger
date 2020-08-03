from config_utils import user_enter, function_maker, is_type, get_command_type, get_command_definition, on_not_valid_type, type_to_input_functions
import constants
import data_types.did_do as bool_lib

def build_if_yes_function(definition):
    """
    Builds a function given a conditional bool response to a question to the user gets the data for a given data type from the user.
    Raises an error if the definition is not valid.
    str -> (() -> (label: str, value: float)) or error
    """
    return function_maker(user_enter_if_yes,
                          definition, is_valid_if_yes_definition,
                          "Not a valid if_yes definition: " + definition)

def is_valid_if_yes_definition(definition):
    """
    Returns true if the if_yes definition is valid.
    str -> bool
    """
    if definition.count(constants.QUESTION_DENOTE) < 2 or definition[0] != constants.QUESTION_DENOTE:
        return False

    # First char is white space so it needs to be removed.
    if_true = get_data_logged_on_true(definition)

    data_type = get_command_type(if_true)
    if not is_type(data_type):
        on_not_valid_type(data_type)

    data_type_definition = get_command_definition(if_true)

    # The validation logic is called upon this function call.
    type_to_input_functions(data_type, data_type_definition)

    return True

def user_enter_if_yes(definition):
    """
    Asks the user a question the text of which is defineind in the definition.
    If true, prompts the user the enter a value of a data type.
    Returns it along with label for the value.
    Signature in config: if "boolean question" data_type data_type_definition
    Note: Quotes are included
    str -> (label: str, value: any)
    """
    update_question = get_question_text(definition)
    
    update = user_enter(get_question_text, 
                      bool_lib.user_enter_boolean_response, 
                      bool_lib.get_bool_from_response,
                      bool_lib.is_valid_boolean_response,
                      update_question,
                      bool_lib.VALID_BOOL_RESPONSE,
                      definition)

    # If the user enters "yes"
    if not update[1]:
        return (update[0], '')
    
    if_true = get_data_logged_on_true(definition)
    data_type = get_command_type(if_true)
    data_type_definition = get_command_definition(if_true)

    # The validation logic is called upon this function call.
    return type_to_input_functions(data_type, data_type_definition)()


def get_question_text(definition):
    """
    Returns the text for the question that is being asked to the user.
    str -> str
    """
    return definition.split(constants.QUESTION_DENOTE, 1)[1].rsplit(constants.QUESTION_DENOTE, 1)[0]

def get_data_logged_on_true(definition):
    """
    Returns the description of the data that is logged if the user's answer is yes.
    Basically everything based the question.
    str -> str
    """
     # First char is white space so it needs to be removed.
    return definition.rsplit(constants.QUESTION_DENOTE, 1)[1][1:]