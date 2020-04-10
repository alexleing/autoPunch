from time import sleep
from appium import webdriver
import os
import time
from appium.webdriver.common.touch_action import TouchAction


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0.0'
desired_caps['deviceName'] = 'xiaomi5'
desired_caps['app'] = 'C:\AppData\DXIM_signed.apk'  # 被测试的App在电脑上的位置
desired_caps['appPackage'] = 'com.pubinfo.sfim.dx'
desired_caps['appActivity'] = 'com.pubinfo.sfim.main.activity.WelcomeActivity'
desired_caps['noReset'] = 'true'


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
sleep(5)
# 进入微服务
TouchAction(driver).tap(x=984, y=1821).perform()
sleep(7)
# 进入考勤
TouchAction(driver).tap(x=967, y=808).perform()
sleep(15)
# 点击打卡
TouchAction(driver).tap(x=532, y=992).perform()
sleep(7)
# 点击退出
TouchAction(driver).tap(x=1009, y=134).perform()

driver.quit()
