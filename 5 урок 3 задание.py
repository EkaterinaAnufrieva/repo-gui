with open('text_for_5.3lesson_txt', 'r') as text:
    content = text.readlines()
    sotrudniki = {}
    zp = 0
    for line in content:
        emp_info = line.split()
        sotrudniki.update({emp_info[0]:float(emp_info[1])})
        zp += float(emp_info[1])
averange_zp= zp / len(sotrudniki)
print(f'Средняя зп = {averange_zp}')
for k, v in sotrudniki.items():
    if v < 20000:
        print(f"{k} {v}")







