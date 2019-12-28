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

def save_data(data):
    """
    Saves the logged data to a file.
    dic str to any -> none
    """
    data_frame = data_to_data_frame(data)
    
    if file_in_folder(constants.SAVE_DATA_PATH):
        add_data_to_file(data_frame)
    else:
        save_to_new_file(data_frame)
    
    print('Data Saved!')

def add_data_to_file(data):
    """
    Adds data a scv file.
    data frame -> void
    """
    print('was here!')

def save_to_new_file(data):
    """
    Saves the data to a new file.
    data frame -> void
    """
    data.to_csv(constants.SAVE_DATA_PATH)

def file_in_folder(file_path):
    """
    Returns true if a file is in a folder.
    str -> bool
    """
    return path.exists(constants.SAVE_DATA_PATH)
    
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