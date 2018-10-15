# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание
# данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в
# соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
# os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и
# поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта»,
# «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для
# каждого файла);
# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение
# данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
# Проверить работу программы через вызов функции write_to_csv().

import os
import csv


def get_data():
    files = [file for file in os.listdir('.') if file.startswith('info')]
    data = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    for file in files:
        with open(file) as f:
            for line in f.readlines():
                if any(line.startswith(d) for d in data):
                    maindata.append([line.split(':')[0].strip(), line.split(':')[1].strip()])
    for i in range(len(maindata)):
        if maindata[i][0] == data[0]:
            os_prod_list.append(maindata[i][1])
        if maindata[i][0] == data[1]:
            os_name_list.append(maindata[i][1])
        if maindata[i][0] == data[2]:
            os_code_list.append(maindata[i][1])
        if maindata[i][0] == data[3]:
            os_type_list.append(maindata[i][1])


def write_to_csv():
    get_data()
    with open('data_report.csv', 'w', newline='') as f:
        wr = csv.writer(f, delimiter=',')
        for i in range(len(os_prod_list)):
            text = i + 1, os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]
            wr.writerow(text)


maindata = []
os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []

write_to_csv()
