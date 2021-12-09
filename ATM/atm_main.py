# from os import name, read
import pathlib
import csv

def start_main():
    pass

def balance_changer(user_id,calc_char):
    if calc_char == '+':
        with open(pathlib.Path(__file__).parent.joinpath('DEPOSIT').joinpath(f'{user_id}.txt'), 'r+') as many_file:
            temp = int(input('n mach ? '))
            temp_many = int(many_file.read()) + temp
            many_file.write(str(temp_many))
            print(temp_many)
    elif calc_char == '-':
        with open(pathlib.Path(__file__).parent.joinpath('DEPOSIT').joinpath(f'{user_id}.txt'), 'r+') as many_file:
            temp = int(input('n mach ? '))
            temp_many = int(many_file.read()) - temp
            many_file.write(str(temp_many))
            print(temp_many)
           

def balance_checkr(user_id):    #prod
    temp_many = 0
    with open(pathlib.Path(__file__).parent.joinpath('DEPOSIT').joinpath(f'{user_id}.txt'), 'r') as many_file_temp:
            temp_many = many_file_temp.read()
            print(f'you deposut {temp_many} $')

def user_menu(menu_page):
    if menu_page == '1':
        print('balance check 1 ')
        print('balance change 2 ')
        print('balance exit 3 ')
    # if menu_page == '2'
    return

def validator(user_name = 0,user_password = 0): #prod
    with open(pathlib.Path(__file__).parent.joinpath('db').joinpath('db.txt'), 'r') as validator_file:
        #print(validator_file.read())
        temp_file = csv.DictReader(validator_file)
        for dict_user in temp_file:
            if user_name == dict_user['name']:
                if user_password == dict_user['password']:
                    return dict_user['name']
                else:
                    print('error password')
            else:
                print('user is not found... ')


user_name = 'user_1'
user_password = '1111'
while True:
    flag = validator(user_name,user_password)
    if flag != None:
        user_menu('1')
        user_option = input('_ ')
        if user_option == '1':
            balance_checkr(user_name)
        elif user_option == '2':
            add_or_take = input('add 1 or take 2 ?')
            if add_or_take == '1':
                balance_changer(user_name,'+')
            elif add_or_take == '2':
                balance_changer(user_name,'-')

    
    
