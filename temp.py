file = open('temp2.txt')
f = file.readlines()

arr1 =[]
arr2 =[]
arr3 =[]


rn = 1

for line in f:
    val = line.strip('\n')
    if rn == 1:
        arr1.append(val)
        rn = 2
    elif rn == 2:
        arr2.append(val)
        rn =3
    elif rn == 3:
        arr3.append(val)
        rn = 1

final_arr = [
    arr1,
    arr2,
    arr3,
]
print(final_arr[1][1])

