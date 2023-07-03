import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup


def get_payload(method, url, payload, headers):
    return requests.request(method, url, headers=headers, data=payload)


def get_dict_licitacao(soup):
    tags_tr = soup.find('form', {"id": "form1"}).find_all('tr')[:4]

    text_orgao = tags_tr[0].find('td', class_='tex3').get_text().strip()
    text_uasg = tags_tr[1].find('td', class_='tex3').get_text().strip()
    text_modalidade = tags_tr[2].find('td', class_='tex3').get_text().strip()
    text_numero = tags_tr[3].find('td', class_='tex3').get_text().strip()
    return {
        'licitacao': {
            'modalidade': {
                "codigo": text_modalidade.split('-')[0].strip(),
                "descricao": text_modalidade.split('-')[1].strip()
            },
            'numero': text_numero
        },
        'orgao': {
            'codigo': text_orgao.split('-')[0].strip(),
            'descricao': text_orgao.split('-')[1].strip(),
        },
        'uasg': {
            'codigo': text_uasg.split('-')[0].strip(),
            'descricao': text_uasg.split('-')[1].strip(),
        },
        'itens': []
    }

def get_dict_item(soup_item):
    # criando o html da pagina requisitada
    soup = soup_item

    # criando variaveis de string vazias
    text_situacao = ''
    text_cpf_cnpj = ''
    text_nome = ''
    text_sequencial = ''
    text_codigo_material = ''
    text_desc_material = ''
    text_quantidade = ''
    text_marca = ''
    text_unidade = ''
    text_preco_unidade = ''
    text_valor_total = ''
    text_desc_det_material = ''

    # raspando os dados da pagina
    elements_trs = soup.find('form', {"id": "form1"}).find('table', class_='tex3').find_all('tr')
    for element_tr in elements_trs:
        elements_tds = element_tr.find_all('td')
        for td in elements_tds:
            if 'Situação:' in td.text:
                text_situacao = td.find_all('span')[-1].text.strip()
                if not text_situacao:
                    text_situacao = ''
            elif 'CNPJ/CPF:' in td.text:
                text_cpf_cnpj = td.find_all('span')[-1].text.strip()
                if not text_cpf_cnpj:
                    text_cpf_cnpj = ''
            elif 'Razão Social/Nome:' in td.text:
                text_nome = td.find_all('span')[-1].text.strip()
                if not text_nome:
                    text_nome = ''
            elif 'Item da Licitação:' in td.text:
                text_sequencial = td.find_all('span')[-1].text.strip()
                if not text_sequencial:
                    text_sequencial = ''
            elif 'Cod. do' in td.text:
                text_codigo_material = td.find_all('span')[-1].text.strip()
                if not text_codigo_material:
                    text_codigo_material = ''
            elif 'Identificação' in td.text:
                text_desc_material = td.find_all('span')[-1].text.strip()
                if not text_desc_material:
                    text_desc_material = ''
            elif 'Quantidade:' in td.text:
                text_quantidade = td.find_all('span')[-1].text.strip()
                if not text_quantidade:
                    text_quantidade = ''
            elif 'Marca:' in td.text:
                text_marca = td.find_all('span')[-1].text.strip()
                if not text_marca:
                    text_marca = ''
            elif 'Unidade:' in td.text:
                text_unidade = td.find_all('span')[-1].text.strip()
                if not text_unidade:
                    text_unidade = ''
            elif 'Preço Unitário:' in td.text:
                text_preco_unidade = td.find_all('span')[-1].text.strip()
                if not text_preco_unidade:
                    text_preco_unidade = ''
            elif 'Valor Total:' in td.text:
                text_valor_total = td.find_all('span')[-1].text.strip()
                if not text_valor_total:
                    text_valor_total = ''
            elif 'Descrição Detalhada' in td.text:
                text_desc_det_material = td.find_all('span')[-1].text
                if not text_desc_det_material:
                    text_desc_det_material = ''

    # setando os dados raspados no valor do dicionario
    dict_item = {

        "situacao": text_situacao,
        "fornecedor": {
            "identificador": text_cpf_cnpj.replace('.','').replace('/','').replace('-',''),
            "nome": text_nome
        },
        "sequencial": int(text_sequencial),
        "material": {
            "codigo": text_codigo_material,
            "descricao": text_desc_material,
            "especificacao": text_desc_det_material.strip()
        },
        "quantidade": float(text_quantidade),
        "marca": text_marca,
        "unidade": text_unidade,
        "preco_unitario": float(text_preco_unidade.replace('.', '').replace(',', '.')),
        "valor_total": float(text_valor_total.replace('.', '').replace(',', '.'))

    }
    return dict_item

