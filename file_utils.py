import pandas
import constants
from os import path

def open_file(filename):
    """
    Take in a file name and returns its contents has a list of file lines.
    string -> list of strings
    """
    file = open(filename)
    file_data = [line for line in file]
    file.close()

    return file_data

def save_data(data, name):
    """
    Saves the logged data to a file.
    dic str to any, str -> none
    """
    data_frame = data_to_data_frame(data)
    
    file_path = get_save_file_path(name)
    
    if file_in_folder(file_path):
        add_data_to_file(data_frame, file_path)
    else:
        save_to_new_file(data_frame, file_path)
    
    print('Data Saved!')

def get_save_file_path(name):
    """
    Returns the save file path of a file given its name.
    str -> str
    """
    return constants.SAVE_DATA_PATH + constants.SAVED_DATA_NAME_TAG + '_' + name + '.csv'

def add_data_to_file(data, file_path):
    """
    Adds data a scv file.
    data frame, str -> void
    """
    file_data = pandas.read_csv(file_path)
    new_data = file_data.append(data, ignore_index=True, sort=True)
    save_to_new_file(new_data, file_path)

def save_to_new_file(data, file_path):
    """
    Saves the data to a new file.
    data frame, str -> void
    """
    data.to_csv(file_path)

def file_in_folder(file_path):
    """
    Returns true if a file is in a folder.
    str -> bool
    """
    return path.exists(file_path)
    
def data_to_data_frame(data):
    """
    Convers some data into a data frame.
    dic str to any -> data frame
    """
    data = dic_values_to_list(data)
    return pandas.DataFrame(data)

def dic_values_to_list(dic):
    """
    Returns a new dictionary with all its values wrapped in lists. 
    dic -> dic of any to list
    """
    new_dic = {}
    for key in dic.keys():
        new_dic[key] = [dic[key]]
    return new_dic