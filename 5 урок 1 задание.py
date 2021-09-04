with open("text.txt", 'w') as text:
    user_text = input("Введите текст:\n")
    while user_text:
        text.write(f'{user_text}\n')
        user_text = input("Введите текст:\n")







