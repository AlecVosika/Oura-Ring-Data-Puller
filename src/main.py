from oura import OuraClient
from write_to_file import WriteToFile
from get_config import *


class Main:

    def __init__(self):
        # Gets the Client ID
        self.client_id = GetconfigData.GetClientId()
        # Gets the Access Token
        self.access_token = GetconfigData.GetAccessToken()
        # Request variable used to pull data from Oura
        self.request = OuraClient(client_id=f'{self.client_id}',
                                  access_token=f'{self.access_token}')


def main():

    # Create object
    oura = Main()

    # gets general user info and prints to debug console
    who_am_i = oura.request.user_info()
    print(who_am_i, "\n")

    info = oura.request.sleep_summary("2021-5-21")
    WriteToFile(info)
    print("Done")


if __name__ == '__main__':
    main()
