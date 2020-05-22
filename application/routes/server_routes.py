import re
from flask import request, Response
from flask_restful import Resource
from application.server import api
from application.routes.utils import HTTP_STATUS_CODE
from application.routes.utils import get_json, get_from_request, get_files


class CPF(Resource):
    def post(self):
        try:
            data = get_json(request)

            cpf = get_from_request(data, 'cpf')
            cpf = re.sub('[^0-9]', '', cpf)

        except Exception as e:
            resp = {
                    'error': str(e),
                    'status': HTTP_STATUS_CODE['BAD_REQUEST']
            }

            return resp

        is_valid = self.valida_cpf(cpf)

        resp = {
                'is_valid': is_valid,
                'status': HTTP_STATUS_CODE['OK']
        }

        return resp

    def valida_cpf(self, cpf):
        is_valid = True

        if len(cpf) != 11 or cpf.count(cpf[0]) == 11:
            is_valid = False

        if(is_valid):
            is_valid = self._valida_digito(cpf, -2, 10)

        if(is_valid):
            is_valid = self._valida_digito(cpf, -1, 11)

        return is_valid

    def _valida_digito(self, cpf, pos, count):
        digito_valido = True

        soma = [int(a)*b for a, b in zip(cpf[:pos], range(count, 1, -1))]
        soma = 10*sum(soma)

        if soma % 11 != int(cpf[pos]):
            digito_valido = False

        return digito_valido


class JsonUnicos(Resource):
    def post(self):
        try:
            data = get_json(request)

            compara = get_from_request(data, 'compara')

            unicos = self.encontra_unicos(compara)

        except Exception as e:
            resp = {
                    'error': str(e),
                    'status': HTTP_STATUS_CODE['BAD_REQUEST']
            }

            return resp


        resp = {
                'unicos': unicos,
                'status': HTTP_STATUS_CODE['OK']
        }

        return resp

    def encontra_unicos(self, data):
        unicos = set(data[0])

        for i in range(1, len(data)):
            unicos ^= set(data[i])

        return list(unicos)


class ArquivosUnicos(Resource):
    def post(self):
        try:
            arquivos = get_files(request)

            unicos = self.compara_arquivos(arquivos)

        except Exception as e:
            resp = {
                    'error': str(e),
                    'status': HTTP_STATUS_CODE['BAD_REQUEST']
            }

            return resp

        return Response(unicos,
                        mimetype='text/plain',
                        status=HTTP_STATUS_CODE['OK'])

    def compara_arquivos(self, arquivos):
        unicos = set()

        for arq in arquivos:
            data = arq.read().strip().split('\n'.encode('ascii'))
            unicos ^= set(data)

        unicos = [x+'\n'.encode('ascii') for x in list(unicos)]

        return unicos


def init_routes():
    api.add_resource(CPF, '/validacao/cpf')
    api.add_resource(JsonUnicos, '/compara/json')
    api.add_resource(ArquivosUnicos, '/compara/arquivos')
