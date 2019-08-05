# Modules
import requests
import json

# Varibles
destination_url = 'localhost'
destination_port = 32768
resource_path = 'api/dcim/devices/'
netbox_token = '0123456789abcdef0123456789abcdef01234567'
delete_id = '23/'

# Functions
def rest_api_delete(active_url, active_port, active_resource,
                    active_token):

    resource_path = "http://{}:{}/{}".format(active_url, active_port, 
                                             active_resource)
    all_headers = {
                      'Authorization': 'Token {}'.format(active_token)
                  }

    rest_response = requests.delete(url=resource_path, 
                                    headers=all_headers)

    return rest_response


# Body
if __name__ == '__main__':
    summary_resource = "{}{}".format(resource_path, delete_id)
    reply = rest_api_delete(destination_url, destination_port, 
                            summary_resource, netbox_token)

    print(reply)
