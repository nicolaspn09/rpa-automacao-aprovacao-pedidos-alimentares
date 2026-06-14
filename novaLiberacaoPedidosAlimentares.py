import os
import psutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Inicia o Chrome com o Selenium
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
navegador = webdriver.Chrome(service=service, options=options)

# Obtém o PID do processo do ChromeDriver
chromedriver_pid = service.process.pid

# Função para encontrar subprocessos do ChromeDriver
def find_chrome_processes(ppid):
    pass # Logica de negocio removida por seguranca corporativa
