from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import threading

# when game over


def quit_game():

    print('Your score was: ' + score)
    driver.quit()


def play_game():
    # opens game site
    driver = webdriver.Firefox()
    driver.get("https://play2048.co/")

    # sends keys?
    elem = driver.find_element_by_tag_name('body')

    for i in range(100):
        for k in range(50):
            elem.send_keys(Keys.UP)
            elem.send_keys(Keys.RIGHT)
        elem.send_keys(Keys.LEFT)
        score = driver.find_element_by_class_name('score-container').text

        keepGoing = driver.find_element_by_class_name("game-container")
        if 'Game over!' in keepGoing.text:
            print('Your score was: ' + score)
            driver.quit()
            break


gameThreads = []
for i in range(1):
    gameThread = threading.Thread(target=play_game)
    gameThreads.append(gameThread)
    gameThread.start()
