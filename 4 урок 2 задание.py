my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new = []
for id, val in enumerate(my_list):
    if id>0 and my_list[id]>my_list[id-1]:
        new.append(val)
print(new)

