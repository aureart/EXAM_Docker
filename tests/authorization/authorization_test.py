import requests
import os
# définition de l'adresse de l'API
api_address = os.getenv('API_ADDRESS', 'api')
# port de l'API
api_port = os.getenv('API_PORT', 8000) #port sur lequel l'api est disponilble
log_path = os.getenv('LOG_PATH', None) #Définii dns docker-compose


def run_authorization_test(api_address, api_port, log_path):
    users = {
        "alice": {"username": "alice", 
                  "password": "wonderland", 
                  "versions": ["v1", "v2"]},  
        "bob": {"username": "bob",
                 "password": "builder",
                   "versions": ["v1"]}
    }

    for user, details in users.items():
        for version12 in ["v1", "v2"]:
            url = f"http://{api_address}:{api_port}/{version12}/sentiment"
            params = {
                "username": details["username"],
                "password": details["password"],
                "sentence": "test authorization"
            }
            response = requests.get(url, params=params)

            # Déterminez si le test est réussi
            status_code = response.status_code
            expected_status = 200 if (user != "bob" or version12 != "v2") else 403
            test_status = 'SUCCESS' if status_code == expected_status else 'FAILURE'

            #expected_status = 200
            #test_status = 'SUCCESS' if status_code == expected_status else 'FAILURE'

            output = f'''
            ============================
                Authorization test
            ============================

            request done at "/{version12}/sentiment"
            | username="{details["username"]}"

            expected result = {expected_status}
            actual result = {status_code}

            ==>  {test_status}
            '''

            print(output)
            if os.environ.get('LOG') == '1':
                with open(log_path, 'a') as file:
                    file.write(output)


if __name__ == "__main__":
    run_authorization_test(api_address, api_port, log_path)