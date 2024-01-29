import requests

def connect_to_stream():
    response = requests.get('http://127.0.0.1:8000/stream', stream=True)

    for line in response.iter_lines():
        if line:  # Filter out keep-alive new lines
            print('Received data:', line.decode('utf-8'))
            # Process received data here

if __name__ == '__main__':
    connect_to_stream()