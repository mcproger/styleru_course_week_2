import json
import matplotlib.pyplot as plt

def load_file():
    filename = input('Enter route to vacancies list: ')
    with open(filename, mode='r', encoding='utf-8') as myfile:
        data = json.load(myfile)
    return data

def language_list():
    languages = {'1С': [0, 0], 'Python': [0, 0], 'C': [0, 0], 'C++': [0, 0], 'С#': [0, 0],
     'Java': [0, 0],  'Delphi': [0, 0],  'CSS': [0, 0], 'HTML': [0, 0],
     'PHP': [0, 0], 'JS': [0, 0], 'Ruby': [0, 0], 'Swift': [0, 0], 'Objective-C': [0, 0]}
    return languages

def language_rating(languages):
    vacancies_list = load_file()
    for vacancies in vacancies_list:
        for language in languages:
            if (vacancies['prof'] == None) or (vacancies['work'] == None):
                continue
            if (vacancies['prof'].find(language) != -1) or (vacancies['work'].find(language) != -1) or vacancies['pay'] != 0:
                languages[language][0] = languages[language][0] + 1
                languages[language][1] = languages[language][1] + vacancies['pay']
    for language in languages:
        if (languages[language][0] != 0) and (languages[language][1] != 0):
            languages[language][1] = (languages[language][1] // languages[language][0])
    return languages

def hist_draw():
    language = [language for language in rating_list]
    pay = [rating_list[language][1] for language in rating_list]
    fig = plt.figure()
    plt.bar(range(len(rating_list)), pay, tick_label=language)
    plt.title('Statistic of vacancies')
    plt.show()

if __name__ == '__main__':
    languages = language_list()
    rating_list = language_rating(languages)
    for language in rating_list:
        print(language, rating_list[language][0], rating_list[language][1])
    hist_draw()




