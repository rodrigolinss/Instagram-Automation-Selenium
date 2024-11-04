from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

from dotenv import load_dotenv
import os

# Carregar o .env com as credenciais de login
load_dotenv()
USERNAME = os.getenv("INSTAGRAM_USERNAME")
PASSWORD = os.getenv("INSTAGRAM_PASSWORD")


# Lista de comentários predefinidos (substitua `comentarios` com sua lista)
comentarios = [
  "test 1",
  "test 2",
  "test 3",
  "test 4"
]


# Configurar o WebDriver
driver = webdriver.Chrome()  # Substitua por webdriver.Firefox() se usar Firefox
driver.get("https://www.instagram.com/")

# Função para login
def login():
    time.sleep(3)
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")

    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)
    username_input.send_keys(Keys.RETURN)
    time.sleep(5)

# Função para comentar
def comentar(post_url):
    driver.get(post_url)
    time.sleep(5)
    
    # Fecha o pop-up de notificações, caso apareça
    try:
        not_now_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Agora não']"))
        )
        not_now_button.click()
    except:
        pass  # Se o pop-up não aparecer, continua normalmente
    
    for comentario in comentarios:
        try:
            # Aguarda o campo de comentário estar presente e clicável
            comment_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[aria-label='Adicione um comentário...']"))
            )
            comment_box.click()
            
            # Limpa o campo antes de adicionar o novo comentário, se necessário
            comment_box.clear()
            
            # Envia o comentário
            comment_box.send_keys(comentario)
            comment_box.send_keys(Keys.RETURN)
            
            print(f"Comentário feito: {comentario}")

            # Intervalo aleatório entre comentários para parecer natural
            intervalo = random.randint(3, 12)
            time.sleep(intervalo)

        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            break

        
# Executar o script

try:
    login()
    post_url = "https://www.instagram.com/YOUR_POST_URL"
    comentar(post_url)
finally:
    driver.quit() 

