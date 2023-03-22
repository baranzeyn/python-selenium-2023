from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSauce:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")
        sleep(2)

    def login(self, username, passw):
        username_input = self.driver.find_element(By.ID, "user-name")  # username inputunu seçtin
        passw_input = self.driver.find_element(By.ID, "password")  # passw inputunu seçtin
        sleep(2)
        # blank test vakti
        username_input.send_keys(username)
        passw_input.send_keys(passw)
        sleep(2)

        login_btn = self.driver.find_element(By.ID, "login-button")  # login butonunu seçtin
        sleep(2)

        login_btn.click()
        sleep(2)

    def username_psw_blank_test(self):
        """
        test case 1:
        Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak
         "Epic sadface: Username is required" gösterilmelidir.
        """
        self.driver.refresh()
        sleep(2)
        tester.login("", "")
        error_msg = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        sleep(3)
        result = error_msg.text == "Epic sadface: Username is required"  # doğruluk durumu kontrolü
        if result:
            print("test 1 passed")

    def username_psw_blank_test_second_part(self):
        """
        test case 2:
    Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır.
    Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır.
    (Tek test casede işleyiniz)
        """
        self.driver.refresh()
        sleep(2)

        tester.login("", "")

        error_msg = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        sleep(3)

        result = error_msg.text == "Epic sadface: Username is required"  # doğruluk durumu kontrolü
        if result:
            error_msg_x = self.driver.find_element(By.XPATH,
                                                   "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
            sleep(2)

            error_msg_x.click()
            sleep(2)

            try:
                username_x = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/svg")
                passw_x=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/svg")
                sleep(2)
            except:
                print("test 2 passed")
            else:
                print("test 2 failed")
        else:
            print("test 2 failed")

    def username_psw_test(self):
        """
        test case 3:
        Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde
         "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
        """
        self.driver.refresh()
        sleep(2)

        tester.login("locked_out_user", "secret_sauce")

        error_msg = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]")
        result = error_msg.text == "Epic sadface: Sorry, this user has been locked out."

        if result:
            print("test 3 passed")
        else:
            print("something went wrong. test 3 failed.")

    def passw_blank_test(self):
        """
        test case 4:
        Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak
        "Epic sadface: Password is required" gösterilmelidir.
        """
        self.driver.refresh()
        sleep(2)

        tester.login("locked_out_user", "")

        error_msg = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        sleep(3)

        result = error_msg.text == "Epic sadface: Password is required"
        if result:
            print("test 4 passed")
        else:
            print("test 4 failed")

    def username_psw_test_second_ver(self):
        """
        test case 5:
        Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı
        "/inventory.html" sayfasına gönderilmelidir.
        """
        self.driver.refresh()
        sleep(2)

        tester.login("standard_user", "secret_sauce")
        current_url = self.driver.current_url
        result=current_url=="https://www.saucedemo.com/inventory.html"
        
        if result:
            print("test 5 passed")
        else:
            print("test 5 failed")

    def check_product_list(self):
        """
        Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.
        """
        self.driver.get("https://www.saucedemo.com/")

        tester.login("standard_user", "secret_sauce")
        self.driver.get("https://www.saucedemo.com/inventory.html")
        sleep(5)
        list_of_products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        sleep(2)
        print(len(list_of_products))
        result = len(list_of_products) == 6
        if result:
            print("test 6 passed")
        else:
            print("test 6 failed")


tester = TestSauce()

tester.username_psw_blank_test()
tester.username_psw_blank_test_second_part()
tester.username_psw_test()
tester.passw_blank_test()
tester.username_psw_test_second_ver()
tester.check_product_list()