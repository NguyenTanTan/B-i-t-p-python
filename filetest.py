'''''#Bài 1,2
import random

stir=input("Nhập chuỗi ký tự: ")
# Mở file để viết:
wri=open('test.txt','w')
# Ghi file
with open('test.txt','w') as wri:
    wri.write(stir)
#Đóng file
wri.close()
# Mở file để đọc:
rea=open('test.txt','r')
# Đọc file
with open('test.txt','r') as rea:
    dc=rea.read()
rea.close()
print(dc)
# Bài 3,4
# Nhập tên tập tin:
namefile=input(" Tên tập tin: ")
stir1=input("Nhập chuỗi ký tự: ")
nhap= open(namefile,'a+')
with open(namefile,'a+') as nhap:
    nhap.write(stir1)
    doc=nhap.read()
print(doc)
nhap.close()'''
#Bài 5
# Sinh ngẫu nhiên:
import random 
random_list= [random.randrange(-1000,1001) for i in range(0,1000)]
inputnamefile= input("Nhập tên tập tin bài 5: ")
# Open file to write:
namefile5= open(inputnamefile,"a+")
for i in range(0,100):
	for j in range(0,10):
		if j==9:
			namefile5.write(str(random_list[i*10+j]))
		else:
			namefile5.write(str(random_list[i*10+j])+",")
	namefile5.write("\n")
namefile5.close()
# Open file to read:
namefile6=open(inputnamefile,"r")
readfile=namefile6.read()
listlife=readfile.split(",")
tabfile="\t".join(listlife)
print(tabfile)
namefile6.close()








