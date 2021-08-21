vvod_user = input("Веедите строку из нескольких слов, разделённых пробелами. ")
words = vvod_user.split()
for num, word in enumerate(words):
    print(f'#{num} - {word[:10]}')
# 4 zadanie