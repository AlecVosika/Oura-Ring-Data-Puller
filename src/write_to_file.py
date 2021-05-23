
def WriteToFile(info):
    """
    Writes data for args

    Args:
        info : A list containing a dictionary
    """
    f = open("src/data.txt", "a")

    for date in info['sleep']:
        for key in date:
            f.write(str(key + ' = '))
            f.write(str(date[key]) + '\n')
    f.close()
