from selenium import webdriver
from common.configuration import Configuration


_driver_instance    = None
_configuration      = Configuration()

def get_driver():
    global _driver_instance
    if not _driver_instance:
        command_executor = "{}://{}:{}{}".format(
            Configuration.get('protocol'),
            Configuration.get('host'),
            Configuration.get('port'),
            Configuration.get('path')
        )
        _driver_instance = webdriver.Remote(
            command_executor=command_executor,
            desired_capabilities=Configuration.get("capabilities")
        )
        _driver_instance.implicitly_wait(0)

        win_size = Configuration.get('window_size')
        if win_size == 'maximize':
            _driver_instance.maximize_window()
        else:
            _driver_instance.set_window_size(*win_size)

    return _driver_instance

def close_driver():
    global _driver_instance
    if _driver_instance:
        _driver_instance.quit()
        _driver_instance = None