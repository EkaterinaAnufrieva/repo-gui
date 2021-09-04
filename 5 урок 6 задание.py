result = {}
with open("text_for_5.6lesson.txt") as file:
    file_lines = file.readlines()
    for line in file_lines:
        data = line.split()
        hours = 0
        for elem in data [1:]:
            if elem != '-':
                num = '0'
                for i in elem:
                    if i.isdigit():
                        num +=1
                    else:
                        break
                    hours += int(num)
        result.update({data[0].strip(':'): hours})
print(result)





