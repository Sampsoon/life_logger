from config_utils import user_enter, function_maker, is_type, get_command_type, get_command_definition, on_not_valid_type, type_to_input_functions
import constants

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
    question_denote = '"'
    if definition.count(question_denote) < 2 or definition[0] != question_denote:
        return False

    # First char is white space so it needs to be removed.
    if_true = definition.rsplit(question_denote, 1)[1][1:]

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
    pass