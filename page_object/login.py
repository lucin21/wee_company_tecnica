import time

def login(driver, wait):
    driver.get("https://weepentest202102.azurewebsites.net/WeeClaims/#/")
    time.sleep(2)
    email_input = wait.waitForElement(locator="frmMasterLogin_UserName")
    wait.sendKeys("ale3@weecompany.net", email_input)
    password_input = wait.waitForElement(locator="frmMasterLogin_Password")
    wait.sendKeys("$isis.demo01C", password_input)
    time.sleep(2)
