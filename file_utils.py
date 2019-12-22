import pandas

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
    
    data_frame.to_csv('saves\\save.csv')
    
    print('Data Saved!')
    
def data_to_data_frame(data):
    """
    Convers some data into a data frame.
    dic str to any -> data frame
    """
    return pandas.DataFrame(data)