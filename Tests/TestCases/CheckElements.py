# -*- coding: UTF-8 -*-
import time
from Tests.TestCases.Base import BaseTest
from Tests.Config.main import driver
from Tests.Pages import AllElements
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Action:
    def __init__(self):
        self.driver = driver

    def find(self, locator):
        try:
            WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located(locator))
            return driver.find_element(*locator)
        except NoSuchElementException:
            raise NoSuchElementException("NoSuchElementException : %s" % str(locator))
        except TimeoutException:
            raise TimeoutException("TimeoutException : %s" % str(locator))

    def click(self, locator):
        try:
            WebDriverWait(driver, timeout=10).until(EC.visibility_of_element_located(locator)).click()
        except NoSuchElementException:
            raise NoSuchElementException("NoSuchElementException : %s" % str(locator))
        except TimeoutException:
            raise TimeoutException("TimeoutException : %s" % str(locator))


AC = Action()


class Testing(BaseTest):
    # 주소접속
    def test_0001_이사로개발URL접속(self):
        driver.get(AllElements.WebIsaURL)
        driver.maximize_window()
        time.sleep(3)
        self.assertEqual(driver.current_url, "https://24ro.co.kr/www-dev/")

    # 팝업 체크
    def test_0002_랜딩팝업요소체크(self):
        AC.find((By.CSS_SELECTOR, AllElements.PopupContents))
        AC.find((By.CSS_SELECTOR, AllElements.PopupContents_Applogo))
        AC.find((By.CSS_SELECTOR, AllElements.PopupContents_SubTitle))
        AC.find((By.CSS_SELECTOR, AllElements.PopupContents_MainTitle01))
        AC.find((By.CSS_SELECTOR, AllElements.PopupContents_MainTitle02))
        AC.find((By.CSS_SELECTOR, AllElements.PopupContents_MainTitle03))
        AC.find((By.CSS_SELECTOR, AllElements.PopupContents_AppBtn))
        AC.find((By.CSS_SELECTOR, AllElements.PopupContents_CloseText))
        AC.click((By.CSS_SELECTOR, AllElements.PopupContents_CloseText))

    # 사이드 체크
    def test_0003_좌우사이드요소체크(self):
        AC.find((By.CSS_SELECTOR, AllElements.Side_QrcodeArea))
        AC.find((By.CSS_SELECTOR, AllElements.Side_Title1))
        AC.find((By.CSS_SELECTOR, AllElements.Side_Title2))
        AC.find((By.CSS_SELECTOR, AllElements.Side_SecondTitle))
        AC.find((By.CSS_SELECTOR, AllElements.Side_ChatText01))
        AC.find((By.CSS_SELECTOR, AllElements.Side_ChatText02))
        AC.find((By.CSS_SELECTOR, AllElements.Side_IconChat01))

    # 아이프레임으로 들어가기
    def test_0004_아이프레임진입(self):
        driver.switch_to.frame("myframe")

    # 메인화면_이사
    def test_0005_서비스신청_포장이사(self):
        AC.click((By.CSS_SELECTOR, AllElements.ServiceIconCar))
        AC.click((By.XPATH, "/html/body/reach-portal/div/div[2]/div[2]/div/div/div[1]/div[2]/button[1]"))
        AC.click((By.CSS_SELECTOR,
                  "body > reach-portal > div > div:nth-child(2) > div:nth-child(2) > div > div > div.css-grjgbs.et1e07b2 > button"))

    # 서비스1단계 진행
    def test_0006_서비스신청_포장이사_1단계(self):
        AC.click(
            (By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div[3]/div[5]/div[6]"))
        AC.click((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[4]/div[2]/div/div/div[1]/div/div/label/span"))
        AC.click((By.XPATH, "/html/body/div[2]/div[2]/div/div/div[1]/div/div[2]"))
        AC.click((By.XPATH, "/html/body/div[2]/div[2]/div/div/div[2]/div/div[10]"))
        AC.click((By.XPATH, "/html/body/div[2]/div[2]/button"))
        AC.click((By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/button"))

    # 서비스2단계 진행
    def test_0007_서비스신청_포장이사_2단계(self):
        AC.click((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[3]/div/div/div[1]/div[2]/div[1]/div[1]/span"))
        time.sleep(1)

    # 서비스2단계 출발지 주소 아이프레임
    def test_0008_서비스신청_2단계_출발지주소검색_아이프레임진입(self):
        iframe0 = driver.find_elements(By.TAG_NAME, 'iframe')[0]
        driver.switch_to.frame(iframe0)
        time.sleep(1)

        iframe1 = driver.find_elements(By.TAG_NAME, 'iframe')[0]
        driver.switch_to.frame(iframe1)
        time.sleep(1)

    # 서비스2단계 출발지 주소 검색
    def test_0009_서비스신청_2단계_카카오주소검색(self):
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/form/fieldset/div/div/input").send_keys("센테니아")
        AC.click((By.XPATH, "/html/body/div[1]/div/div[1]/form/fieldset/div/button[2]/span"))
        AC.click((By.XPATH, "/html/body/div[1]/div/div[2]/ul/li/dl/dd[1]/span/button/span[1]"))
        time.sleep(1)

    # 서비스2단계 출발지 아이프레임 나가기
    def test_0010_서비스신청_2단계_아이프레임나가기(self):
        driver.switch_to.parent_frame()
        driver.switch_to.parent_frame()

    # 서비스2단계 출발지완료
    def test_0011_서비스신청_2단계_출발지(self):
        AC.click((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[3]/div/div/div[1]/div[2]/div[2]/div[1]/span"))
        AC.click((By.XPATH, "/html/body/div[2]/div[2]/div/div/div[1]/div/div[4]"))
        AC.click((By.XPATH, "/html/body/div[2]/div[2]/button"))
        AC.click((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[3]/div/div/div[1]/div[2]/div[2]/div[2]/span"))
        AC.click((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[1]/div/div[5]"))
        AC.click((By.XPATH, "/html/body/div[3]/div[2]/button"))
        AC.click((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[3]/div/div/form[1]/div[1]/label"))
        AC.click((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[3]/div/div/form[2]/div[1]/label"))

    # 서비스2단계 도착지 주소 아이프레임
    def test_0012_서비스신청_2단계_도착지주소검색_아이프레임진입(self):
        AC.click((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[5]/div/div/div[1]/div[2]/div[1]/div[1]/span"))
        time.sleep(1)

        iframe0 = driver.find_elements(By.TAG_NAME, 'iframe')[0]
        driver.switch_to.frame(iframe0)
        time.sleep(1)

        iframe1 = driver.find_elements(By.TAG_NAME, 'iframe')[0]
        driver.switch_to.frame(iframe1)
        time.sleep(1)

    # 서비스2단계 도착지 주소 검색
    def test_0013_서비스신청_2단계_카카오주소검색(self):
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/form/fieldset/div/div/input").send_keys("센테니아")
        AC.click((By.XPATH, "/html/body/div[1]/div/div[1]/form/fieldset/div/button[2]/span"))
        AC.click((By.XPATH, "/html/body/div[1]/div/div[2]/ul/li/dl/dd[1]/span/button/span[1]"))
        time.sleep(1)

    # 서비스2단계 도착지 아이프레임 나가기
    def test_0014_서비스신청_2단계_아이프레임나가기(self):
        driver.switch_to.parent_frame()
        driver.switch_to.parent_frame()

    # 서비스2단계 도착지완료
    def test_0015_서비스신청_2단계_도착지(self):
        AC.click((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[5]/div/div/div[1]/div[2]/div[2]/div/span"))
        AC.click((By.XPATH, "/html/body/div[4]/div[2]/div/div/div[1]/div/div[4]"))
        AC.click((By.XPATH, "/html/body/div[4]/div[2]/button"))
        AC.click((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[5]/div/div/form[1]/div[1]/label"))
        AC.click((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[5]/div/div/form[2]/div[1]/label"))
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[7]/div/div/div/textarea").send_keys(
            "자동화테스트 진행중")
        AC.click((By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/button"))
        time.sleep(1)  # 스크롤 기능 작동위한 대기

    # 서비스3단계 사진가이드
    def test_0016_서비스신청_3단계_사진가이드(self):
        ## 팝업창 스크롤 하는 방법 필요
        # SCROLL_PAUSE_TIME = 3
        # last_height = driver.execute_script("return document.body.scrollHeight")  # Get scroll height
        #
        # while True:
        #     # Scroll down to bottom
        #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #
        #     # Wait to load page
        #     time.sleep(SCROLL_PAUSE_TIME)
        #
        #     # Calculate new scroll height and compare with last scroll height
        #     new_height = driver.execute_script("return document.body.scrollHeight")
        #     if new_height == last_height:
        #         break
        #     last_height = new_height
        # time.sleep(2)
        AC.click((By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/div/div[7]"))

    # 서비스3단계 구조선택
    def test_0017_서비스신청_3단계_구조선택(self):
        AC.click((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/div/div/label/span"))
        AC.click((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[4]/div[2]/span[3]"))
        AC.click((By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/button"))

    # 서비스3단계 사진첨부
    def test_0018_서비스신청_3단계_사진첨부(self):
        time.sleep(1)
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/div/div[1]/div/div/div/span/div/div/span/input").send_keys(
            r"C:\Users\1\Desktop\1.jpg")
        AC.click((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div/div[3]/div[3]/div"))
        driver.find_element(By.XPATH,
                            "/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div/span/div/div/span/input").send_keys(
            r"C:\Users\1\Desktop\1.jpg")
        AC.click((By.XPATH, "/html/body/div[1]/div/div[1]/div[5]/button"))

    # 서비스3단계 신청내용확인
    def test_0019_서비스신청_3단계_신청내용확인_스크롤(self):
        SCROLL_PAUSE_TIME = 3
        last_height = driver.execute_script("return document.body.scrollHeight")  # Get scroll height

        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        time.sleep(1)

    # 서비스3단계 상자+및메모
    def test_0020_서비스신청_3단계_신청내용확인_마무리(self):
        AC.click((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[7]/div[3]/div[2]/div/span[3]"))
        AC.click((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/div/textarea"))
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div/div[2]/div/div/textarea").send_keys(
            "  테스트중입니다")
        AC.click((By.XPATH, "/html/body/div[1]/div/div[1]/div[4]/button"))

    # 인증하기
    def test_0021_서비스신청_인증하기(self):
        AC.find((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[3]/input"))
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[3]/input").send_keys("안진형")
        time.sleep(1)  # 서비스 인증 딜레이에 따른 대기

        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[3]/div[1]/input").send_keys(
            "01000000008")
        time.sleep(1)

        AC.click((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[3]/div[1]/button/p"))
        time.sleep(1)

        driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[3]/div[2]/input").send_keys("1111")
        time.sleep(1)

        AC.click((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[3]/div[2]/div/button/p"))
        time.sleep(1)

        AC.click((By.XPATH, "/html/body/div[1]/div/div[1]/div[3]/div/button"))

    # 서비스 신청 접수 완료
    def test_0022_견적신청접수완료_팝업(self):
        AC.click((By.XPATH, "/html/body/div[1]/div/div[1]/div[5]/div/div/div/span[2]"))
        AC.find((By.XPATH, "/html/body/div[1]/div/div[2]/a[2]/img"))
