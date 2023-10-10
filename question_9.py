clubes_de_futebol = [
    'ibis',
    'flamengo',
    'perilima',
    'volta redonda',
    'nacional de patos',
    'internacional',
    'vasco da gama',
    'cruzeiro',
    'barça',
    'palmeiras'
]

clube_de_pesquisa = input('Digite o clube: ')


for clube in clubes_de_futebol:
    if clube != clube_de_pesquisa:
        print('Ainda não achei!')
    else:
        print('Achei')
        break
        