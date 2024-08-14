import time

def proveedor_modulo(driver, wait):
    driver.get("https://weepentest202102.azurewebsites.net/WeeClaims/#/")
    time.sleep(2)
    proveedor_module = wait.waitForElement(locator="c1")
    wait.click(proveedor_module)