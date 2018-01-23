from selenium import webdriver
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

driver.find_element_by_class_name("goCart").click()
