import os
import re
import sys
import time
import psutil
import shutil
import locale
import smtplib
import datetime
import zipfile
import requests
import cx_Oracle
import subprocess
import mysql.connector
from datetime import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from logExecucaoCodigos import grava_log_execucao_sql

import sys

sys.path.append(r"C:\rpa\Python")

from Classes.Firefox.Firefox.conectaFirefox import FirefoxSeleniumManager


def get_firefox_version(directory, executable_name):
    pass # Logica de negocio removida por seguranca corporativa



def rename_firefox_executable():
    pass # Logica de negocio removida por seguranca corporativa



def get_latest_geckodriver_url():
    pass # Logica de negocio removida por seguranca corporativa

def download_geckodriver():
    pass # Logica de negocio removida por seguranca corporativa

def diretorio_json():
    pass # Logica de negocio removida por seguranca corporativa

def obtem_status():
    pass # Logica de negocio removida por seguranca corporativa

def handle_exception(bloco_codigo, e):
    pass # Logica de negocio removida por seguranca corporativa

def envia_email(mensagemEmail, destinatarios_email, assunto_email):
    pass # Logica de negocio removida por seguranca corporativa

def grava_log(mensagem_log):
    pass # Logica de negocio removida por seguranca corporativa

def solicita_margem_minima():
    pass # Logica de negocio removida por seguranca corporativa

def solicita_contratos():
    pass # Logica de negocio removida por seguranca corporativa

def solicita_laboratorios():
    pass # Logica de negocio removida por seguranca corporativa

def solicita_produtos():
    pass # Logica de negocio removida por seguranca corporativa

def solicita_clientes():
    pass # Logica de negocio removida por seguranca corporativa

def conecta_oracle(query):
    pass # Logica de negocio removida por seguranca corporativa

def consulta_desconto_laboratorio(laboratorio, tabela_laboratorios):
    pass # Logica de negocio removida por seguranca corporativa

def consulta_desconto_item(codigo_produto, uf_cliente):
    pass # Logica de negocio removida por seguranca corporativa

def seleciona_verba_tela(navegador, chrome_pids, linha, verba_laboratorio="0"):
    pass # Logica de negocio removida por seguranca corporativa

def confirma_pedido(navegador, chrome_pids, liberar_pedido=False):
    pass # Logica de negocio removida por seguranca corporativa

def aplicar_negociacao(navegador, chrome_pids):
    pass # Logica de negocio removida por seguranca corporativa

def confirma_margem_passa_pedido(navegador, chrome_pids, margem_canal, liberar_pedido=False):
    pass # Logica de negocio removida por seguranca corporativa

def verifica_lista_contrato(codigo_cliente_pedido):
    pass # Logica de negocio removida por seguranca corporativa

def retira_recursos_valida_margem(navegador, chrome_pids, margem_canal):
    pass # Logica de negocio removida por seguranca corporativa

def rejeita_itens_valida_margem(navegador, chrome_pids, margem_canal):
    pass # Logica de negocio removida por seguranca corporativa

def cancelar_pedido(navegador, chrome_pids):
    pass # Logica de negocio removida por seguranca corporativa

def conecta_oracle(sql):
    pass # Logica de negocio removida por seguranca corporativa

def margem_dia_query():
    pass # Logica de negocio removida por seguranca corporativa

def valida_margem_verba_utilizada(navegador, chrome_pids, margem_minima_pedido, valor_desconto_maximo, margem_tolerancia):
    pass # Logica de negocio removida por seguranca corporativa

def rejeita_itens(navegador, chrome_pids, linha_laboratorio, url):
    pass # Logica de negocio removida por seguranca corporativa

def aceita_itens(navegador, chrome_pids, linha_laboratorio, url):
    pass # Logica de negocio removida por seguranca corporativa

def retira_recursos(navegador, chrome_pids, linha_laboratorio, url):
    pass # Logica de negocio removida por seguranca corporativa

def valida_recursos_descontos_laboratorios(navegador, chrome_pids, linha_laboratorio, margem_canal, valor_desconto_maximo, margem_tolerancia, url, url_retirar):
    pass # Logica de negocio removida por seguranca corporativa

def valida_recursos_retira_itens_descontos_laboratorios(navegador, chrome_pids, linha_laboratorio, margem_canal, valor_desconto_maximo, margem_tolerancia, url):
    pass # Logica de negocio removida por seguranca corporativa

def valida_margem_verba_utilizada_industria(navegador, chrome_pids, margem_canal, margem_tolerancia, colecao_laboratorio, tabela_laboratorios):
    pass # Logica de negocio removida por seguranca corporativa

def valida_margem_retira_itens_verba_utilizada_industria(navegador, chrome_pids, margem_canal, margem_tolerancia, colecao_laboratorio, tabela_laboratorios):
    pass # Logica de negocio removida por seguranca corporativa

def conecta_my_sql(banco_dados, sql):
    pass # Logica de negocio removida por seguranca corporativa

def conecta_my_sql_insert(banco_dados, sql):
    pass # Logica de negocio removida por seguranca corporativa

def valida_cliente_pedido(codigo_cliente, tabela):
    pass # Logica de negocio removida por seguranca corporativa

def find_chrome_processes(ppid):
    pass # Logica de negocio removida por seguranca corporativa

def kill_firefox():
    pass # Logica de negocio removida por seguranca corporativa

def kill_process(pid):
    pass # Logica de negocio removida por seguranca corporativa

def acessa_navegador():
    pass # Logica de negocio removida por seguranca corporativa

def loga_sistema_intranet():
    pass # Logica de negocio removida por seguranca corporativa

def consulta_liberacao_pedidos_alimentar():
    pass # Logica de negocio removida por seguranca corporativa



def deslogar_sistema_intranet(navegador):
    pass # Logica de negocio removida por seguranca corporativa

def navega_tabela_pedidos_gerais():
    pass # Logica de negocio removida por seguranca corporativa

def processa_itens(navegador, chrome_pids, margem_informada, tabela_laboratorios):
    pass # Logica de negocio removida por seguranca corporativa

def executa_codigo_principal():
    pass # Logica de negocio removida por seguranca corporativa

if __name__ == "__main__":
    executa_codigo_principal()