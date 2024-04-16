import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()

driver = webdriver.Chrome()

# ORIGIN AND DESTINATION
driver.maximize_window()
driver.get('https://almex.com.mx/')
mouse = ActionChains(driver)
mouse.move_to_element(driver.find_element(By.XPATH, "//a[normalize-space()='Envíos']")).perform()
link2 = driver.find_element(By.XPATH, "//a[normalize-space()='Cotiza tu Envío']")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(link2)).click()
link2.click()


#handles parma moverme a otra pestaña
window_handles = driver.window_handles
driver.switch_to.window(window_handles[1])

barra2 = driver.find_element(By.XPATH, "//a[normalize-space()='Registro']")
barra2.click()

time.sleep(5)
barra4 = driver.find_element(By.XPATH, "//input[@id='cuenta']")
barra4.send_keys('LQuintero')
time.sleep(5)
barra5 = driver.find_element(By.XPATH, "//input[@id='password']")
barra5.send_keys('LQuintero')
time.sleep(3)

driver.execute_script('window.scrollTo(0,200)')
time.sleep(2)
link3 = driver.find_element(By.XPATH, "//select[@id='cmbTipoDePersona']")
link3.click()
select = Select(driver.find_element(By.XPATH, "//select[@id='cmbTipoDePersona']"))
#mouse.move_to_element(driver.find_element(By.XPATH, "//select[@id='cmbTipoDePersona']")).perform()
time.sleep(3)
#select.select_by_value('2')
select.select_by_visible_text('MORAL')
time.sleep(2)
barra6 = driver.find_element(By.ID, "rfc")
barra6.send_keys('GAMD970427DQ9')
time.sleep(15)

#btn = driver.find_element(By.XPATH, "//span[normalize-space()='Nueva Cotización']")
#btn.click()
#time.sleep(5)

# Cerrar el navegador al finalizar
driver.quit()