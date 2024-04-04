from data_create import name_data,surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные \n\n"
    f"1 Вариант: \n "
    f"{name}\n{surname}\n{phone}\n{address} \n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{address} \n"
    f"Выберите вариант:  " ))

    while var != 1 and var != 2:
        print('Неправильный ввод')
        var = int(input('Введите число '))

    if var == 1:
        with open('data_1var.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address} \n\n")
    elif var == 2:
         with open('data_1var.csv', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address} \n\n")      

             
def print_data():
    pass

input_data()