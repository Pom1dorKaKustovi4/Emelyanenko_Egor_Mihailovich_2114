with open("devices.txt", encoding="utf8") as f:  # чтение файла
    head = f.readline().strip()
    names = f.readlines()
new_names = []
for i in names:
    new_names.append(i.strip().split("*"))

for i in range(len(new_names)):  # сортировка
    for now in range(len(new_names) - i - 1):
        if new_names[now][0] < new_names[now + 1][0]:
            new_names[now], new_names[now + 1] = new_names[now + 1], new_names[now]

for i in range(5):
    print(f"{new_names[i][0]} - {new_names[i][1]} - {new_names[i][-1]}")
