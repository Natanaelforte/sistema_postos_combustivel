import requests
from bs4 import BeautifulSoup


def fazer_requisicao(method, url, payload, headers):
    return requests.request(method, url, headers=headers, data=payload)


def get_co_no_uasg(texto):
    soup = BeautifulSoup(texto, 'html.parser')

    tag = soup.find('table', class_='tex3b')

    if not tag:
        raise Exception("tag select 'co_no_uasg' não foi encontrado.")

    pre_co_no_uasg = tag.find('option').text.strip()
    co_no_uasg = f'{pre_co_no_uasg.split("-")[0].strip()}{pre_co_no_uasg.split("-")[1].strip()}'
    return co_no_uasg


def get_itens(texto):
    soup = BeautifulSoup(texto, 'html.parser')

    tag = soup.find('form', {'id': 'form1'})

    if not tag:
        raise Exception("tag form não foi encontrada.")
    all_options = []

    options = tag.find('select', class_='texField').find_all('option')

    if options:
        for option in options:
            text = option.get_text().strip()
            item = f'{text.split("-")[0].strip()}{text.split("-")[1].strip()}'
            all_options.append(item)

    return all_options


def get_dict_licitacao(texto):
    soup = BeautifulSoup(texto, 'html.parser')

    tags = soup.find('form', {"id": "form1"})

    if not tags:
        raise Exception("tag form não foi encontrado.")

    tags_tr = tags.find_all('tr')[:4]

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


def acessar_pagina_comprasnet(uasg):
    url = 'http://comprasnet.gov.br/livre/Resultado/conrelit01.asp'

    data_payload = {

        'co_uasg': f'{uasg}'

    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'
                  ',application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '43',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'comprasnet.gov.br',
        'Origin': 'http://comprasnet.gov.br',
        'Referer': 'http://comprasnet.gov.br/livre/Resultado/conrelit00.asp',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 '
                      'Safari/537.36',
        'Cookie': 'ASPSESSIONIDASCACSRB=AJNOMEEBPPEIIEPNNDNFFFOL; ASPSESSIONIDQQABAQSC=FPADNEEBNFNAGJCPCGMOAAMF; '
                  'ASPSESSIONIDCQCACRRD=AFHKDFEBJCCNDCLCMJLCOCDF; ASPSESSIONIDQQBACRTB=ELKDDFEBKCJLLCMKMHIIPMOG; '
                  'ASPSESSIONIDCQCBBRRA=CCHLGNOBDKKDGOHIONNLBBNJ; ASPSESSIONIDAARCATRD=EHGCAOOBPPGJFDMDKBPEOEML; '
                  'ASPSESSIONIDQQADBSQB=OAADMNOBBGGJBLKNGEFENHGE; ASPSESSIONIDCCTACQQD=AGDBCOOBJJNBPPNHHCDFPICE; '
                  'ASPSESSIONIDCQCBBTQD=OJGOOOOBIOAFOGNCPPJMLHCD; ASPSESSIONIDSADCBTTD=FBOGFGJCIGJPNGEEKKPMAHHB; '
                  'ASPSESSIONIDSSABCQTD=MEFEEGJCMPFJFCFBIMLFDHCC; ASPSESSIONIDSCBBASSD=HKKKNGJCKBHEKAKEGDJDNDNH; '
                  'ASPSESSIONIDASCCBRRA=EIIGOODDONDOPLGKACNOKFGL; ASPSESSIONIDCSACASTB=KBFKBPDDDBHKCJKDFNMKHFJD; '
                  'ASPSESSIONIDCCTCARQB=MEOKHPDDCHIDDMHLNMHKPHNK; ASPSESSIONIDSSCCASTD=NPCJNPDDEMEMPGIAEFHGMODJ; '
                  'ASPSESSIONIDCATTBSRD=OOKMCJDBLIJCLDEHCIBJPFMH; ASPSESSIONIDACBCQRRC=BPFPFJDBECPBEFBGBMILBPME; '
                  'ASPSESSIONIDQACCQRRB=LDBKMJDBBIFBHNJECEFKIOOC; ASPSESSIONIDCATTDRRA=FOOLGJDBPJDOGMDPJAHHPNLB'
    }

    response = fazer_requisicao(method='post', url=url, headers=headers, payload=data_payload)

    return response.text


