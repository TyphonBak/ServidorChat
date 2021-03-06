from datetime import datetime

alunos = [
    {"id": 1, "nome": "Paulo"},
    {"id": 1, "nome": "Joao"},
    {"id": 1, "nome": "lucas"},
    {"id": 1, "nome": "Paulo"},
    {"id": 1, "nome": "Paulo"}
]

data = datetime.now()
strg_data = data.strftime('%y%m%d%U%w%H%M%S')
numeros = [int(x) for x in strg_data]
sequencia = [sum(numeros[ind:ind+3]) for ind in range(0, len(numeros), 3)]
seed = int(data.strftime('%f')[:2]+data.strftime('%f')[-2:])
base = list(map(lambda num: (seed//num)//num, sequencia))
asc_letras_maisculas = list(range(65,91))
asc_letras_minusculas = list(range(97,123))
asc_numeros = list(range(48,58))
referencia = asc_letras_maisculas + asc_letras_minusculas + asc_numeros
maximo = len(referencia)

retorno = [referencia[indice if indice<maximo else indice%maximo] for indice in base]

print(retorno)
print(''.join([chr(valor) for valor in retorno]))

print(numeros)
print(base)

print(list(map(lambda num: (seed//num)//num, base)))

print(chr(97))

print('Fim')