from time import sleep
from selenium.common.exceptions import NoSuchElementException
from random import uniform


def bookmaker_bots(driver, book, bet, link, amount):
    if book == 10:
        return bet_365_bot(driver, bet, link, amount)
    elif book == 23:
        return bet_at_home_bot(driver, bet, link, amount)


def bet_365_bot(driver, bet, link, amount):
    driver.get(link)
    succ_bet = 0
    sleep(uniform(2, 5))
    i = driver.find_element_by_class_name('bss-StakeBox_StakeValueInput')
    i.send_keys(str(amount))
    try:
        accept_changes = driver.find_element_by_class_name('bs-AcceptButton')
    except NoSuchElementException:
        driver.find_element_by_class_name('bss-PlaceBetButton').click()
        succ_bet += 1
        return succ_bet, amount
    else:
        accept_changes.click()
        sleep(uniform(0.5, 1))
        driver.find_element_by_class_name('bss-PlaceBetButton').click()
        succ_bet += 1
        return succ_bet, amount


def bet_at_home_bot(driver, bet, link, amount):
    driver.get(link)
    sleep(uniform(2, 5))
    suc_bet = 0

    i = driver.find_element_by_xpath('//*[@id="StakePerBetInput"]')
    status = driver.find_element_by_xpath('//*[@id="OrderStatus-Valid"]').get_attribute('id')

    i.send_keys(str(amount))
    sleep(uniform(0.5, 1))
    if status != 'OrderStatus-Valid':

        # OrderStatus - OddChanged
        # 'OrderStatus-InvalidTip'
        return suc_bet, amount
    else:
        next_button = driver.find_element_by_xpath('//*[@id="BtnOrderCheck"]')
        next_button.click()
        sleep(uniform(0.5, 1))
        status = driver.find_element_by_xpath('//*[@id="OrderStatus-Valid"]').get_attribute('id')

    if status != 'OrderStatus-Valid':
        return suc_bet, amount
    else:
        place_order_button = driver.find_element_by_xpath('//*[@id="BtnOrderPlace"]')
        place_order_button.click()
        sleep(uniform(0.5, 1))

    try:
        tip = driver.find_element_by_xpath('//*[@id="OrderStatus-InvalidTip"]').get_attribute('id')
    except NoSuchElementException:
        sleep(uniform(0.5, 1))
    else:
        while tip == 'OrderStatus-InvalidTip':
            i.send_keys(str(amount - (amount*50)/100))
            amount = amount - (amount*50)/100
            driver.find_element_by_xpath('//*[@id="BtnOrderCheck"]').click()
            sleep(uniform(0.5, 1))
            # driver.find_element_by_xpath('//*[@id="BtnOrderCheck"]').click()
            driver.find_element_by_xpath('//*[@id="BtnOrderPlace"]').click()
            sleep(uniform(1, 2))
            tip = driver.find_element_by_xpath('//*[@id="OrderStatus-InvalidTip"]').get_attribute('id')
    finally:
        sleep(uniform(1, 2))
        if driver.find_element_by_xpath('//*[@id="OrderStatus-Saved"]').get_attribute('id') != 'OrderStatus-Saved':
            return suc_bet, amount
        else:
            sleep(uniform(0.5, 1))
            ok_button = driver.find_element_by_xpath('//*[@id="BtnOrderFinalize"]')
            ok_button.click()
            suc_bet += 1
            return suc_bet, amount

    # "The maximum number of tips for this bet was exceeded."
    #
    # "The odds have changed or the selected bets are no longer available."


# //*[@id="OrderStatus-Error"]

# <div ng-attr-id="OrderStatus-{{bs.OrderStatusNames[bs.orderStatus]}}" class="hib-content-text" ng-bind-html="bs.orderStatusText" id="OrderStatus-Error">An error has occurred.</div>