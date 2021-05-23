from configparser import ConfigParser


def GetClientId():
    # instantiate
    config = ConfigParser()

    # parse existing file
    config.read('config.ini')

    # read values from a section
    client_id = config.get('config', 'client_id')

    return client_id


def GetAccessToken():
    # instantiate
    config = ConfigParser()

    # parse existing file
    config.read('config.ini')

    # read values from a section
    access_token = config.get('config', 'access_token')

    return access_token
