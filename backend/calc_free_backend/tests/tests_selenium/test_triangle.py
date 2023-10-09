import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TriangleSeleniumTestsCases(unittest.TestCase):

    def setUp(self):
        "Initializing selenium driver, going to page, maximizing window and setting break time"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://calcfree.azurewebsites.net")
        self.time_sleep = 2.0
    
    def tearDown(self):
        "Quiting selenium"
        self.driver.quit()
    
    def test_page(self):
        "Test checks if all of page functions works"
        page = self.driver.find_element(By.ID, "triangleCalculations")
        page.click()
        time.sleep(self.time_sleep)
        popover = self.driver.find_elements(By.ID, "popover-body")
        self.assertEqual(len(popover), 0, msg = "Popover should not be open")
        popover_button = self.driver.find_element(By.ID, "popoverButton")
        popover_button.click()
        time.sleep(self.time_sleep)
        popover = self.driver.find_element(By.ID, "popover-body")
        popover.click()
        time.sleep(self.time_sleep)
        popover = self.driver.find_elements(By.ID, "popover-body")
        self.assertEqual(len(popover), 0, msg = "Popover should not be open")
        a = self.driver.find_element(By.ID, "a")
        b = self.driver.find_element(By.ID, "b")
        c = self.driver.find_element(By.ID, "c")
        sin_l = self.driver.find_element(By.ID, "sinL")
        cos_l = self.driver.find_element(By.ID, "cosL")
        tg_l = self.driver.find_element(By.ID, "tgL")
        ctg_l = self.driver.find_element(By.ID, "ctgL")
        sin_b = self.driver.find_element(By.ID, "sinB")
        cos_b = self.driver.find_element(By.ID, "cosB")
        tg_b = self.driver.find_element(By.ID, "tgB")
        ctg_b = self.driver.find_element(By.ID, "ctgB")
        a_value = a.get_attribute("value")
        b_value = b.get_attribute("value")
        c_value = c.get_attribute("value")
        sin_l_value = sin_l.get_attribute("value")
        cos_l_value = cos_l.get_attribute("value")
        tg_l_value = tg_l.get_attribute("value")
        ctg_l_value = ctg_l.get_attribute("value")
        sin_b_value = sin_b.get_attribute("value")
        cos_b_value = cos_b.get_attribute("value")
        tg_b_value = tg_b.get_attribute("value")
        ctg_b_value = ctg_b.get_attribute("value")
        self.assertEqual(len(a_value), 0, "a should be empty on start")
        self.assertEqual(len(b_value), 0, "b should be empty on start")
        self.assertEqual(len(c_value), 0, "c should be empty on start")
        self.assertEqual(len(sin_l_value), 0, "Sin(L) should be empty on start")
        self.assertEqual(len(cos_l_value), 0, "Cos(L) should be empty on start")
        self.assertEqual(len(tg_l_value), 0, "Tg(L) should be empty on start")
        self.assertEqual(len(ctg_l_value), 0, "Ctg(L) should be empty on start")
        self.assertEqual(len(sin_b_value), 0, "Sin(B) should be empty on start")
        self.assertEqual(len(cos_b_value), 0, "Cos(B) should be empty on start")
        self.assertEqual(len(tg_b_value), 0, "Tg(B) should be empty on start")
        self.assertEqual(len(ctg_b_value), 0, "Ctg(B) should be empty on start")
        a.send_keys("3,0")
        time.sleep(self.time_sleep)
        b.send_keys("4,0")
        time.sleep(self.time_sleep)
        c.send_keys("5,0")
        time.sleep(self.time_sleep)
        hint = self.driver.find_elements(By.ID, "hint")
        self.assertTrue(len(hint) == 0, msg = "Hint text area should not be on the page")   
        solve_button = self.driver.find_element(By.ID, "solve")
        solve_button.click()
        time.sleep(self.time_sleep)
        hint_button = self.driver.find_element(By.ID, "hintButton")
        hint_button.click()
        time.sleep(self.time_sleep)
        hint = self.driver.find_element(By.ID, "hint")
        hint_text = hint.text
        self.assertTrue(len(hint_text) > 0, msg = "Hint text should appear")
        self.assertEqual(sin_l.get_attribute("value"), "0,8", msg = "Sin(L) should be correct")
        self.assertEqual(cos_l.get_attribute("value"), "0,6", msg = "Cos(L) should be correct")
        self.assertEqual(tg_l.get_attribute("value"), "1,3333333333333333", msg = "Tg(L) should be correct")
        self.assertEqual(ctg_l.get_attribute("value"), "0,75", msg = "Ctg(L) should be correct")
        self.assertEqual(sin_b.get_attribute("value"), "0,6", msg = "Sin(B) should be correct")
        self.assertEqual(cos_b.get_attribute("value"), "0,8", msg = "Cos(B) should be correct")
        self.assertEqual(tg_b.get_attribute("value"), "0,75", msg = "Tg(B) should be correct")
        self.assertEqual(ctg_b.get_attribute("value"), "1,3333333333333333", msg = "Ctg(B) should be correct")
        c.send_keys(u'\ue009' + u'\ue003')
        c.send_keys("6,0")
        time.sleep(self.time_sleep)
        solve_button.click()
        time.sleep(self.time_sleep)
        c_helper = self.driver.find_element(By.ID, "c-helper-text")
        self.assertTrue(len(c_helper.text) > 0, msg = "Error should appear")
        sin_l_value = sin_l.get_attribute("value")
        cos_l_value = cos_l.get_attribute("value")
        tg_l_value = tg_l.get_attribute("value")
        ctg_l_value = ctg_l.get_attribute("value")
        sin_b_value = sin_b.get_attribute("value")
        cos_b_value = cos_b.get_attribute("value")
        tg_b_value = tg_b.get_attribute("value")
        ctg_b_value = ctg_b.get_attribute("value")
        self.assertEqual(len(sin_l_value), 0, "Sin(L) should be empty")
        self.assertEqual(len(cos_l_value), 0, "Cos(L) should be empty")
        self.assertEqual(len(tg_l_value), 0, "Tg(L) should be empty")
        self.assertEqual(len(ctg_l_value), 0, "Ctg(L) should be empty")
        self.assertEqual(len(sin_b_value), 0, "Sin(B) should be empty")
        self.assertEqual(len(cos_b_value), 0, "Cos(B) should be empty")
        self.assertEqual(len(tg_b_value), 0, "Tg(B) should be empty")
        self.assertEqual(len(ctg_b_value), 0, "Ctg(B) should be empty")
        self.assertTrue(len(hint.text) == 0, msg = "Hint text should disappear")
        c.send_keys(u'\ue009' + u'\ue003')
        solve_button.click()
        time.sleep(self.time_sleep)
        self.assertEqual(c.get_attribute("value"), "5,0", msg = "C should have correct length")
        self.assertEqual(sin_l.get_attribute("value"), "0,8", msg = "Sin(L) should be correct")
        self.assertEqual(cos_l.get_attribute("value"), "0,6", msg = "Cos(L) should be correct")
        self.assertEqual(tg_l.get_attribute("value"), "1,3333333333333333", msg = "Tg(L) should be correct")
        self.assertEqual(ctg_l.get_attribute("value"), "0,75", msg = "Ctg(L) should be correct")
        self.assertEqual(sin_b.get_attribute("value"), "0,6", msg = "Sin(B) should be correct")
        self.assertEqual(cos_b.get_attribute("value"), "0,8", msg = "Cos(B) should be correct")
        self.assertEqual(tg_b.get_attribute("value"), "0,75", msg = "Tg(B) should be correct")
        self.assertEqual(ctg_b.get_attribute("value"), "1,3333333333333333", msg = "Ctg(B) should be correct")
        self.assertTrue(len(hint.text) > 0, msg = "Hint text should appear")
        hint_button.click()
        time.sleep(self.time_sleep)
        hint = self.driver.find_elements(By.ID, "hint")
        self.assertTrue(len(hint) == 0, msg = "Hint text area should not be on the page")