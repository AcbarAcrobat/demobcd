import selenium.webdriver.chrome.webdriver


command_executor = "{}://{}:{}{}".format(
            "http",
            "localhost",
            "4444",
            "/wd/hub"
        )
        _driver_instance = selenium.webdriver.chrome.webdriver.WebDriver.Remote(
            command_executor=command_executor,
            desired_capabilities=
                           {
                               "browserName": 'chrome',
                               "unexpectedAlertBehaviour": 'accept',
                               "enableVNC": True,
                               "screenResolution": "1920x1080x24",
                               "loggingPrefs": {
                                   "browser": "INFO"
                               },
                               "chromeOptions": {
                                   "args": ['--disable-infobars']
                               }
                           }

        )
        _driver_instance.implicitly_wait(0)