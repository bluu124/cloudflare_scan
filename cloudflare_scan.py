import argparse
import socket
import requests

# Parser
def parser_args():
    parser = argparse.ArgumentParser(description='Identificar si un sitio está protegido por Cloudflare')
    parser.add_argument('-t', '--target', dest='target', required=True, help='El sitio a analizar')
    parser.add_argument('-m', '--method', dest='method', default='headers', help='Debe ingresar entre el metodo headers(selección por defecto) o dns')
    args = parser.parse_args()
    return args

# Realizar una petición al sitio y buscar la palabra "cloudflare" en los headers
def check_headers(target):
    response = requests.get(target)
    headers = response.headers
    if 'server' in headers:
        server = headers['server'].lower()
        if 'cloudflare' in server:
            return True
    return False

# Obtener los registros DNS del sitio y buscar la palabra "cloudflare"
def check_dns(target):
    try:
        dns_records = socket.getaddrinfo(target, None)
    except socket.gaierror:
        return False
    for record in dns_records:
        if 'cloudflare' in record[3][0]:
            return True
    return False

if __name__ == '__main__':
    args = parser_args()
    target = args.target
    method = args.method

    if method == 'headers':
        if check_headers(target):
            print(f'El sitio {target} está protegido por Cloudflare mediante headers')
        else:
            print(f'El sitio {target} no está protegido por Cloudflare mediante headers')
    elif method == 'dns':
        if check_dns(target):
            print(f'El sitio {target} está protegido por Cloudflare mediante dns')
        else:
            print(f'El sitio {target} no está protegido por Cloudflare mediante dns')
    else:
        print('Método inválido, utiliza headers o dns')
