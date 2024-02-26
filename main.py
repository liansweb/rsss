from src.start import script
from src.start import handle

KEYWORDS = {
    'CONFIG_INI':'src/ini/config.ini',
    'OPML_INI':'src/ini/opml.ini',
}


def main():
    """
    The main function that initializes the app, imports a test module, and handles the core functionality.
    """
    app_start = script(**KEYWORDS)
    from src.config.get import test
    # test()
    handle_core = handle()
    handle_core.core()
    

if __name__ == '__main__':  
    main()