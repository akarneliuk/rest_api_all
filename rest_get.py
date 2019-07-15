# Modules
import requests

# Varibles
destination_url = 'localhost'
destination_port = 2375
resource_path = 'info'


# Functions
def rest_api_get(active_url, active_port, active_resource):
    resource_path = "http://%s:%s/%s" % (active_url, active_port, active_resource)

    rest_response = requests.get(url=resource_path)
    return rest_response.json()

# Body
if __name__ == '__main__':
    reply = rest_api_get(destination_url, destination_port, resource_path)

    print(reply)
