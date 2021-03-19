from .GetChromePro import get_chromedriver
from random import uniform, randint
from time import sleep


def bet_at_home(usern, passw):
    driver_bet_at_home = get_chromedriver()
    driver_bet_at_home.get('https://www.bet-at-home.com/')
    auto =False
    if auto:
        consent_popup = driver_bet_at_home.find_element_by_xpath('//*[@id="cookieConsentPopup"]/div/div/div[1]/p[2]/a[2]')
        consent_popup.click()

        sleep(uniform(2, 4))

        username = driver_bet_at_home.find_element_by_xpath('//*[@id="loginId"]')
        username.clear()
        username.send_keys(usern)
        password = driver_bet_at_home.find_element_by_xpath('//*[@id="loginPassword"]')
        password.clear()
        password.send_keys(passw)
        driver_bet_at_home.find_element_by_xpath('//*[@id="btnLogin"]').click()
        sleep(uniform(15, 16))
        capital = float(driver_bet_at_home.find_element_by_xpath('//*[@id="menubarAux"]/div[1]/ul/li['
                                                                 '3]/span/span/strong/span[1]').text)

        return driver_bet_at_home, capital
    else:
        capital = input("Capital:")
        k = input("Give Start for bookmaker:")
        while k != "go":
            k = input("Again")
        return driver_bet_at_home, capital


def random_location(height, width):
    newHeight = randint(0, height)
    newWidth = randint(0, width)
    return newHeight, newWidth


def bet_365(usern, passw):
    driver_bet_365 = get_chromedriver(use_proxy=True)
    auto = False
    driver_bet_365.get('https://www.bet365.com/')
    sleep(3)
    if auto:
        # sleep(uniform(10, 15))
        driver_bet_365.find_element_by_class_name('hm-MainHeaderRHSLoggedOutWide_Login').click()

        # sleep(uniform(7, 18))
        sleep(2)
        username = driver_bet_365.find_element_by_class_name('lms-StandardLogin_Username')
        username.clear()
        username.send_keys(usern)
        # sleep(randint(8, 16))
        sleep(2)
        password = driver_bet_365.find_element_by_class_name('lms-StandardLogin_Password')
        password.clear()
        password.send_keys(passw)
        # sleep(randint(9, 20))
        sleep(2)
        driver_bet_365.find_element_by_class_name('lms-StandardLogin_LoginButton').click()
        # sleep(randint(4, 13))
        sleep(2)
        driver_bet_365.find_element_by_class_name('hm-MainHeaderMembersWide_MembersMenuIcon').click()
        sleep(2)
        capital = int(str(driver_bet_365.find_element_by_class_name('um-UserInfo_Balance').text).lstrip('$').split('.')[0])
        return driver_bet_365, capital
    else:
        capital = input("Capital:")
        k = input("Give Start for bookmaker:")
        while k != "go":
            k = input("Again")
        return driver_bet_365, capital