from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from bs4 import BeautifulSoup

import time


def coletar_dados_selenium():

    driver = webdriver.Chrome()
    driver.get('http://comprasnet.gov.br/livre/Resultado/conrelit00.asp')

    driver.implicitly_wait(0.5)

    campo_co_uasg = driver.find_element(by=By.NAME, value="co_uasg")
    campo_co_uasg.clear()
    campo_co_uasg.send_keys('943001')

    botao_ok = driver.find_element(by=By.NAME, value="ok")
    botao_ok.click()


    campo_modalidade = Select(driver.find_element(by=By.NAME, value="co_mod"))
    campo_modalidade.select_by_visible_text('05 - Pregão')

    campo_numero = driver.find_element(by=By.NAME, value="nu_aviso")
    campo_numero.clear()
    campo_numero.send_keys('1102023')

    botao_ok2 = driver.find_element(by=By.NAME, value="ok2")
    botao_ok2.click()

    botao_item = driver.find_element(by=By.NAME, value="itens")
    botao_item.click()

    campo_item = Select(driver.find_element(by=By.NAME, value="nu_no_item"))
    # coletar todas as opções e fazer um for para entrar em cada item e coletar as informações.
    # o codigo daqui pra frente é dentro do for.

    print(campo_item.options)

    campo_item.select_by_visible_text('00062 - MACARRÃO')

    # botao_ok3 = driver.find_element(by=By.NAME, value="ok")
    # botao_ok3.click()

    # valor = driver.find_element(By.CSS_SELECTOR, "tr:nth-child(10) > td:nth-child(1) > .mensagem")

    # valor_unitario = valor.text

    # print(valor_unitario)
    # return valor_unitario
    # page_source = botao_ok3
    #
    # soup = BeautifulSoup(page_source, 'lxml')
    # info_itens = []
    #
    #
    #
    # elements_tds = soup.find_all('td', attrs={'colspan': '2'})
    #
    # for element_td in elements_tds
    #     pri

def gat_info_itens(option,campo_item,driver):

    campo_item.select_by_visible_text(f'{option}')

    botao_ok3 = driver.find_element(by=By.NAME, value="ok")
    botao_ok3.click()

    page_source = botao_ok3

    soup = BeautifulSoup(page_source, 'lxml')
    info_iten = {}

    elements_tds = soup.find_all('td', attrs={'colspan': '2'})
    for element_td in elements_tds:
        encontrar_chave = element_td.find('span', class_='tex3b')
        encontrar_valor = element_td.find('span', class_='tex3')
        if encontrar_valor is None:
            encontrar_valor = element_td.find('span', class_='mensagem')
        chave = encontrar_chave.get_text()
        valor = encontrar_valor.get_text()

        info_iten[f'{chave}'] = f'{valor}'

    botao_ok3 = driver.find_element(by=By.NAME, value="voltar")
    botao_ok3.click()

    return info_iten