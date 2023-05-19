import pytest

from pageObjects.LoginPage import loginpage
from utilites import XLutils
from utilites.readproperties import Readconfig
from utilites.Logger import LogGenerator


class Test_Login_DDT:
    Url = Readconfig.geturl()
    # username = Readconfig.getusername()
    # password = Readconfig.getpassword()
    log = LogGenerator.loggen()
    path = "C:\\Users\\Dhaval Patel\\PycharmProjects\\OrangeeHrmm\\testCases\\TestData\\LoginData.xlsx"


    def test_login_ddt_006(self, setup):
        self.driver = setup
        self.log.info("test_login_ddt_006 is started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Go to this url-->" + self.Url)
        self.lp = loginpage(self.driver)
        self.rows = XLutils.getrowCount(self.path, 'Sheet1')
        print("Number of rows are --->", self.rows)
        login_stuats=[]
        for r in range(2, self.rows+1):
            self.username = XLutils.readData(self.path, 'Sheet1',r,2)
            self.password = XLutils.readData(self.path, 'Sheet1', r, 3)

            self.lp.Enter_UserName(self.username)
            self.log.info("Entering username-->" + self.username)
            self.lp.Enter_Password(self.password)
            self.log.info("Entering password-->" + self.password)
            self.lp.Click_Login()
            self.log.info("Click on login button")

            if self.lp.Login_Status() == True:

                self.driver.save_screenshot(
                    "C:\\Users\\Dhaval Patel\\PycharmProjects\\OrangeeHrmm\\ScreenShots\\"+self.username+self.password+"test_login_ddt_006-pass.png")
                self.lp.Click_MenuButton()
                self.log.info("Click on Menu button")
                self.lp.Click_Logout()
                self.log.info("Click on logout button")

                login_stuats.append("Pass")
                XLutils.writeData(self.path, 'Sheet1', r, 4,"Pass")
            else:

                login_stuats.append("Fail")
                XLutils.writeData(self.path, 'Sheet1', r, 4, "Fail")
                self.driver.save_screenshot(
                    "C:\\Users\\Dhaval Patel\\PycharmProjects\\OrangeeHrmm\\ScreenShots\\"+self.username+self.password+"test_login_ddt_006-fail.png")
                #assert False

        print(login_stuats)
        if "Fail" not in login_stuats:
            self.log.info("test_login_ddt_006 is Passed")
            assert True
        else:
            self.log.info("test_login_ddt_006 is Failed")
            assert False
        self.driver.close()
        self.log.info("test_login_ddt_006 is Completed")


# pytest -v -n=3 --html=Reports/report.html -m sanity -p no:warnings