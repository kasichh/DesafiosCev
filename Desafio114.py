import urllib.request


def tente_site(nome_site, site):
    try:
        tentativa = urllib.request.urlopen(site).getcode()
        return f'site {nome_site} válido'
    except:
        return f'site {nome_site} inacessivel'


print(tente_site('pudim', 'www.pudim.com.br'))
