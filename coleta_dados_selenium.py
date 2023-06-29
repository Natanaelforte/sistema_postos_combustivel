import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from bs4 import BeautifulSoup


def get_dict_item(page_item):
    soup = BeautifulSoup(page_item, 'html.parser')
    dict_item = {}

    elements_trs = soup.find('form', {"id": "form1"}).find('table', class_='tex3').find_all('tr')
    for element_tr in elements_trs:
        elements_tds = element_tr.find_all('td')
        for td in elements_tds:
            if 'Modalidade' in td.text:
                dict_item.update({'modalidade': td.find_all('span')[-1].text.strip()})
                # if not td.find('span', class_='tex3'):
                #     dict_item.update({'modalidade': td.find('span', class_='mensagem').text.strip()})
            elif 'Número da Licitação:' in td.text:
                dict_item.update({'numero_licitacao': td.find_all('span')[-1].text.strip()})
            elif 'Situação:' in td.text:
                dict_item.update({'situacao': td.find_all('span')[-1].text.strip()})
            elif 'CNPJ/CPF:' in td.text:
                dict_item.update({'cpf_cnpj': td.find_all('span')[-1].text.strip()})
            elif 'Razão Social/Nome:' in td.text:
                dict_item.update({'razao_social_nome': td.find_all('span')[-1].text.strip()})
            elif 'Item da Licitação:' in td.text:
                dict_item.update({'item_licitacao': td.find_all('span')[-1].text.strip()})
            elif 'Cod. do' in td.text:
                dict_item.update({'cod_do_conjunto_material': td.find_all('span')[-1].text.strip()})
            elif 'Identificação' in td.text:
                dict_item.update({'identificacao_conjunto_material': td.find_all('span')[-1].text.strip()})
            elif 'Descrição Detalhada do' in td.text:
                dict_item.update({'descricao_detalhada-material': td.find_all('span')[-1].text.strip()})
            elif 'Quantidade:' in td.text:
                dict_item.update({'quantidade': td.find_all('span')[-1].text.strip()})
            elif 'Marca:' in td.text:
                dict_item.update({'marca': td.find_all('span')[-1].text.strip()})
            elif 'Unidade:' in td.text:
                dict_item.update({'unidade': td.find_all('span')[-1].text.strip()})
            elif 'Preço Unitário:' in td.text:
                dict_item.update({'preco_unitario': td.find_all('span')[-1].text.strip()})
            elif 'Valor Total:' in td.text:
                dict_item.update({'valor_total': td.find_all('span')[-1].text.strip()})


    return dict_item

def get_dict_licitacao(soup):
    tags_tr = soup.find('form', {"id": "form1"}).find_all('tr')[:3]
    return {
        'orgao': tags_tr[0].find('td', class_='tex3').get_text().strip(),
        'uasg': tags_tr[1].find('td', class_='tex3').get_text().strip(),
        'itens': []
    }


def coletar_dados_licitacao(uasg, data_numero):

    # acessar pagina no compranet.
    driver = webdriver.Chrome()
    driver.get('http://comprasnet.gov.br/livre/Resultado/conrelit00.asp')
    driver.implicitly_wait(0.5)

    # setar dados do certame na pagina comprasnet
    campo_co_uasg = driver.find_element(by=By.NAME, value="co_uasg")
    campo_co_uasg.clear()
    campo_co_uasg.send_keys(f'{uasg}') #943001

    botao_ok = driver.find_element(by=By.NAME, value="ok")
    botao_ok.click()

    campo_modalidade = Select(driver.find_element(by=By.NAME, value="co_mod"))
    campo_modalidade.select_by_visible_text('05 - Pregão')

    campo_numero = driver.find_element(by=By.NAME, value="nu_aviso")
    campo_numero.clear()
    campo_numero.send_keys(f'{data_numero}') #1102023

    botao_ok2 = driver.find_element(by=By.NAME, value="ok2")
    botao_ok2.click()


    # apertar botão item e ir para outra pagina
    botao_item = driver.find_element(by=By.NAME, value="itens")
    botao_item.click()
    driver.implicitly_wait(0.7)

    page_item = driver.page_source
    soup = BeautifulSoup(page_item, 'html.parser')


    dict_certame = get_dict_licitacao(soup)

    campo_item = Select(driver.find_element(by=By.NAME, value="nu_no_item"))


    # lista de text options
    options_text = []

    # alimentar lista com o campo_item.options
    for option in  campo_item.options:
        text = option.text
        options_text.append(text)


    for option_text in options_text:
        # acessar pagina item
        campo_item = Select(driver.find_element(by=By.NAME, value="nu_no_item"))
        campo_item.select_by_visible_text(option_text)

        botao_ok3 = driver.find_element(by=By.NAME, value="ok")
        botao_ok3.click()

        page_item2 = driver.page_source

        # coletar dados, criar dicionario
        dict_item = get_dict_item(page_item2)

        # com o dicionario criado, adicionar o dicionario do item na lista
        dict_certame['itens'].append(dict_item)

        # voltar para pagina de seleção dos itens
        time.sleep(2)
        driver.execute_script("window.history.go(-1)")


    print(dict_certame)
    return dict_certame