def acessar_pagina_licitacao(co_no_uasg, data_numero):
    url = 'http://comprasnet.gov.br/livre/Resultado/conrelit03.asp'

    data_payload = {
        'co_no_uasg': f'{co_no_uasg}',
        'co_mod': '05 - Pregão',
        'nu_aviso': f'{data_numero:09}'
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'
                  ',application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '118',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'comprasnet.gov.br',
        'Origin': 'http://comprasnet.gov.br',
        'Referer': 'http://comprasnet.gov.br/livre/Resultado/conrelit02.asp',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 '
                      'Safari/537.36',
        'Cookie': 'ASPSESSIONIDASCACSRB=AJNOMEEBPPEIIEPNNDNFFFOL; ASPSESSIONIDQQABAQSC=FPADNEEBNFNAGJCPCGMOAAMF; '
                  'ASPSESSIONIDCQCACRRD=AFHKDFEBJCCNDCLCMJLCOCDF; ASPSESSIONIDQQBACRTB=ELKDDFEBKCJLLCMKMHIIPMOG; '
                  'ASPSESSIONIDCQCBBRRA=CCHLGNOBDKKDGOHIONNLBBNJ; ASPSESSIONIDAARCATRD=EHGCAOOBPPGJFDMDKBPEOEML; '
                  'ASPSESSIONIDQQADBSQB=OAADMNOBBGGJBLKNGEFENHGE; ASPSESSIONIDCCTACQQD=AGDBCOOBJJNBPPNHHCDFPICE; '
                  'ASPSESSIONIDCQCBBTQD=OJGOOOOBIOAFOGNCPPJMLHCD; ASPSESSIONIDSADCBTTD=FBOGFGJCIGJPNGEEKKPMAHHB; '
                  'ASPSESSIONIDSSABCQTD=MEFEEGJCMPFJFCFBIMLFDHCC; ASPSESSIONIDSCBBASSD=HKKKNGJCKBHEKAKEGDJDNDNH; '
                  'ASPSESSIONIDASCCBRRA=EIIGOODDONDOPLGKACNOKFGL; ASPSESSIONIDCSACASTB=KBFKBPDDDBHKCJKDFNMKHFJD; '
                  'ASPSESSIONIDCCTCARQB=MEOKHPDDCHIDDMHLNMHKPHNK; ASPSESSIONIDSSCCASTD=NPCJNPDDEMEMPGIAEFHGMODJ; '
                  'ASPSESSIONIDCATTBSRD=OOKMCJDBLIJCLDEHCIBJPFMH; ASPSESSIONIDACBCQRRC=BPFPFJDBECPBEFBGBMILBPME; '
                  'ASPSESSIONIDQACCQRRB=LDBKMJDBBIFBHNJECEFKIOOC; ASPSESSIONIDCATTDRRA=FOOLGJDBPJDOGMDPJAHHPNLB'
    }

    response = fazer_requisicao(method='post', url=url, headers=headers, payload=data_payload)

    return response


