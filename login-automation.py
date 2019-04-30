from selenium import webdriver

USERNAME = 'Vishnu'
PASSWORD = 'password'

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://vishnu.com/wordpress/wp-login.php')

user_input = driver.find_element_by_id('user_login')
user_input.send_keys(USERNAME)

password_input = driver.find_element_by_id('user_pass')
password_input.send_keys(PASSWORD)

login_button = driver.find_element_by_id('wp-submit')
login_button.click()
