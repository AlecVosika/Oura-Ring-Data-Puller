from configparser import ConfigParser


def GetClientId():
    """
    Function used by main.py to get the Client ID from the config.ini file

    Returns:
        client_ID: The client ID used to get data 
    """
    # instantiate
    config = ConfigParser()

    # parse existing file
    config.read('config.ini')

    # read values from a section
    client_id = config.get('config', 'client_id')

    return client_id


def GetAccessToken():
    """
    Function used by main.py to get the Access Token from the config.ini file

    Returns:
        access_token: The Access Token used to get data 
    """
    # instantiate
    config = ConfigParser()

    # parse existing file
    config.read('config.ini')

    # read values from a section
    access_token = config.get('config', 'access_token')

    return access_token
