url: "http://vm-biocad-filestorage.axmor.nsk:8085/?track=fb8a1ddd-f7e3-492b-9cf2-64674442ce38"
implicit_timeout: 5

capabilities:
    browserName: 'chrome'
    unexpectedAlertBehaviour: 'accept'
    enableVNC: True
    screenResolution: "1920x1080x24"
    # enableVideo: true
    # videoFrameRate: 60
    loggingPrefs:
        browser: "INFO"
    chromeOptions:
        args: ['--disable-infobars', '--window-size=1920,1080']
