from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.common.keys import Keys
#Create your tests here
class MusicPlayer(LiveServerTestCase):
    def testform(self):
        selenium=webdriver.Chrome()
        
        selenium.get('http:127.0.0.1:8000/authentication/login/')

        username=selenium.find_element('id','username')
        psswd=selenium.find_element('id','psswd')

        submit = selenium.find_element('id','submit')

        username.send_keys("athul@gmail.com")
        psswd.send_keys("cherukattu")
        submit.send_keys(Keys.RETURN) 

        assert 'athul' in selenium.page_source  
