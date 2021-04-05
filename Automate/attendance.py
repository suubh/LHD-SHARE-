from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://nitap.co.in/moodle/')

# FOR LOGIN
log_in = driver.find_element_by_link_text('Log in')
log_in.click()
username = driver.find_element_by_xpath('//*[@id="username"]')
username.send_keys('admin')
pwd = driver.find_element_by_xpath('//*[@id="password"]')
pwd.send_keys('admin')
log_in_btn = driver.find_element_by_id('loginbtn')
log_in_btn.click()

# FOR SUBJECT
disaster = driver.find_element_by_class_name('(//*[@class="aalink coursename mr-2"])[4]')
disaster.click()
