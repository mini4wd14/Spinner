def counterClockwise(a):
    b = []
    list1 = []
    list2 = []
    list3 = []
    for i in range(3):          #Membuat list yang beranggotakan digit ke 3 setiap list awal
        list1.append(a[i][2])
    for i in range(3):          #Membuat list yang beranggotakan digit ke 2 setiap list awal
        list2.append(a[i][1])
    for i in range(3):          #Membuat list yang beranggotakan digit ke 1 setiap list awal
        list3.append(a[i][0])
    b.append(list1)             
    b.append(list2)             #Menggabungkan list1,2,3 kedalam 1 list b
    b.append(list3)
    for i in b:                 #print setiap item yang ada pada list b kebawah
        print(i)

counterClockwise(
[[1,2,3],
[4,5,6],
[7,8,9]])