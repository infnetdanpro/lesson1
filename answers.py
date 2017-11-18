def get_answer(question):
    answers = {'привет':'И тебе привет!', 'как дела':'Лучше всех', 'пока':'Увидимся'}
    return answers.get(question, 'Задайте вопрос еще раз').lower()
question = input('Введите текст: ')
print(get_answer(question)) 