import json
def load_file():
    filename = input('Enter route to vacancies list: ')
    with open(filename, mode='r', encoding='utf-8') as myfile:
        data = json.load(myfile)
    return data

vacancies = []
vacancies_list = load_file()

def treatment_vacancies(vacancies):
    vac = {}
    for i in range(100):
        vac['prof'] = vacancies_list['objects'][i]['profession']
        vac['work'] = vacancies_list['objects'][i]['work']
        vac['pay'] = vacancies_list['objects'][i]['payment_from']
        vacancies.append(vac)
        vac = {}
    return vacancies

if __name__ == '__main__':
    new_list = []
    new_list = treatment_vacancies(vacancies)
    filename = input('Enter route for new vacancie list: ')
    with open(filename, mode='w', encoding='utf-8') as myfile:
        json.dump(new_list, myfile)








