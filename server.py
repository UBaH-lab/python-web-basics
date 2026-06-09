import socket
from urllib.parse import parse_qs

# Пути к HTML-файлам
ROUTES = {
    '/': 'templates/index.html',
    '/contacts': 'templates/contacts.html',
    '/index.html': 'templates/index.html',
    '/contacts.html': 'templates/contacts.html',
}


def read_file(filepath):
    """Чтение файла с помощью контекстного менеджера"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return None


def parse_request(request):
    """Парсинг HTTP-запроса"""
    lines = request.split('\r\n')
    method, path, protocol = lines[0].split()

    # Разделяем путь и параметры
    if '?' in path:
        path, params = path.split('?', 1)
    else:
        params = ''

    return method, path, params


def parse_body(request):
    """Извлечение тела POST-запроса"""
    parts = request.split('\r\n\r\n')
    if len(parts) > 1:
        return parts[1]
    return ''


def create_response(status, content, content_type='text/html'):
    """Создание HTTP-ответа"""
    response = f'HTTP/1.1 {status}\r\n'
    response += f'Content-Type: {content_type}; charset=utf-8\r\n'
    response += f'Content-Length: {len(content.encode("utf-8"))}\r\n'
    response += 'Connection: close\r\n'
    response += '\r\n'
    response += content
    return response


def handle_post(body):
    """Обработка POST-запроса"""
    if body:
        # Парсим данные формы
        parsed = parse_qs(body)
        print('=' * 40)
        print('Получены данные POST-запроса:')
        for key, value in parsed.items():
            print(f'{key}: {value}')
        print('=' * 40)


def run_server(host='127.0.0.1', port=8080):
    """Запуск сервера"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f'Сервер запущен: http://{host}:{port}')
    print('Для остановки нажмите Ctrl+C\n')

    try:
        while True:
            client_socket, address = server_socket.accept()
            request = client_socket.recv(4096).decode('utf-8')

            if not request:
                client_socket.close()
                continue

            method, path, params = parse_request(request)
            print(f'Запрос: {method} {path}')

            # Обработка POST-запроса
            if method == 'POST':
                body = parse_body(request)
                handle_post(body)

            # Определение файла для отправки
            if path in ROUTES:
                filepath = ROUTES[path]
                content = read_file(filepath)

                if content:
                    response = create_response('200 OK', content)
                else:
                    content = read_file('templates/500.html')
                    response = create_response('500 Internal Server Error', content or 'Server Error')
            else:
                content = read_file('templates/404.html')
                response = create_response('404 Not Found', content or 'Not Found')

            client_socket.send(response.encode('utf-8'))
            client_socket.close()

    except KeyboardInterrupt:
        print('\nСервер остановлен')
    finally:
        server_socket.close()


if __name__ == '__main__':
    run_server()