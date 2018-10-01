import configparser


class ConfigAccess:


    # Config File parsing
    configParser = configparser.RawConfigParser()
    configFilePath = r'/home/pavitra/Documents/workspace_python/Python_Programs_11/python_assignment_2/config.csv'
    configParser.read(configFilePath)
    file_path = configParser.get('p-config', 'filepath')
    file_name = configParser.get('p-config', 'filename')
    delimiter = configParser.get('p-config', 'delimiter')
    date_format = configParser.get('p-config', 'date_format')
    sender_email = configParser.get('p-config', 'sender_email')