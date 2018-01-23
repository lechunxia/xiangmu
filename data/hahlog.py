#
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://test-books.maishumaishu.com/")
driver.maximize_window()
# 登录账户
driver.find_element_by_link_text("登录").click()
driver.implicitly_wait(30)
driver.find_element_by_name("cid").send_keys("lcx1")
driver.find_element_by_name("uid").send_keys("001")
driver.find_element_by_name("password").send_keys("123456")
driver.find_element_by_class_name("btn").click()
# driver.find_element_by_partial_link_text("登录").click()

# 搜索冰与火之歌这个产品
driver.find_element_by_name("key_words").send_keys("冰与火之歌")
driver.find_element_by_class_name("findicon").click()

# 进入该产品的产品详情页面
driver.find_element_by_css_selector("body > section > div:nth-child(2) > ul > li.funny.lineheight > a").click()
driver.implicitly_wait(30)

# 添加进入购物车
# driver.find_element_by_class_name("car-dot").click()   # 通过点击购物车图标
# driver.find_element_by_name("207849").clear()
driver.find_element_by_link_text("一键询价").click()
# driver.implicitly_wait(30)

# 进入购物车
# driver.find_element_by_css_selector("body > header > div.headbottom > ul > li.car > a").click()






