# Projeto

Projeto desenvolvido com o intuito de criar um servidor flask simples.

## Como Funciona?
O servidor possui três rotas:

1. `/validacao/cpf`
2. `/compara/jsons`
3. `/compara/arquivos`

### 1 - /validacao/cpf

Esta rota recebe um json contendo uma string **cpf** e retorna uma mensagem dizendo se o CPF é válido.

Exemplo de entrada:

```json
{
	"cpf": "282.862.070-09"
}
```

Exemplo de saída:

```json
{
	"is_valid": true
}
```

O CPF de entrada pode ou não conter pontuações.

`"282.862.070-09"` = válido
`"28286207009"` = válido

### 2 - /compara/jsons

Esta rota recebe um json contendo N listas e retorna uma lista contendo os itens únicos.
Um item será classificado como único se ele não for encontrado em nenhuma outra lista.

Exemplo de entrada:

```json
{
	"compara": [
		["item A", "item C"],
		["item A", "item B", "item C"]
	]
}
```

Exemplo de saída:

```json
{
	"unicos": ["item B"]
}
```

Caso não haja nenhum item único, a rota retorna uma lista vazia: `"unicos": []`

## 3 - /compara/arquivos

Esta rota recebe N arquivos e retorna um arquivo contendo a lista de itens únicos.
Um item será classificado como único se ele não for encontrado em nenhum outro arquivo.

Exemplos de entrada:

```
item A
item C
```

```
item A
item B
item C
```

Exemplo de saída:

```
item B
```

Caso não haja nenhum item único, a rota retorna um arquivo vazio.

## Rodando o Projeto

Assim que realizar o download ou clonar o projeto, 
basta instalar os requirements através do comando:

```bash
$ python -m pip install -r requirements.txt
```

Após a instalação, o servidor pode ser inicializado com o comando:

```bash
$ python entry_point.py
```
Você também pode rodar este servidor utilizando o docker realizando os
seguintes comandos:

```bash
$ docker build -t servidor_flask .
$ docker run -d -p 5000:5000 servidor_flask
```

Desta maneira, o servidor estará rodando em uma imagem do Docker e se comunicando com 
sua máquina através da porta 5000.
