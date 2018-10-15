# Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
# Написать скрипт, автоматизирующий его заполнение данными. Для этого:
# Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
# цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл
# orders.json. При записи данных указать величину отступа в 4 пробельных символа;
# Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
import json


def write_order_to_json(item, quantity, price, buyer, date):
    data = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date,
    }
    with open("orders.json") as f:
        obj = json.loads(f.read())
        obj['orders'].append(data)
    with open("orders.json", 'w') as f:
        f.write(json.dumps(obj, indent='    '))


write_order_to_json('telephone', '1', '7800', 'Veronika V', '11/11/2018')

# {"orders": []}
