# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile
name = ''
age = 0
phone = ''
email = ''
index = ''
postal_address = ''
info = ''
# information about the entrepreneur
OGRNIP = 0
INN = 0
payment_account = 0
bank_name = ''
BIC = 0
correspondent_account = 0


def general_info_user(name_parameter, age_parameter, phone_parameter,
                      email_parameter, index_parameter,
                      postal_address_parameter, info_parameter):
    print(SEPARATOR)
    print('Имя:    ', name_parameter)
    if 11 <= age_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif age_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= age_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'
    print('Возраст:', age_parameter, years_parameter)
    print('Телефон:', phone_parameter)
    print('E-mail: ', email_parameter)
    print('Индекс: ', index_parameter)
    print('Почтовый адрес: ', postal_address_parameter)
    if info:
        print('')
        print('Дополнительная информация:')
        print(info_parameter)


print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break
    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                name = input('Введите имя: ')
                while 1:
                    # validate user age
                    age = int(input('Введите возраст: '))
                    if age > 0:
                        break
                    print('Возраст должен быть положительным')

                    uphone = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                    phone = ''
                    for symbol in uphone:
                        if symbol == '+' or ('0' <= symbol <= '9'):
                            phone += symbol

                    email = input('Введите адрес электронной почты: ')
                    uindex = input('Введите почтовый индекс: ')
                    index = ''
                    for symbol in uindex:
                        if symbol == '+' or ('0' <= symbol <= '9'):
                            index += symbol
                    postal_address = input(
                        'Введите почтовый адрес (без индекса): ')
                    info = input('Введите дополнительную информацию:\n')
            elif option2 == 2:
                # input information about the entrepreneur
                while True:
                    OGRNIP = input('Введите ОГРНИП: ')
                    if len(OGRNIP) == 15:
                        break
                    else:
                        print('ОГРНИП должен содержать 15 цифр')

                    INN = int(input('Введите ИНН: '))

                while True:
                    payment_account = input('Введите расчётный счёт: ')
                    if len(payment_account) == 20:
                        break
                    else:
                        print('Расчётный счёт должен содержать 20 цифр')

                    bank_name = input('Введите название банка: ')
                    BIC = int(input('Введите БИК: '))
                    correspondent_account = int(
                        input('Введите корреспондентский счёт: '))

            else:
                print('Введите корректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(name, age, phone, email, index,
                                  postal_address, info)

            elif option2 == 2:
                general_info_user(name, age, phone, email, index,
                                  postal_address, info)

                # print bank requisites
                print('')
                print('Информация о предпринимателе')
                print('ОГРНИП:', OGRNIP)
                print('ИНН:   ', INN)
                print('Банковские реквизиты')
                print('Р/с:   ', payment_account)
                print('Банк:  ', bank_name)
                print('БИК:   ', BIC)
                print('К/с:   ', correspondent_account)
            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')
