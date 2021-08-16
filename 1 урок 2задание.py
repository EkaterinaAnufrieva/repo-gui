sek = input('Введите время в секундах ')
h = int(sek)//60
if 60 > h:
    s = int(sek)-h*60
    print("00:"+str(h)+":"+str(s))
if h > 60:
    a = h//60     # часы
    b = h - a*60   # минуты
    e = int(sek)-60*a*60-b*60 # секунды
    print(str(a)+":"+str(b)+":"+str(e))
