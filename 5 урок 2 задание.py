with open('text_for_5.2lesson.txt', 'r') as text:
    content = text.readlines()
    for num, line in enumerate(content):
        word_cont = len(line.split())
        print(f"{num+1} строка - {word_cont} слов")







