

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
    list of (str, any) -> none
    """
    
    print('Data Saved!')