def coletar_dados_licitacao(uasg, data_numero):
    # setando o cromedrive para o driver rodar sem abrir o navegador
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
    campo_co_uasg.send_keys(f'{uasg}')

    botao_ok = driver.find_element(by=By.NAME, value="ok")
    botao_ok.click()

    campo_modalidade = Select(driver.find_element(by=By.NAME, value="co_mod"))
    campo_modalidade.select_by_visible_text('05 - Pregão')

    campo_numero = driver.find_element(by=By.NAME, value="nu_aviso")
    campo_numero.clear()
    campo_numero.send_keys(f'{data_numero}')

    botao_ok2 = driver.find_element(by=By.NAME, value="ok2")
    botao_ok2.click()

    # apertar botão item e ir para outra pagina
    botao_item = driver.find_element(by=By.NAME, value="itens")
    botao_item.click()
    driver.implicitly_wait(0.7)

    # pegando o sorce da pagina e criando o html com o beautiful soap
    page_item = driver.page_source
    soup = BeautifulSoup(page_item, 'html.parser')

    # gerando o dicionario do certame
    dict_certame = get_dict_licitacao(soup)

    tags_tr = soup.find('form', {"id": "form1"}).find_all('tr')[:4]
    text_orgao = tags_tr[0].find('td', class_='tex3').get_text().strip()
    co_no_uasg = f"{text_orgao.split('-')[0].strip()}{text_orgao.split('-')[1].strip()}"

    # selecionando o campo com selenium
    campo_item = Select(driver.find_element(by=By.NAME, value="nu_no_item"))

    # lista de text options
    options_text = []

    # alimentar lista com o campo_item.options
    for option in  campo_item.options:
        text = option.text
        options_text.append(text)

    for option_text in options_text:
        # acessando a pagina de item com response
        nu_no_item = option_text.split('-')

        url = 'http://comprasnet.gov.br/livre/Resultado/conrelit09.asp'

        data_payload = {
            'nu_no_item': nu_no_item,
            'co_mod': '05 - Pregão',
            'nu_aviso': f"{data_numero:09}",
            'co_no_uasg': co_no_uasg,
            'pagina': '3',
            'ok': 'OK'
        }

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'
                      ',application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Length': '234',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'comprasnet.gov.br',
            'Origin': 'http://comprasnet.gov.br',
            'Referer': 'http://comprasnet.gov.br/livre/Resultado/conrelit08.asp?Pagina=3',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 '
                          'Safari/537.36',
            'Cookie': 'ASPSESSIONIDASCACSRB=AJNOMEEBPPEIIEPNNDNFFFOL; ASPSESSIONIDQQABAQSC=FPADNEEBNFNAGJCPCGMOAAMF;'
                      ' ASPSESSIONIDCQCACRRD=AFHKDFEBJCCNDCLCMJLCOCDF; ASPSESSIONIDQQBACRTB=ELKDDFEBKCJLLCMKMHIIPMOG; '
                      'ASPSESSIONIDCQCBBRRA=CCHLGNOBDKKDGOHIONNLBBNJ; ASPSESSIONIDAARCATRD=EHGCAOOBPPGJFDMDKBPEOEML; '
                      'ASPSESSIONIDQQADBSQB=OAADMNOBBGGJBLKNGEFENHGE; ASPSESSIONIDCCTACQQD=AGDBCOOBJJNBPPNHHCDFPICE; '
                      'ASPSESSIONIDCQCBBTQD=OJGOOOOBIOAFOGNCPPJMLHCD; ASPSESSIONIDSADCBTTD=FBOGFGJCIGJPNGEEKKPMAHHB; '
                      'ASPSESSIONIDSSABCQTD=MEFEEGJCMPFJFCFBIMLFDHCC; ASPSESSIONIDSCBBASSD=HKKKNGJCKBHEKAKEGDJDNDNH; '
                      'ASPSESSIONIDASCCBRRA=EIIGOODDONDOPLGKACNOKFGL; ASPSESSIONIDCSACASTB=KBFKBPDDDBHKCJKDFNMKHFJD; '
                      'ASPSESSIONIDCCTCARQB=MEOKHPDDCHIDDMHLNMHKPHNK; ASPSESSIONIDSSCCASTD=NPCJNPDDEMEMPGIAEFHGMODJ; '
                      'ASPSESSIONIDCATTBSRD=OOKMCJDBLIJCLDEHCIBJPFMH; ASPSESSIONIDACBCQRRC=BPFPFJDBECPBEFBGBMILBPME; '
                      'ASPSESSIONIDQACCQRRB=LDBKMJDBBIFBHNJECEFKIOOC'
        }

        try:
            get_payload(method="POST", url=url, payload=data_payload, headers=headers)
        except:
            pass

        url = 'http://comprasnet.gov.br/livre/Resultado/conrelit10.asp?Pagina=3'

        response = get_payload(method="GET", url=url, payload=data_payload, headers=headers)

        # transformando o texto do response em html com o  BeautifulSoup
        soup_item = BeautifulSoup(response.text, 'html.parser')

        # coletar dados do item e criando o dicionario dos itens
        dict_item = get_dict_item(soup_item)

        # com o dicionario criado, adicionar o dicionario do item na lista
        dict_certame['itens'].append(dict_item)

    print(dict_certame)
    return dict_certame