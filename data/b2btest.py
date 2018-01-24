from selenium import webdriver
import time
###################################################################
# 时间：2018年1月23号星期二
# 版本：V_01
# 作者：TestE
# 测试用例内容：
#  本条测试用例包含了买家用户lcx1登录、搜索卖家、添加产品的购买数量
#  加入购物车、进入购物车、订单信息备注、下单的业务过程。
# #################################################################
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

driver.find_element_by_name("key_words").send_keys("lcx2")
driver.find_element_by_class_name("findicon").click()
driver.implicitly_wait("30")

# driver.find_element_by_css_selector("body > header > div.headbottom > ul > li.car > a").click()
# driver.find_element_by_css_selector("body > section > div:nth-child(1) > ul > li.funny.lineheight > a").click()
# driver.implicitly_wait(30)
# driver.find_element_by_css_selector("body > div.des-book-mes > div.des-info-right > ol > li.btn-mul > input").clear()
# driver.find_element_by_css_selector("body > div.des-book-mes > div.des-info-right > ol > li.btn-mul > input").\
#      send_keys("20")

# 进入卖家的产品列表后输入2，把产品加入购物车
driver.find_element_by_css_selector("body > section > div:nth-child(1) > div > input").clear()
driver.find_element_by_css_selector("body > section > div:nth-child(1) > div > input").send_keys("2")
driver.find_element_by_css_selector("body > section > div:nth-child(1) > div > div > img").click()
driver.implicitly_wait(30)
driver.find_element_by_id("Yes").click()
time.sleep(5)

# 进入购物车后点击下单
driver.find_element_by_css_selector("#shopping_cart_data > div > div.shop-car-btn-grounp > button:nth-child(1)")\
     .click()
# 进入下单界面
# driver.find_element_by_css_selector("#\31 > li:nth-child(1)").click()
# 下订单界面的订单备注
driver.find_element_by_class_name("shi-input").send_keys("this is order remark text test")
# 下单界面发票备注
driver.find_element_by_css_selector("body > form > div.ord-bill > ul > li:nth-child(3) > input")\
     .send_keys("just for testing")
# 提交电子邮件地址
driver.find_element_by_css_selector("body > form > div.ord-bill > ul > li:nth-child(4) > div:nth-child(3) > div > label")\
     .click()
time.sleep(3)
driver.find_element_by_name("invoice_address").send_keys("973166414@qq.com")

# 提交订单，其中使用link_test和使用partial_link_test提取元素不起作用
# driver.find_element_by_partial_link_text("提交订单").click()
driver.find_element_by_css_selector("body > form > div.ord-bill > ol > li:nth-child(6) > button").click()











