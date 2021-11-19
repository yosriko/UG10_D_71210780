#program penghitung akar dari fungsi kuadrat

#input
a= float(input("Nilai a :"))
b= float(input("Nilai b :"))
c= float(input("Nilai c :"))

#proses
D= b**2-(4*a*c)

if a==0 :
    print("Maaf, nilai a nya gaboleh 0")
else: #a!=0
    if D<0:
        print("Fungsi tersebut tidak memiliki akar riil")
    elif D>0:
        import math
        x1= ((-b)+ math.sqrt(D))/(2*a)
        x2= ((-b)- math.sqrt(D))/(2*a)
        print("Akar akar dari persamaan tersebut adalah {} dan {}".format(x1,x2))
    else: #D=0
        x3= -b/(2*a)
        print("Fungsi tersebut memiliki akar kembar yaitu", x3)
