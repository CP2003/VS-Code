Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def sessionGenerator(sessionFilePath):
  
    # 1.1 Open Chrome browser
    browser = webdriver.Chrome()
  
    # 1.2 Open Web Whatsapp
    browser.get("https://web.whatsapp.com/")
  
    # 1.3 Ask user to scan QR code
    print("Waiting for QR code scan...")
  
    # 1.4 Wait for QR code to be scanned
    _wait_for_presence_of_an_element(
      browser, MAIN_SEARCH_BAR__SEARCH_ICON)
  
    # 1.5 Execute javascript in browser and 
    # extract the session text
    session = browser.execute_script(EXTRACT_SESSION)
  
    # 1.6 Save file with session text file with
    # custom file extension ".wa"
    with open(sessionFilePath, "w", encoding="utf-8") as sessionFile:
        sessionFile.write(str(session))
  
    print("Your session file is saved to: " + sessionFilePath)
  
    # 1.7 Close the browser
    browser.close()
    