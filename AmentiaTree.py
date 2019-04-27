# -*- coding:UTF-8 -*-

from  selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time, sys, random, os
from selenium.webdriver.common.action_chains import ActionChains
from collections import deque
import threading


username="username" 
passwd="passwd"
url='lessonURL'

css_selector="[class='clearfix video children']"
global courseList

def viewControlBar():
    while True:
        try:
            time.sleep(1)
            browser.execute_script("document.getElementsByClassName('controlsBar')[0].style.display='block'")
            break
        except:
            continue

def setPlayerOn():
    while True:
        try:
            player = browser.find_element_by_id('vjs_mediaplayer_html5_api')
            browser.execute_script("return arguments[0].play()", player)
            return True
        except:
            continue



def getCourseList(css_selector):
    while True:
        tmp = []
        try:
            courseList=browser.find_elements_by_css_selector(css_selector)
            for course in courseList:
                if course.get_attribute("watchstate") == "0" or course.get_attribute("watchstate") == "2":
                    tmp.append(course)
            break
        except:
            continue
    return tmp


def closeDialog():
    while True:
        try:
            time.sleep(5)
            browser.switch_to_frame("tmDialog_iframe")
            browser.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[2]/label/input").click()
            browser.switch_to.default_content()
            time.sleep(3)
            browser.execute_script("document.getElementsByClassName('popbtn_cancel')[0].click()")
        except:
            continue

def login():
    browser.get(url)
    browser.implicitly_wait(10)
    browser.find_element_by_xpath('//*[@id="lUsername"]').send_keys(username)
    browser.find_element_by_xpath('//*[@id="lPassword"]').send_keys(passwd)
    browser.find_element_by_xpath('//*[@id="f_sign_up"]/div/span').click()


def playPreProcess():
    while True:
        try:
            time.sleep(0.5)
            viewControlBar()
            browser.find_element_by_class_name("speedBox").click()
            browser.find_element_by_class_name("speedTab15").click()
            browser.find_element_by_class_name("volumeIcon").click()
            break
        except:
            continue

def isVideoDone():
    try:
        viewControlBar()
        ct = browser.find_element_by_class_name("currentTime").text
        dr = browser.find_element_by_class_name("duration").text
        if ct==dr:
            return True
        else:
            False
    except:
        return False

def closeExamDialog():
    while True:
        try:
            time.sleep(1)
            browser.execute_script("document.getElementsByClassName('popup_delete')[0].click()")
            print("CloseExamDialog Out")
            return True
        except:
            continue


def nextVideo():
    global courseList
    e = courseList.popleft()
    while True:
        try:
            e.click()
            time.sleep(3)
            playPreProcess()
            setPlayerOn()
            return True
        except:
            continue

def run():
    global courseList
    login()
    time.sleep(5)
    print("%s Begin Running" % time.strftime("%y-%m-%d %H:%M:%S", time.localtime()))
    playPreProcess()
    setPlayerOn()
    while True:
        courseList = deque(getCourseList(css_selector))
        if isVideoDone():
            nextVideo()
            print("%s New Running" % time.strftime("%y-%m-%d %H:%M:%S",time.localtime()))
            time.sleep(3)
        time.sleep(1)



if __name__=="__main__":
    threads=[]
    t1=threading.Thread(target=closeDialog)
    t2=threading.Thread(target=closeExamDialog)

    threads.append(t1)
    threads.append(t2)

    for t in threads:
        t.start()

    browser = webdriver.Chrome()
    run()


