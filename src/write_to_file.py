
def WriteToFile(info):
    """
    Writes data to src/data.txt file for args

    Args:
        info : A list containing a dictionary
    """
    f = open("src/data.txt", "a")

    for date in info['sleep']:
        for key in date:
            f.write(str(key + ' = '))
            f.write(str(date[key]) + '\n')
        f.write(str('\n'))
    f.close()
