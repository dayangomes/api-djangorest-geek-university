import requests

# GET Avaliações
avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# Acessando o código de status HTTP
print(avaliacoes.status_code)

# Acessando os dados da resposta
print(avaliacoes.json())
print(type(avaliacoes.json()))

# Acessando a quantidade de registros
print(avaliacoes.json()['count'])

# Acessando a próxima página de resultados
print(avaliacoes.json()['next'])

# Acessando os resultados dessa página
print(avaliacoes.json()['results'])
print(type(avaliacoes.json()['results']))

# Acessando o primeiro elemento da lista de resultados
print(avaliacoes.json()['results'][0])

# Acessando o último elemento da lista de resultados
print(avaliacoes.json()['results'][-1])

# Acessando o nome da pessoa que fez a última avaliação
print(avaliacoes.json()['results'][-1]['nome'])

# GET Avaliação
avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/1/')
print(avaliacao.json())

# GET Cursos

headers = {
    'Authorization': 'Token 7afcdc31bf7910ec3172b4dfa1c5789a0cb11d5b'
}

cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)

print(cursos.status_code)
print(cursos.json())

