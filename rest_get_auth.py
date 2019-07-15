# Modules
import requests


# Varibles
destination_url = 'localhost'
destination_port = 32768
resource_path = 'api/dcim/devices/'
netbox_token = '0123456789abcdef0123456789abcdef01234567'


# Functions
def rest_api_get(active_url, active_port, active_resource, active_token):
    resource_path = "http://%s:%s/%s" % (active_url, active_port, active_resource)
    authorization_header = {'Authorization': 'Token %s' % active_token}

    rest_response = requests.get(url=resource_path, headers=authorization_header)
    return rest_response.json()

# Body
if __name__ == '__main__':
    reply = rest_api_get(destination_url, destination_port, resource_path, netbox_token)

    print(reply)
