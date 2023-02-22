list = []
filename1 = '1.txt'
filename2 = '2.txt'
filename3 = '3.txt'


with open('1.txt') as file1:
    len1 = len(file1.readlines())
    list.append(len1)
with open('2.txt') as file2:
    len2 = len(file2.readlines())
    list.append(len2)
with open('3.txt') as file3:
    len3 = len(file3.readlines())
    list.append(len3)

match = {len1: filename1, len2: filename2, len3: filename3}


list.sort()

for i in list:
    print(match[i])
    print(i)
    print("".join(open(match[i]).readlines()))


