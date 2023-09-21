# 1. Приветствие
# 2. Мануал – как пользоваться программой и какие валюты доступны
# 3. Ввести исходную валюту
# 4. Ввести в какую валюту перевести
# 5. Количество валюты
# 6. Подсчёт
# 7. Вывод результата


import requests


api_key = 'cur_live_AFvHSQELaEolESfjyfxN2hnwzlSrutfOlAsFhmI1'


def print_manual():
  print('Для конвертации валюты:')
  print('- Введите код исходной валюты (например, USD)')
  print('- Введите код конечной валюты (например, EUR)')
  print('- Введите количество конвертируемой валюты (например, 100)')
  print('- Программа выведет результат конвертации')
  print('- Чтобы увидеть список доступных валют, введите 1, если нет 2.\n')


def get_currencies():
    url = f'https://api.currencyapi.com/v3/currencies?apikey={api_key}'
    response = requests.get(url)
    return set(response.json()['data'])


def validate_currency(currency, available):
    currency = currency.upper()
    while currency not in available:
        print('Неверная валюта')
        currency = input('Повторите ввод: ').upper()
    return currency


def validate_amount(amount):
    try:
        return float(amount)
    except ValueError:(
        print('Сумма должна быть числом'))
    return validate_amount(input('Повторите ввод суммы: '))


def get_currency_list():
    currency_url = f'https://api.currencyapi.com/v3/latest?apikey={api_key}&currencies='
    currencies_response = requests.get(currency_url)
    currencies_data = currencies_response.json()

    print('Доступные валюты:')
    for currency in currencies_data['data'].keys():
        print(currency)


currencies = get_currencies()


print('Добро пожаловать в конвертер валют!\n')
print_manual()

if input('Хотите увидеть список доступных валют? 1 - да, 2 - нет: ') == '1':
    currencies = get_currencies()
    print(currencies)

base_currency = validate_currency(input('Валюта: '), currencies)
target_currency = validate_currency(input('Конвертировать в: '), currencies)
amount = validate_amount(input('Сумма: '))

conversion_url = f'https://api.currencyapi.com/v3/latest?apikey={api_key}&base_currency={base_currency}&currencies={target_currency}'
conversion_response = requests.get(conversion_url)
conversion_data = conversion_response.json()

rate = conversion_data['data'][target_currency]['value']
result = amount * rate
result_round = round(amount * rate)

print('\nРезультат конвертации:')
print(f'{amount} {base_currency} = {result} {target_currency}\n')
print('Без копеек:')
print(f'{amount} {base_currency} = {result_round} {target_currency}')