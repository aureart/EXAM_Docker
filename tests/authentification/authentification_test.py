# authentication_test.py
import os
import requests


# définition de l'adresse de l'API
api_address = os.getenv('API_ADDRESS', 'localhost')
# port de l'API
api_port = os.getenv('API_PORT', 8000) #port sur lequel l'api est disponilble
log_path = os.getenv('LOG_PATH', None) #Définii dns docker-compose


def run_test(api_address, api_port):
    #
    users = [("alice", "wonderland"), ("bob", "builder"), ("clementine", "mandarine")]

    for username, password in users:
        response = requests.get(
            url=f"http://{api_address}:{api_port}/permissions",
            params={'username': username, 'password': password}
        )

        status_code = response.status_code
        expected_status = 200 if username in ["alice", "bob"] else 403
        test_status = 'SUCCESS' if status_code == expected_status else 'FAILURE'

        output = f'''
        ============================
            Authentication test
        ============================

        request done at "/permissions"
        | username="{username}"
        | password="{password}"

        expected result = {expected_status}
        actual result = {status_code}

        ==>  {test_status}
        '''

        # impression dans un fichier
        print(output)
        if os.environ.get('LOG') == '1':
            with open(log_path, 'a') as file:
                file.write(output)

if __name__ == "__main__":
    run_test('localhost', 8000)  # Adjust address and port if needed