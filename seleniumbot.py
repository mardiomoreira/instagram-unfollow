from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.options import Options as Firefox_Options
import time
import getpass
from tkinter import messagebox
from random import randint
link = "https://www.instagram.com/"

arquivo = open('lista.txt', "r")
usuario = input("Digite o usuario do instagram ")
senha = getpass.getpass("Senha ")
class BotInstagram():
    def __init__(self):
        ## Navegador Chome
        # self.driver = webdriver.Chrome('/home/mardio/PYTHON/intagram/chromedriver')
        # self.ser = Service("/home/mardio/PYTHON/intagram/chromedriver")
        # self.op = webdriver.ChromeOptions()
        # self.driver = webdriver.Chrome(service=self.ser, options=self.op)
        
        ## Navegador Firefox Developer
        self.new_driver_path = '/home/mardio/PYTHON/intagram/geckodriver'
        self.new_binary_path = '/opt/firefox-developer/firefox'

        self.ops = options()
        self.ops.binary_location = self.new_binary_path
        self.serv = Service(self.new_driver_path)
        self.driver = webdriver.Firefox(service=self.serv, options=self.ops)
    def entrar_inst(self):
        time.sleep(randint(3,7))
        self.username_input = self.driver.find_element(By.XPATH,"/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
        self.password_input = self.driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
        
        self.username_input.send_keys(usuario)
        self.password_input.send_keys(senha)
        
        self.login_button = self.driver.find_element(By.XPATH,"//button[@type='submit']")
        self.login_button.click()
        
    def entrar_link(self, link):
        self.driver.get(link)
    def dar_like(self):
        self.driver.find_element(By.CSS_SELECTOR,".glyphsSpriteFriend_Follow").click()
    def deixar_de_seguir(self):
        self.driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div/div[3]/button[1]').click()
    def fechar(self):
        self.driver.close()
try:
    pass
    bot = BotInstagram()
    bot.entrar_link('https://www.instagram.com')
    print("--------- Abrindo o Perfil ----------")
    time.sleep(randint(4, 10))
    bot.entrar_inst()
    unfollow = 1
    for linha in arquivo:
        deslike=link+linha
        print(deslike)
        time.sleep(randint(1,10))
        bot.entrar_link(deslike)
        time.sleep(randint(2, 5))
        print("--------------------- Clicando pra unfollow ----------------------")
        bot.dar_like()
        
        time.sleep(randint(1, 5))
        bot.deixar_de_seguir()
        time.sleep(randint(2, 6))
        print("")
        print("")
        print("#####################################################")
        print("#########       QTD. de Unflow: ", unfollow,"          ########")
        print("#####################################################")
        print("")
        unfollow +=1

    messagebox.showwarning("Completo", "Script chegou ao fim!!!")
except Exception as e:
    raise e


