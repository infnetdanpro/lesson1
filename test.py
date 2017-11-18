MyDict = {
	'Максим':{'city':'Moscow', 'temp':20, 'wind':'северный'},
	'Валерий':{'city':'Samara', 'temp':15, 'wind':'восточный'},
	'Дмитрий':{'city':'Krasnoda', 'temp':30, 'wind':'южный'}
	}
name = input('Введите Имя: ')
print('\n')
print(MyDict[name]['city'] + '\n' + str(MyDict[name]['temp']) + '\n' + MyDict[name]['wind'])