def acessar_pagina_resultado_licitacao():
    url_post = f'http://comprasnet.gov.br/livre/Resultado/conrelit07.asp?Pagina=3'
    url_get = f'http://comprasnet.gov.br/livre/Resultado/conrelit08.asp?Pagina=3'

    data_payload = {
        'itens': 'Itens'
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'
                  ',application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Length': '11',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'comprasnet.gov.br',
        'Origin': 'http://comprasnet.gov.br',
        'Referer': 'http://comprasnet.gov.br/livre/Resultado/conrelit03.asp',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 '
                      'Safari/537.36',
        'Cookie': 'ASPSESSIONIDASCACSRB=AJNOMEEBPPEIIEPNNDNFFFOL; ASPSESSIONIDQQABAQSC=FPADNEEBNFNAGJCPCGMOAAMF; '
                  'ASPSESSIONIDCQCACRRD=AFHKDFEBJCCNDCLCMJLCOCDF; ASPSESSIONIDQQBACRTB=ELKDDFEBKCJLLCMKMHIIPMOG; '
                  'ASPSESSIONIDCQCBBRRA=CCHLGNOBDKKDGOHIONNLBBNJ; ASPSESSIONIDAARCATRD=EHGCAOOBPPGJFDMDKBPEOEML; '
                  'ASPSESSIONIDQQADBSQB=OAADMNOBBGGJBLKNGEFENHGE; ASPSESSIONIDCCTACQQD=AGDBCOOBJJNBPPNHHCDFPICE; '
                  'ASPSESSIONIDCQCBBTQD=OJGOOOOBIOAFOGNCPPJMLHCD; ASPSESSIONIDSADCBTTD=FBOGFGJCIGJPNGEEKKPMAHHB; '
                  'ASPSESSIONIDSSABCQTD=MEFEEGJCMPFJFCFBIMLFDHCC; ASPSESSIONIDSCBBASSD=HKKKNGJCKBHEKAKEGDJDNDNH; '
                  'ASPSESSIONIDASCCBRRA=EIIGOODDONDOPLGKACNOKFGL; ASPSESSIONIDCSACASTB=KBFKBPDDDBHKCJKDFNMKHFJD; '
                  'ASPSESSIONIDCCTCARQB=MEOKHPDDCHIDDMHLNMHKPHNK; ASPSESSIONIDSSCCASTD=NPCJNPDDEMEMPGIAEFHGMODJ; '
                  'ASPSESSIONIDCATTBSRD=OOKMCJDBLIJCLDEHCIBJPFMH; ASPSESSIONIDACBCQRRC=BPFPFJDBECPBEFBGBMILBPME; '
                  'ASPSESSIONIDQACCQRRB=LDBKMJDBBIFBHNJECEFKIOOC; ASPSESSIONIDCATTDRRA=FOOLGJDBPJDOGMDPJAHHPNLB; '
                  'ASPSESSIONIDCQDSDQTC=BAHNJJDBGFJHKGBDEECICEDL'
    }

    try:
        fazer_requisicao(method="POST", url=url_post, payload=data_payload, headers=headers)
    except:
        pass

    headers.pop('Content-Length')

    # retorno com o texto da pagina
    response = fazer_requisicao(method='GET', url=url_get, headers=headers, payload='')

    return response.text


def acessar_pagina_itens():
    pass


def acessar_pagina_detalhes_item(nu_no_item, data_numero, co_no_uasg):
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
        fazer_requisicao(method="POST", url=url, payload=data_payload, headers=headers)
    except:
        pass

    url = 'http://comprasnet.gov.br/livre/Resultado/conrelit10.asp?Pagina=3'

    response = fazer_requisicao(method="GET", url=url, payload=data_payload, headers=headers)

    return response


def iniciar_raspagem_de_dados_comprasnet(uasg, data_numero):


    texto_pegar_co_no_uas = acessar_pagina_comprasnet(uasg)

    co_no_uasg = get_co_no_uasg(texto_pegar_co_no_uas)

    acessar_pagina_licitacao(co_no_uasg=co_no_uasg, data_numero=data_numero)

    texto_pegar_itens_data = acessar_pagina_resultado_licitacao()

    dict_certame = get_dict_licitacao(texto_pegar_itens_data)

    itens = get_itens(texto_pegar_itens_data)

    for item in itens:
        item_dict = acessar_pagina_detalhes_item(nu_no_item=item, data_numero=data_numero, co_no_uasg=co_no_uasg)

        soup_item = BeautifulSoup(item_dict.text, 'html.parser')
        dict_item = get_dict_item(soup_item)

        dict_certame['itens'].append(dict_item)

    print(dict_certame)
    return dict_certame




















def coletar_dados_licitacao(uasg, data_numero):

    # urls utilizadas nos requests

    url3 = f'http://comprasnet.gov.br/livre/Resultado/conrelit07.asp?Pagina=3'
    url4 = f'http://comprasnet.gov.br/livre/Resultado/conrelit08.asp?Pagina=3'
    url5 = 'http://comprasnet.gov.br/livre/Resultado/conrelit09.asp'
    url6 = 'http://comprasnet.gov.br/livre/Resultado/conrelit10.asp?Pagina=3'

    # entrando na pagina para setar modalidade e numero da data


    # retorno com o texto da pagina


    # pegando o texto do response


    # pegando o co_no_uasg para ultilizar nos proximos passos


    # entrando na pagina para setar modalidade e numero da data




    print(co_no_uasg)