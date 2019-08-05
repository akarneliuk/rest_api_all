# Modules
import requests
import json

# Varibles
destination_url = 'localhost'
destination_port = 32768
resource_path = 'api/dcim/devices/'
netbox_token = '0123456789abcdef0123456789abcdef01234567'


# Functions
def rest_api_post(active_url, active_port, active_resource,
                  active_token):

    resource_path = "http://{}:{}/{}".format(active_url, active_port, 
                                             active_resource)
    all_headers = {
                      'Authorization': 'Token {}'.format(active_token),
                      'Content-Type': 'application/json'
                  }
    data_body = {
                    'name': 'de-test-spine-333', 
                    'device_type': 3, 
                    'device_role': 3, 
                    'site': 1, 
                    'status': 2
                }

    rest_response = requests.post(url=resource_path, 
                                  headers=all_headers,
                                  data=json.dumps(data_body))

    return rest_response.json()


# Body
if __name__ == '__main__':
    reply = rest_api_post(destination_url, destination_port, 
                          resource_path, netbox_token)

    print(reply)
