from time import gmtime, strftime

def getdatetime():
    '''
    Gets current date and time

    Returns:
        str: Return date and time
    '''
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())

