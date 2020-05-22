HTTP_STATUS_CODE = {
    'OK': 200,
    'BAD_REQUEST': 400
}


def get_json(request):
    if not request.is_json:
        raise Exception('Arquivo JSON nao encontrado')

    else:
        return request.get_json()


def get_from_request(data, key):

    if key not in data:
        raise KeyError('Chave nao encontrada: {}'.format(key))

    else:
        return data[key]


def get_files(request):
    values = list(request.files.listvalues())

    if not values:
        raise FileNotFoundError('Requisicao sem arquivos')

    else:
        arquivos = []
        [arquivos.extend(value) for value in values]
        return arquivos
