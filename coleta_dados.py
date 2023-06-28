# import requests
#
#
# def get_payload(url, payload, headers):
#     return requests.request("POST", url, headers=headers, data=payload)
#
# def _try_get_uasg_full(text, codigo):
#     initial_index = text.index(codigo)
#     final_index = text.index(f'{codigo} -') -21
#
#     return text[initial_index:final_index]
#
# def _try_get_numero_item(text, codigo):
#     initial_index = text.index(f'000{codigo}')
#     final_index = text.index(f'000{codigo} -')
#
#     return text[initial_index:final_index]
#
#
# url1 = 'http://comprasnet.gov.br/livre/Resultado/conrelit01.asp'
# url2 = 'http://comprasnet.gov.br/livre/Resultado/conrelit03.asp'
# url4 = 'http://comprasnet.gov.br/livre/Resultado/conrelit09.asp'
#
# fist_uargs = {'co_uasg': '943001'}
#
# # Abaixo, estou pegando os payloads uasg_full, modalidade e numero para passar na segunda pagina e chegar na licitação.
#
# headers1 = {
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Cookie': 'ASPSESSIONIDASDCBTRA=GINMMEEBHFIENPHHIHOEBBKD'
# }
#
# response = get_payload(url=url1, headers=headers1, payload=fist_uargs)
#
# text_large = response.text
#
# uasg = _try_get_uasg_full(text_large, '943001')
#
# # uasg_full = f'co_no_uasg={uasg}'
# # modalidade = 'co_mod=05 - Pregão'
# # numero = 'nu_aviso=001102023'
# data_payload = {
#     'co_no_uasg': uasg,
#     'co_mod': '05 - Pregão',
#     'nu_aviso': '001102023'
# }
#
# # Abaixo, usarei os pyload uasg_full, modalidade e numero para acessar a pagina do pregão eletronico.
#
#
# headers2 = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'Accept-Encoding': 'gzip, deflate',
#     'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
#     'Cache-Control': 'max-age=0',
#     'Connection': 'keep-alive',
#     'Content-Length': '11',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Cookie': 'ASPSESSIONIDASCACSRB=AJNOMEEBPPEIIEPNNDNFFFOL; ASPSESSIONIDQQABAQSC=FPADNEEBNFNAGJCPCGMOAAMF; ASPSESSIONIDCQCACRRD=AFHKDFEBJCCNDCLCMJLCOCDF; ASPSESSIONIDQQBACRTB=ELKDDFEBKCJLLCMKMHIIPMOG',
#     'Host': 'comprasnet.gov.br',
#     'Origin': 'http://comprasnet.gov.br',
#     'Referer': 'http://comprasnet.gov.br/livre/Resultado/conrelit03.asp',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
# }
#
# response2 = get_payload(url=url2, headers=headers2, payload=data_payload)
#
# text_large2 = response2.text
#
# headers2.update({
#     'Cookie': response2.headers.get('Set-cookie'),
#     'Content-Type': response2.headers.get('Content-Type')
# })
#
#
# # data_payload2 = {
# #     'itens': 'Itens',
# # }
#
# data_payload2 = {'itens': 'Itens'}
#
# def _try_get_pagina(url, pagina=0):
#     response_inicial = get_payload(url % 3, headers=headers2, payload=data_payload2)
#
#     if response_inicial.status_code == int(500):
#         pagina += 1
#
#         return _try_get_pagina(url, pagina)
#
#     return response_inicial
#
# url3 = f'http://comprasnet.gov.br/livre/Resultado/conrelit07.asp?Pagina=%s'
#
# # text_large_response = _try_get_pagina(url3)
# # text_large3 = text_large_response.text
#
# # numero_item = _try_get_numero_item(text_large3, '62')
#
# # print(numero_item)

# response_inicial = requests.request(
#     "POST",
#     'http://comprasnet.gov.br/livre/Resultado/conrelit07.asp?Pagina=3',
#     headers={
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'Accept-Encoding': 'gzip, deflate',
#         'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
#         'Cache-Control': 'max-age=0',
#         'Connection': 'keep-alive',
#         'Content-Length': '11',
#         'Content-Type': 'application/x-www-form-urlencoded',
#         'Cookie': 'ASPSESSIONIDASCACSRB=AJNOMEEBPPEIIEPNNDNFFFOL; ASPSESSIONIDQQABAQSC=FPADNEEBNFNAGJCPCGMOAAMF; ASPSESSIONIDCQCACRRD=AFHKDFEBJCCNDCLCMJLCOCDF; ASPSESSIONIDQQBACRTB=ELKDDFEBKCJLLCMKMHIIPMOG',
#         'Host': 'comprasnet.gov.br',
#         'Origin': 'http://comprasnet.gov.br',
#         'Referer': 'http://comprasnet.gov.br/livre/Resultado/conrelit03.asp',
#         'Upgrade-Insecure-Requests': '1',
#         'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
#     },
#     data={'itens': 'Itens'}
# )
#
# print(response_inicial.text)








import requests

url = "http://comprasnet.gov.br/livre/Resultado/conrelit07.asp?Pagina=3"

payload='itens=Itens'
headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Encoding': 'gzip, deflate',
  'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
  'Cache-Control': 'max-age=0',
  'Connection': 'keep-alive',
  'Content-Length': '11',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'ASPSESSIONIDASCACSRB=AJNOMEEBPPEIIEPNNDNFFFOL; ASPSESSIONIDQQABAQSC=FPADNEEBNFNAGJCPCGMOAAMF; ASPSESSIONIDCQCACRRD=AFHKDFEBJCCNDCLCMJLCOCDF; ASPSESSIONIDQQBACRTB=ELKDDFEBKCJLLCMKMHIIPMOG; ASPSESSIONIDCQCBBRRA=CCHLGNOBDKKDGOHIONNLBBNJ; ASPSESSIONIDCQCBBRRA=PMFLGNOBNEHANIMCNMKCLPFD',
  'Host': 'comprasnet.gov.br',
  'Origin': 'http://comprasnet.gov.br',
  'Referer': 'http://comprasnet.gov.br/livre/Resultado/conrelit03.asp',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)






