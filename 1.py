with open("devices.txt", encoding="utf8") as f:  # чтение файла
    head = f.readline().strip()
    names = f.readlines()
new_names = []
for i in names:
    new_names.append(i.strip().split("*"))
m = {}
for i in new_names:
    if i[2] + "," + i[5] in m:
        m[i[2] + "," + i[5]] += 1
    else:
        m[i[2] + "," + i[5]] = 1
new_names = sorted(new_names)
with open("count_company.txt", "w", encoding="utf8") as f:
    print("Ultrabook", file=f)
    for i in m.keys():
        a = i.split(",")
        if "Ultrabook" == a[0]:
            print(a[1] + "-" + str(m[i]), file=f)