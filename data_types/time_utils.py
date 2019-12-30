import datetime

def respones_to_datetime(response, formate):
    """
    Parses a user string respones into a datetime object.
    str, str -> datetime
    """
    return datetime.datetime.strptime(response, formate)

def datatime_to_string(datetime, formate):
    """
    Converts a datetime object to a string.
    datetime, str -> str
    """
    return datetime.strftime(formate)