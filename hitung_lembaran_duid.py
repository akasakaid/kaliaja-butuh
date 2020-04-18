jml = int(input('Masukkan jumlah uang: '))

# pecahan seratus ribu
seratus,re1 = divmod(jml,100000)
print('pecahan 100 ribu:',seratus,'lembar')
# pecahan 50 ribu
lima, re2 = divmod(re1,50000)
print('pecahan 50 ribu',lima,'lembar')
# pecahan 20 ribu
duap, re3 = divmod(re2,20000)
print('pecahan 20 ribu',duap,'lembar')
# pecahan 10 ribu
sepp, re4 = divmod(re3,10000)
print('pecahan 10 ribu',sepp,'lembar')
# pecahan 5 ribu
limar, re5 = divmod(re4,5000)
print('pecahan 5 ribu',limar,'lembar')
# pecahan 2 ribu
duar, re6 = divmod(re5,2000)
print('pecahan 2 ribu',duar,'lembar')
# pecahan 1 ribu
seri, re7 = divmod(re6,1000)
print('pecahan 1 ribu',seri,'lembar')
# pecahan 500
limas, re8 = divmod(re7,500)
print('pecahan 500',limas,'keping')
rotos, re9 = divmod(re8,200)
print('pecahan 200',rotos,'keping')
tustus, re10 = divmod(re9,100)
print('pecahan 100',tustus,'keping')
print('total jumlah lembaran',seratus+lima+duap+sepp+limar+duar+seri,'lembar')
print('total jumlah keping',limas+rotos+tustus,'keping')
