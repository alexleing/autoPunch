from time import sleep
from appium import webdriver
import os
import time
from appium.webdriver.common.touch_action import TouchAction


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0.0'
desired_caps['deviceName'] = 'xiaomi5'
desired_caps['app'] = 'C:\AppData\shopping_v5.5.0_71_2019-02-26_uatshareAble.apk' # 被测试的App在电脑上的位置
desired_caps['appPackage'] = 'com.maxxipoint.android'
desired_caps['appActivity'] = 'com.maxxipoint.android.shopping.activity.WelcomeActivity'
desired_caps['noReset'] = 'true'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# 4725 4726 4723
sleep(5)   # sleep()的作用，当网络时间差，页面加载不出来的时候，需要等待几秒，要不然找不到需要定位的组件，就会报错

TouchAction(driver).tap(x=969, y=1820).perform()
TouchAction(driver).tap(x=299, y=1165).perform()
TouchAction(driver).tap(x=566, y=713).perform()
TouchAction(driver).tap(x=573, y=547).perform()
driver.find_element_by_xpath('	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.'
                             'FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.'
                             'RelativeLayout/android.support.v4.view.ViewPager/android.widget.'
                             'LinearLayout/android.widget.LinearLayout/android.support.v4.view.'
                             'ViewPager/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.'
                             'RelativeLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.'
                             'support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.'
                             'LinearLayout/android.widget.ImageView').click()
sleep(7)
driver.quit()
