import os
import requests

# définition de l'adresse de l'API
api_address = os.getenv('API_ADDRESS', 'api')
# port de l'API
api_port = os.getenv('API_PORT', 8000) #port sur lequel l'api est disponilble
log_path = os.getenv('LOG_PATH', None)
#LOG = 1

def run_content_test(api_address, api_port, log_path):
    sentences = ["life is beautiful", "that sucks"]
    users = {
        "alice": {"username": "alice", 
                  "password": "wonderland", 
                  "versions": ["v1", "v2"]},  
        "bob": {"username": "bob",
                 "password": "builder",
                   "versions": ["v1"]}
    }

    for sentence in sentences:
        for user, details in users.items():
            for version in details["versions"]:
                response = requests.get(
                    url=f"http://{api_address}:{api_port}/{version}/sentiment",
                    params = {
                    "username": details["username"],
                    "password": details["password"],
                    "sentence": sentence
                            }
                )

                status_code = response.status_code
                expected_status = 200
                result = response.json()
                score = result.get("score", 0)
                sentiment = "positive" if score > 0 else "negative"
                expected_sentiment = "positive" if sentence == "life is beautiful" else "negative"
                test_status = 'SUCCESS' if status_code == expected_status and sentiment == expected_sentiment else 'FAILURE'

                output = f'''
            ============================
                Content test
            ============================

            request done at "/{version}/sentiment"
            | sentence="{sentence}"

            expected sentiment = {expected_sentiment}
            actual sentiment = {sentiment}

            ==>  {test_status}
            '''

                print(output)
                if os.environ.get('LOG') == '1':
                #if(LOG)
                  with open(log_path, 'a') as file:
                     file.write(output)

if __name__ == "__main__":
    run_content_test(api_address, api_port, log_path)