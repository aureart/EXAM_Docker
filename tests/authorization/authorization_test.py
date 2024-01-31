import requests
import os

def run_authorization_test(api_address, api_port, log_path):
    users = {
        "alice": ["v1", "v2"],  # Alice a accès aux deux versions
        "bob": ["v1"]           # Bob a accès uniquement à la v1
    }

    for username, versions in users.items():
        for version in versions:
            url = f"http://{api_address}:{api_port}/{version}/sentiment"
            response = requests.get(url, params={"username": username, "password": "correct_password", "sentence": "test"})

            status_code = response.status_code
            expected_status = 200
            test_status = 'SUCCESS' if status_code == expected_status else 'FAILURE'

            output = f'''
            ============================
                Authorization test
            ============================

            request done at "/{version}/sentiment"
            | username="{username}"

            expected result = {expected_status}
            actual result = {status_code}

            ==>  {test_status}
            '''

            print(output)
            if log_path:
                with open(log_path, 'a') as file:
                    file.write(output)


if __name__ == "__main__":
    api_address = os.getenv('API_ADDRESS', 'localhost')
    api_port = os.getenv('API_PORT', 8000)
    log_path = os.getenv('LOG_PATH', None)  # Si LOG_PATH est défini, les logs seront écrits dans ce fichier

    run_authorization_test(api_address, api_port, log_path)