
import requests

from unicodedata import normalize

from bs4 import BeautifulSoup


class ColetarDadosComprasNet:
    session = requests.session()

    def fazer_requisicao(self, method, url, payload=None, headers=None):
        if method.upper() == 'POST':
            response = self.session.post(url, headers=headers, data=payload)
        else:
            response = self.session.get(url, headers=headers, data=payload)

        return response

    def get_co_no_uasg(self, texto):
        soup = BeautifulSoup(texto, 'html.parser')

        tag = soup.find('table', class_='tex3b')

        if not tag:
            raise Exception("tag select 'co_no_uasg' não foi encontrado.")

        pre_co_no_uasg = tag.find('option').text.strip()
        co_no_uasg = f'{pre_co_no_uasg.split("-")[0].strip()}{pre_co_no_uasg.split("-")[1].strip()}'
        return co_no_uasg

    def get_itens(self, texto):
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

    def get_dict_licitacao(self, texto):
        soup = BeautifulSoup(texto, 'html.parser')

        tags = soup.find('form', {"id": "form1"})

        if not tags:
            raise Exception("tag form não foi encontrado.")

        tags_tr = tags.find_all('tr')[:4]

        text_orgao = tags_tr[0].find('td', class_='tex3').get_text().strip()
        text_uasg = tags_tr[1].find('td', class_='tex3').get_text().strip()
        text_modalidade = tags_tr[2].find('td', class_='tex3').get_text().strip()
        text_numero = tags_tr[3].find('td', class_='tex3').get_text().strip()
        text_modalidade_normalise = normalize('NFKD', text_modalidade).encode('ASCII','ignore').decode('ASCII')
        return {
            'licitacao': {
                'modalidade': {
                    "codigo": text_modalidade.split('-')[0].strip().lower(),
                    "descricao": text_modalidade_normalise.split('-')[1].strip().lower()
                },
                'numero': text_numero.lower()
            },
            'orgao': {
                'codigo': text_orgao.split('-')[0].strip().lower(),
                'descricao': text_orgao.split('-')[1].strip().lower(),
            },
            'uasg': {
                'codigo': text_uasg.split('-')[0].strip().lower(),
                'descricao': text_uasg.split('-')[1].strip().lower(),
            },
            'itens': []
        }

    def get_dict_item(self, soup_item):
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

            "situacao": text_situacao.lower(),
            "fornecedor": {
                "identificador": text_cpf_cnpj.replace('.','').replace('/','').replace('-','').lower(),
                "nome": text_nome.lower()
            },
            "sequencial": int(text_sequencial),
            "material": {
                "codigo": text_codigo_material.lower(),
                "descricao": text_desc_material.lower(),
                "especificacao": text_desc_det_material.strip().lower()
            },
            "quantidade": float(text_quantidade),
            "marca": text_marca.lower(),
            "unidade": text_unidade.lower(),
            "preco_unitario": float(text_preco_unidade.replace('.', '').replace(',', '.')),
            "valor_total": float(text_valor_total.replace('.', '').replace(',', '.'))

        }
        return dict_item

    def acessar_pagina_comprasnet(self, uasg):
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
        }

        response = self.fazer_requisicao(method='post', url=url, headers=headers, payload=data_payload)
        return response

    def acessar_pagina_licitacao(self, co_no_uasg, data_numero):
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
                          'Safari/537.36'
        }

        self.fazer_requisicao(method='post', url=url, headers=headers, payload=data_payload)

    def _try_fazer_requisicao(self, url_post, url_get, data_payload, headers_post, headers_get):
        try:
            self.fazer_requisicao(method="POST", url=url_post, payload=data_payload, headers=headers_post)
        except:
            pass

        response = self.fazer_requisicao(method='GET', url=url_get, payload=data_payload, headers=headers_get)
        return response

    def acessar_pagina_resultado_licitacao(self):
        url_post = f'http://comprasnet.gov.br/livre/Resultado/conrelit07.asp?Pagina=3'
        url_get = f'http://comprasnet.gov.br/livre/Resultado/conrelit08.asp?Pagina=3'
        url_post4 = f'http://comprasnet.gov.br/livre/Resultado/conrelit07.asp?Pagina=4'
        url_get4 = f'http://comprasnet.gov.br/livre/Resultado/conrelit08.asp?Pagina=4'

        data_payload = {
            'itens': 'Itens'
        }

        headers_post = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
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
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
        }

        headers_get = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'keep-alive',
            'Host': 'comprasnet.gov.br',
            'Referer': 'http://comprasnet.gov.br/livre/Resultado/conrelit03.asp',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        }

        response = self._try_fazer_requisicao(url_post, url_get, data_payload, headers_post, headers_get)

        if response.status_code == int(500):

            response = self._try_fazer_requisicao(url_post4, url_get4, data_payload, headers_post, headers_get)

        return response.text

    def acessar_pagina_detalhes_item(self, nu_no_item, data_numero, co_no_uasg):
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
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
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
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        }

        try:
            self.fazer_requisicao(method="POST", url=url, headers=headers, payload=data_payload)
        except:
            pass

        url = 'http://comprasnet.gov.br/livre/Resultado/conrelit10.asp?Pagina=3'

        response = self.fazer_requisicao(method="GET", url=url, headers=headers, payload=data_payload)

        return response

    def iniciar_raspagem_de_dados_comprasnet(self, uasg, data_numero):
        response = self.acessar_pagina_comprasnet(uasg)

        texto_pegar_co_no_uas = response.text

        co_no_uasg = self.get_co_no_uasg(texto_pegar_co_no_uas)

        self.acessar_pagina_licitacao(co_no_uasg=co_no_uasg, data_numero=data_numero)

        texto_pegar_itens_data = self.acessar_pagina_resultado_licitacao()

        dict_certame = self.get_dict_licitacao(texto_pegar_itens_data)

        itens = self.get_itens(texto_pegar_itens_data)

        for item in itens:
            try:
                item_dict = self.acessar_pagina_detalhes_item(
                    nu_no_item=item, data_numero=data_numero, co_no_uasg=co_no_uasg
                )

                soup_item = BeautifulSoup(item_dict.text, 'html.parser')
                dict_item = self.get_dict_item(soup_item)

                dict_certame['itens'].append(dict_item)
            except:
                print(f'Não coletou os dados do {item}')

        print(dict_certame)

        return dict_certame
