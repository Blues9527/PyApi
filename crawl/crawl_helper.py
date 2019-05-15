# coding:utf8

import ssl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from database.db_helper import DBHelper


class Crawl:
    def __init__(self):
        self.browser = webdriver.Chrome('E:\chromedriver_win32\chromedriver')
        self.browser.get('http://www.rastargame.com/')

    def print_content(self):
        main_content = self.browser.find_elements_by_class_name('IndMainBox')

        for sub_content in main_content:
            game_names = sub_content.find_elements_by_class_name('text_big')
            game_slogens = sub_content.find_elements_by_class_name('text_small')

            j = 1
            for game_name, game_slogen in zip(game_names, game_slogens):
                if tuple(DBHelper().db_select(
                        'select * from game where game_name = \'%s\' and  game_slogen = \'%s\'' % (
                                game_name.text, game_slogen.text))).__len__() == 0:
                    DBHelper().db_execute(
                        'insert into game(game_name,game_slogen) values (\'%s\',\'%s\')' % (
                            game_name.text, game_slogen.text))

                print(str(j) + '.' + game_name.text + "\n")
                print(str(j) + '.' + game_slogen.text + "\n")
                j += 1

            self.quit()

    def quit(self):
        self.browser.quit()


Crawl().print_content()
