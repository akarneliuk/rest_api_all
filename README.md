# REST API cheat sheats
This repo is crated as a source for the REST API blogpost series on the http://karneliuk.com. It intends to cover the interaction with the various applications via REST API. The primary focus is the network automation and programmability, as all the recent topics on the http://karneliuk.com were built around REST API.

## Implemented requests
- GET
- POST
- DELETE

## Covered tools
- Ansible (2.8)
- Bash (4.2)
- Postman (1.18)
- Python (3.7)

It might be that provided scripts are working in other versions, but it was not tested and therefore not guaranteed. In general all the information is provided on the AS-IS basis.

## Python considerations
Python 3.7 version was used, and all the tests were performed in the virtual environment (venv). To get it running perform: 
- `python3.7 -m venv vev` in the folder with the scripts to create the virtual environment.
- `source venv/bin/active` to enter the virtual environment context.
- `pip install --upgrade pip` to update the pip to the latest version.
- `pip install -r requirements.txt` to install the used (or potentially used in the near future) Python libraries.

## Execution (e.g. the simplest GET request):
1) For Ansible playbooks: `ansible-playbook rest_get.yml -i ansible_hosts.yml`
2) For Bash: `./rest_get.sh`
3) For Postman: import proper Postman collection and use it.
4) For Python: `python rest_get.py` from the virtual environment context.
For further details read the official articles at http://karneliuk.com/tag/rest-api/.

## Related projects
The REST API with Ansbile was extensivly used in the two my big projects:
- Service Provider Fabric (https://github.com/akarneliuk/service_provider_fabric)
- Data Centre Fabric (https://github.com/akarneliuk/data_center_fabric)
