def search(n, subj):  # бинарный поиск
    k = len(subj) // 2
    result = []
    if subj[k][0] == n:
        print(
            f"{req} найдены следующие варианты: {subj[k][0]} {subj[k][1]} - тип устройства: {subj[k][2]}; Разрешение экрана - {subj[k][3]}; Цена - {subj[k][-1]}")
        return 0
    if subj[k][0] <= n:
        search(n, subj[k:])
    else:
        search(n, subj[:k])


with open("devices.txt", encoding="utf8") as f:  # открытие и сортировка файла
    head = f.readline().strip()
    names = f.readlines()
company = []
new_names = []
for i in names:
    new_names.append(i.strip().split("*"))
for i in new_names:
    company.append(i[0])
new_names = sorted(new_names, key=lambda x: (x[0], 1 / int(x[-1].split(",")[0])))

req = input()
while req != "=":
    if req in company:
        search(req, new_names)
    else:
        print("У нас нет данного устройства")
    req = input()
