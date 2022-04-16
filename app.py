from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import os

# inisalisasi nim dan password untuk login
nim ="Input Nim In Here"
password = "Input Password In Here"

project_dir = os.path.dirname(os.path.abspath(__file__))

# disini penginstalan webdriver chrome secara otomatis dengan web driver manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
# kita masukan url yang akan di eksekusi dan secara otomatis akan terbuka
# chrome yang menuju ke url tersebut
driver.get("https://syncnau.poltektegal.ac.id/login")

# untuk menemukan keys atau kunci dari halaman tersbut menggunakan find element
# find_element(By.NAME,"value") disini selenium akan mencari element by name mana yang isinya seperti value yang di inputkan
# find_element(By.ID,"value") disini selenium akan mencari element by id mana yang isinya seperti value yang di inputkan
# send_key() berguna untuk mengisi atau replace isi dari inputan
# click() adalah sebuah action
driver.find_element(By.NAME,"username").send_keys(nim)
driver.find_element(By.ID,"password").send_keys(password)
driver.find_element(By.ID,"submit").click()
try:
    # disini akan membuat handle menggunakan try
    # jika find_element(By.CLASS_NAME,"callout") itu ada sistem akan mencetak hasil dari find_element tersebut
    print(driver.find_element(By.CLASS_NAME,"callout").text)
    sleep(5)
    # dan sistem akan berhenti karena ada method quit
    quit()
except NoSuchElementException:
    # dan di except jika find element tersebut tidak ada di sini saya cetak login success
    # dan sistem akan dberjalan lagi
    print("Login Success")

driver.get("https://syncnau.poltektegal.ac.id/profil")
driver.find_element(By.NAME,"user_foto").send_keys(os.path.join(project_dir, "profile.png"))
sleep(3)
driver.find_element(By.NAME,"simpan_foto").click()

try:
    print(driver.find_element(By.CLASS_NAME,"noty_body").text)
    sleep(5)
except NoSuchElementException:
    print("Terjadi Kesalahan")

