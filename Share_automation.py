from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time
import random
from dotenv import load_dotenv
import os

contador_total = 0

# Carregar o .env com as credenciais de login
load_dotenv()
USERNAME = os.getenv("INSTAGRAM_USERNAME")
PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

# Configuração do WebDriver
driver = webdriver.Chrome()  # Ajuste se estiver usando Safari ou outro navegador
driver.get("https://www.instagram.com/")

# Função para login
def login():
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD, Keys.RETURN)
    time.sleep(5)

from selenium.common.exceptions import TimeoutException


# Função para compartilhar um post com contatos
def compartilhar():
    global contador_total 

    try:
        # Tenta localizar o botão de compartilhar usando a classe
        share_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x3nfvp2 x1q0g3np x87ps6o x1lku1pv x1a2a7pz x1mywscw x1y1aw1k x1sxyh0 xwib8y2 xurb0ha') and @role='button']"))
        )
        share_button.click()
        time.sleep(2)
        print("Botão de compartilhar clicado com sucesso.")

    except TimeoutException:
        print("Erro: O botão de compartilhar não foi encontrado.")
        return

    # Seleciona os 15 primeiros contatos, se o botão de compartilhar foi encontrado
    try:
        contatos = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x3nfvp2 x1q0g3np x87ps6o x1lku1pv x1a2a7pz x1lcm9me x1yr5g0i xrt01vj x10y3i5r xl56j7k x1y1aw1k x1sxyh0 xwib8y2 xurb0ha') and @role='button']"))
        )[:15]
        
        contador_atual = 0

        for contato in contatos:
            try:
                contato.click()
                contador_atual += 1
                print("Selecionado um contato para compartilhamento")
                time.sleep(0.5)
            except Exception as e:
                print(f"Erro ao selecionar contato: {e}")
                break

        contador_total += contador_atual

        # Clica no botão de envio para compartilhar
        enviar_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,  "//div[contains(@class, 'x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w x972fbf xcfux6l x1qhh985 xm0m39n xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x9bdzbf x1ypdohk x1f6kntn xwhw2v2 x10w6t97 xl56j7k x17ydfre x1swvt13 x1pi30zi x1n2onr6 x2b8uid xlyipyv x87ps6o xcdnw81 x1i0vuye xh8yej3 x1tu34mt xzloghq x3nfvp2') and @role='button']"))
        )
        enviar_button.click()
        print(f"Post compartilhado com {contador_atual} contatos! Total compartilhado até agora: {contador_total}")

    except TimeoutException:
        print("Erro: Não foi possível selecionar os contatos ou clicar no botão de envio.")

# Executar o script
try:
    login()
    post_url = "https://www.instagram.com/YOUR_POST_ID
    driver.get(post_url)
    time.sleep(3)
    
    while True:  # Loop infinito
        compartilhar()
        time.sleep(5)  # Espera 5 segundos antes de compartilhar novamente

except KeyboardInterrupt:
    print("Processo interrompido pelo usuário.")
finally:
    driver.quit()
