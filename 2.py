import csv


with open("devices.txt", encoding="utf8") as f:
    head = f.readline().strip()
    names = f.readlines()
new_names = []
print(head)
for i in names:
    new_names.append(i.strip().split("*"))

for i in range(len(new_names)):
    for now in range(len(new_names) - i - 1):
        if new_names[now][0] < new_names[now + 1][0]:
            new_names[now], new_names[now + 1] = new_names[now + 1], new_names[now]
with open("new_devises", "w", encoding="utf8") as new_file:
    print(head, file=new_file)
    for i in new_names:
        print("*".join(i), file=new_file)