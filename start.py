import sys
import constants
from file_utils import save_data, open_file
from config_utils import config_to_functions
from formatting_utils import new_line_pad

def main():
    """
    Runs the program.
    """
    
    input_functions = []
    new_line = '\n'
    tab = '\t'
    
    try:
        config = open_file(constants.CONFIG_PATH)
        input_functions = config_to_functions(config)
        
    except Exception as e:
        print(constants.LINE)
        message = new_line_pad('An error occurred:' + new_line + str(e))
        print(message)
        return
    
    data = []
    
    print(new_line + new_line + constants.LINE)
    print(tab + tab + 'WELCOME TO LIFE LOGGER')
    print(constants.LINE + new_line)
    
    for func in input_functions:
        try:
            data.append(func())
        except:
            print(new_line_pad('Program Shutdown'))
            return
        print(new_line_pad(constants.LINE))
    
    save_data(data)

main()