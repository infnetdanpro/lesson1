input_name = input('Введите ваше имя: ')
input_last_name = input('Введите вашу фамилию: ')
user_info = {'first_name':input_name, 'last_name':input_last_name}
print(user_info.get('first_name') + ' ' + user_info.get('last_name'))