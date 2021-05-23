from oura import OuraClient
from write_to_file import WriteToFile
from get_config import *


def main():
    client_id = GetClientId()
    access_token = GetAccessToken()

    oura = OuraClient(client_id=f'{client_id}',
                      access_token=f'{access_token}')

    who_am_i = oura.user_info()
    print(who_am_i, "\n")

    info = oura.sleep_summary("2021-5-21")
    WriteToFile(info)
    print("Done")


if __name__ == '__main__':
    main()
