import unittest
from data.base.webdriver import WebdriverHandler
from page_object.login import login
from helpers.data_fake import data_fake
from page_object.new_proveedor_medic import new_medic_proveedor



class MyTestCase(unittest.TestCase, WebdriverHandler):

    def setUp(self):
        self.my_class_instance = MyTestCase()
        # Inicia  el navegador.
        WebdriverHandler.__init__(self)
        self.driver.get("https://weepentest202102.azurewebsites.net/WeeClaims/#/Home/")




    def tearDown(self):
        # Este método se ejecuta después de cada prueba
        self.driver.quit()



    def test_add_medic_proveedor(self):
        login(self.driver, self.wait)
        data_fake_user = data_fake()
        result = new_medic_proveedor(self.driver, self.wait, data_fake_user[0], data_fake_user[1],
                            data_fake_user[2],data_fake_user[3],data_fake_user[4],data_fake_user[5],data_fake_user[6])

        self.assertIsNotNone(result,  "Error No se creo el nuevo proveedor")
