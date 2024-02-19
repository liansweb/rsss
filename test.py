import configparser
config = configparser.ConfigParser()

def read_config(filename: str):
    config.read(filename)

def main():
    pass

if __name__ == '__main__':
    config_path = 'config/opml.ini'
    main()