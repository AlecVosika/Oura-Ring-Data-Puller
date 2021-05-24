from configparser import ConfigParser


class GetconfigData:
    """
    Class used to access config.ini data
    """

    def __init__(self):
        # instantiate
        self.config = ConfigParser()
        # parse existing file
        self.config.read('config.ini')

    def GetClientId():
        """
        Function used by main.py to get the Client ID from the config.ini file

        Returns:
            client_ID: The client ID used to get data 
        """
        # Create object
        get_client_id = GetconfigData()
        # read values from a section
        client_id = get_client_id.config.get('config', 'client_id')

        return client_id

    def GetAccessToken():
        """
        Function used by main.py to get the Access Token from the config.ini file

        Returns:
            access_token: The Access Token used to get data 
        """
        # Create object
        get_access_token = GetconfigData()
        # read values from a section
        access_token = get_access_token.config.get('config', 'access_token')

        return access_token
