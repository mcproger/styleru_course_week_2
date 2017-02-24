import requests
import json
import getpass
def make_request():
    api_key = getpass.getpass('Enter your Api Key: ')
    header = {'X-Api-App-Id': api_key}
    params = {'town': '4', 'keyword': 'Программист', 'count': '100', 'catalogue_id': 48}
    request = requests.get('https://api.superjob.ru/2.0/vacancies', params=params, headers=header)
    return request.json()

if __name__ == '__main__':
    vacancie_list = make_request()
    filename = input('Enter route for vacancies list: ')
    with open(filename, mode='w', encoding='utf-8') as myfile:
        json.dump(vacancie_list, myfile)


