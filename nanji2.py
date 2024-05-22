from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

url = 'https://yeyak.seoul.go.kr/web/loginForm.do'
driver.get(url)

# 로그인 페이지에서 로그인 버튼 클릭
login_xpath = '//a[@href="/web/loginForm.do"]'
driver.find_element(By.XPATH, login_xpath).click()

#id password 입력창
id_xpath = '//input[@id="userid"]'
userid = '0'
driver.find_element("xpath",id_xpath).send_keys(userid)

pass_xpath = '//input[@id="userpwd"]'
userpass = '0'
driver.find_element("xpath",pass_xpath).send_keys(userpass + Keys.ENTER)

# 특정 예약 페이지로 이동
driver.get('www.')

# 팝업창 종료
popup_xpath = '//div[@class="btn_box"]'
driver.find_element(By.XPATH, popup_xpath).click()

# 예약일자 선택
day_xpath = '//td[@class id="00/00/00"]'
driver.find_element(By.XPATH, day_xpath).click()

# 예약버튼 클릭
click_xpath = '//a[@class="common_btn blue"]'
driver.find_element(By.XPATH, click_xpath).click()

# 체크박스 선택 (클래스 이름에 오타 수정)
total_xpath = '//span[@class="chk_each"]'
driver.find_element(By.XPATH, total_xpath).click()

# 최종 예약 버튼 클릭 (이전에 오타가 있었습니다)
ul_xpath = '//ul[@class="book_btn_box"]/li/button'
driver.find_element(By.XPATH, ul_xpath).click()

# 매크로 실행 버튼 클릭
macro_xpath = '//div[@class="html_element"]'
driver.find_element(By.XPATH, macro_xpath).click()
