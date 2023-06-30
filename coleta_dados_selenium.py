import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup


def get_dict_item(page_item):
    soup = BeautifulSoup(page_item, 'html.parser')

    text_situacao = None
    text_cpf_cnpj = None
    text_nome = None
    text_sequencial = None
    text_codigo_material = None
    text_desc_material = None
    text_quantidade = None
    text_marca = None
    text_unidade = None
    text_preco_unidade = None
    text_valor_total = None


    elements_trs = soup.find('form', {"id": "form1"}).find('table', class_='tex3').find_all('tr')
    for element_tr in elements_trs:
        elements_tds = element_tr.find_all('td')
        for td in elements_tds:
            if 'Situação:' in td.text:
                text_situacao = td.find_all('span')[-1].text.strip()
            elif 'CNPJ/CPF:' in td.text:
                text_cpf_cnpj = td.find_all('span')[-1].text.strip()
            elif 'Razão Social/Nome:' in td.text:
                text_nome = td.find_all('span')[-1].text.strip()
            elif 'Item da Licitação:' in td.text:
                text_sequencial = td.find_all('span')[-1].text.strip()
            elif 'Cod. do' in td.text:
                text_codigo_material = td.find_all('span')[-1].text.strip()
            elif 'Identificação' in td.text:
                text_desc_material = td.find_all('span')[-1].text.strip()
            elif 'Quantidade:' in td.text:
                text_quantidade = td.find_all('span')[-1].text.strip()
            elif 'Marca:' in td.text:
                text_marca = td.find_all('span')[-1].text.strip()
            elif 'Unidade:' in td.text:
                text_unidade = td.find_all('span')[-1].text.strip()
            elif 'Preço Unitário:' in td.text:
                text_preco_unidade = td.find_all('span')[-1].text.strip()
            elif 'Valor Total:' in td.text:
                text_valor_total = td.find_all('span')[-1].text.strip()

    dict_item = {

        "situacao": text_situacao,
        "fornecedor": {
            "identificador": text_cpf_cnpj,
            "nome": text_nome
        },
        "sequencial": int(text_sequencial),
        "material": {
            "codigo": text_codigo_material,
            "descricao": text_desc_material,
        },
        "quantidade": float(text_quantidade),
        "marca": text_marca,
        "unidade": text_unidade,
        "preco_unitario": float(text_preco_unidade.replace(',', '.')),
        "valor_total": float(text_valor_total.replace('.', '').replace(',', '.'))

    }
    return dict_item


def get_dict_licitacao(soup):
    tags_tr = soup.find('form', {"id": "form1"}).find_all('tr')[:4]

    text_orgao = tags_tr[0].find('td', class_='tex3').get_text().strip()
    text_uasg = tags_tr[1].find('td', class_='tex3').get_text().strip()
    text_modalidade = tags_tr[2].find('td', class_='tex3').get_text().strip()
    text_numero = tags_tr[3].find('td', class_='tex3').get_text().strip()
    return {
        'licitacao': {
            'modalidade': {
                "codigo": text_modalidade.split('-')[0],
                "descricao": text_modalidade.split('-')[1]
            },
            'numero': text_numero
        },
        'orgao': {
            'codigo': text_orgao.split('-')[0],
            'descricao': text_orgao.split('-')[1],
        },
        'uasg': {
            'codigo': text_uasg.split('-')[0],
            'descricao': text_uasg.split('-')[1],
        },
        'itens': []
    }


def coletar_dados_licitacao(uasg, data_numero):

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # acessar pagina no compranet.
    driver = webdriver.Chrome(chrome_options)
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
