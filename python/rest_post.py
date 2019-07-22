# Modules
import requests

# Varibles
destination_url = 'localhost'
destination_port = 2375
resource_path = 'containers'
container_name = 'dcf_dhcp'
action = 'kill'


# Functions
def rest_api_post(active_url, active_port, active_resource,
                  active_container, active_action):
    resource_path = "http://%s:%s/%s/%s/%s" % (active_url, active_port,
                                               active_resource,
                                               active_container,
                                               active_action)

    rest_response = requests.post(url=resource_path)
    return rest_response


# Body
if __name__ == '__main__':
    reply = rest_api_post(destination_url, destination_port,
                          resource_path, container_name, action)

    print(reply)
