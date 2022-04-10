import json
from bs4 import BeautifulSoup
import requests

base_url="https://samara.hh.ru/vacancy"

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/100.0.4896.75 Safari/537.36'}

keyword = input("Введите ключевое слово")

url = f'{base_url}/{keyword}'
response = requests.get(url, headers=headers)
dom = BeautifulSoup(response.text, 'html.parser')
vacancys = dom.find_all('div', {'class': 'vacancy-serp-item'})

# функция для пагинации

def max_num():
    mxnum=0
    for item in dom.find_all('a', {'data-qa': 'page-page'}):
        mxnum = list(item.strings)[0].split(" ")[-1]
    return mxnum

max_page = int(max_num())

# сбор данных

def data_collect(pages):
    vacancys_list = []
    for page in range(pages):
        url2 = f'{base_url}/{keyword}?page={page}'
        response2 = requests.get(url2, headers=headers)
        dom2 = BeautifulSoup(response2.text, 'html.parser')
        vacancys2 = dom2.find_all('div', {'class': 'vacancy-serp-item'})
        for vacancy in vacancys2:
            vacancy_data = {}
            vacancy_tittle = vacancy.find('a', {'data-qa':'vacancy-serp__vacancy-title' }).text.strip()
            vacancy_employer = vacancy.find('div',{'class':'vacancy-serp-item__meta-info-company'})
            vacancy_link = vacancy.find('a',{'data-qa':'vacancy-serp__vacancy-title'}).get('href')

            vacancy_salary = vacancy.find('span',{'data-qa':'vacancy-serp__vacancy-compensation'})
            vacancy_salary_data = {'min_salary': '', 'max_salary': '', 'currency': ''}
            if vacancy_salary is None:
                vacancy_salary_data['min_salary']=None
                vacancy_salary_data['max_salary'] = None
                vacancy_salary_data['currency'] = None
            else:
                vacancy_salary = vacancy_salary.text.replace('\u202f',"").split()
                if "от" in vacancy_salary:
                    if "руб." in vacancy_salary:
                        vacancy_salary_data['min_salary'] = int(vacancy_salary[1])
                        vacancy_salary_data['max_salary'] = None
                        vacancy_salary_data['currency'] = 'RUB'
                    if "USD" in vacancy_salary:
                        vacancy_salary_data['min_salary'] = int(vacancy_salary[1])
                        vacancy_salary_data['max_salary'] = None
                        vacancy_salary_data['currency'] = 'USD'
                if "до" in vacancy_salary:
                    if "руб." in vacancy_salary:
                        vacancy_salary_data['min_salary'] = None
                        vacancy_salary_data['max_salary'] = int(vacancy_salary[1])
                        vacancy_salary_data['currency'] = 'RUB'
                    if "USD" in vacancy_salary:
                        vacancy_salary_data['min_salary'] = None
                        vacancy_salary_data['max_salary'] = int(vacancy_salary[1])
                        vacancy_salary_data['currency'] = 'USD'
                if "от" not in vacancy_salary and 'до' not in vacancy_salary:
                    if "руб." in vacancy_salary:
                        vacancy_salary_data['min_salary'] = int(vacancy_salary[0])
                        vacancy_salary_data['max_salary'] = int(vacancy_salary[2])
                        vacancy_salary_data['currency'] = 'RUB'
                    if "USD" in vacancy_salary:
                        vacancy_salary_data['min_salary'] = int(vacancy_salary[0])
                        vacancy_salary_data['max_salary'] = int(vacancy_salary[2])
                        vacancy_salary_data['currency'] = 'USD'
        vacancy_data['vacancy_title'] = vacancy_tittle
        vacancy_data['vacancy_employer']= vacancy_employer
        vacancy_data['vacancy_link'] = vacancy_link
        vacancy_data['vacancy_salary'] = vacancy_salary_data
        vacancys_list.append(vacancy_data)
    return vacancys_list

data = data_collect(max_page)

def data_json(data):
    with open(f'{keyword}.json', "w", encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

data_json(data)






