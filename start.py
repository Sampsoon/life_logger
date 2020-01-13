import sys
import constants
from file_utils import save_data, open_file, get_file_name_from_path
from config_utils import config_to_functions
from formatting_utils import new_line_pad, NEW_LINE, TAB
from data_types.time_utils import respones_to_datetime, datatime_to_string

def main():
    """
    Runs the program.
    void -> void
    """
    config_path = sys.argv[1] if len(sys.argv) > 1 else constants.DEFAULT_CONFIG_PATH
    name = get_file_name_from_path(config_path)
    
    print(NEW_LINE + NEW_LINE + constants.LINE)
    print(TAB + TAB + 'WELCOME TO LIFE LOGGER')
    print(constants.LINE + NEW_LINE)
    
    try:
        input_functions = try_config_to_input_functions(config_path)
        data = try_get_data_from_function(input_functions)
        data['date'] =  get_date()
        print(NEW_LINE + constants.LINE)
        try_save_data(data, name)
    except Exception as e:
        print(e)

def get_date():
    """
    Asks the user what the date that they are logging for and returns it.
    void -> str
    """
    date_time = None
    while date_time == None:
        print('What date are logging for?')
        date = input('Date: ')
        if is_valid_date(date):
            date_time = respones_to_datetime(date, constants.DATETIME_FORMATE_JUST_DATE)
        else:
            print(NEW_LINE + 'Not a valid date')
            print('write is this formate: MM/DD/YY' + NEW_LINE)
    return datatime_to_string(date_time, constants.DATETIME_FORMATE_JUST_DATE)

def is_valid_date(date):
    """
    Returns true if a given date representation is valid.
    str -> bool
    """
    try:
        respones_to_datetime(date, constants.DATETIME_FORMATE_JUST_DATE)
        return True
    except ValueError:
        return False
    

def try_config_to_input_functions(config_path):
    """
    Tries to create a list of input functions based off a read in config.
    str -> list of (void -> (str, any))
    """
    input_functions = []
    
    try:
        config = open_file(config_path)
        input_functions = config_to_functions(config)
        
    except Exception as e:
        message = constants.LINE + NEW_LINE + new_line_pad('An error occurred:' + NEW_LINE + str(e))
        raise Exception(message)
            
    return input_functions

def try_get_data_from_function(input_functions):
    """
    Tries to get the data from the user input functions.
    list of (void -> (str, any)) -> dic str to any 
    """
    data = {}
    
    for func in input_functions:
        try:
            data_to_log = func()
            data[data_to_log[0]] = data_to_log[1]
        except:
            raise Exception(new_line_pad('Program Shutdown'))
        print(new_line_pad(constants.LINE))
        
    return data
    
def try_save_data(data, name):
    """
    Tries to saves some data.
    dic str to any, str -> none
    """
    try:
        save_data(data, name)
    except Exception as e:
        message = 'There was an error saving the logged data:' + NEW_LINE + str(e)
        raise Exception(message)
    
main()