import time

def new_medic_proveedor(driver, wait, rfc, cedula, first_name,second_name, firs_last_name, second_last_name, birthday, curp):
    action_buttom = wait.waitForElement(locator="//button[contains(text(), 'Acciones') and @data-toggle='dropdown']")
    wait.click(action_buttom)
    time.sleep(1)
    add_proveedor_medic = wait.waitForElement(locator="ProveedorNewMedico")
    wait.click(add_proveedor_medic)
    time.sleep(3)
    rfc_put = wait.waitForElement(locator="frmNewProveedorM_txtRFC")
    wait.sendKeys(rfc, rfc_put)

    cedula_input = wait.waitForElement(locator="frmNewProveedorM_txtBuscaCedula")
    wait.sendKeys(cedula, cedula_input)

    first_name_input =  wait.waitForElement(locator="frmNewProveedorM_txtNombre")
    wait.sendKeys(first_name, first_name_input)
    wait.sendKeys(second_name, first_name_input)

    last_name_input = wait.waitForElement(locator="frmNewProveedorM_txtApeidoP")
    wait.sendKeys(firs_last_name, last_name_input)

    second_last_name_input = wait.waitForElement(locator="frmNewProveedorM_txtApeidoP")
    wait.sendKeys(second_last_name, second_last_name_input)

    birthday_input = wait.waitForElement(locator="frmNewProveedorM_txtFechaNac")
    wait.sendKeys(birthday, birthday_input)

    curp_input = wait.waitForElement(locator="frmNewProveedorM_txtCURP")
    wait.sendKeys(curp, curp_input)

    register_buttom = wait.waitForElement(locator="btnProveedorM_newProveedorM")
    wait.click(register_buttom)
    return register_buttom






