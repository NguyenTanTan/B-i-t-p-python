#Khởi tạo các lớp:
class person:
	def __init__(self,name,phone_number,email_address):
		self.name= name
		self.phone_number=phone_number
		self.email_address=email_address 

class student(person)	:
	def __init__(self,name,phone_number,email_address,student_number,average_mark):
		super().__init__(name,phone_number,email_address)
		self.student_number=student_number
		self.average_mark=average_mark
	
class professor(person):
	def __init__(self,name,phone_number,email_address,salary):
		super().__init__(name,phone_number,email_address)
		self.salary=salary
	
def main():
	# Nhập dữ liệu cho person:
	print(" Nhập tên:")
	import random
	listname=[input() for i in range(0,10)]
	listphone=[random.randint(1000000,9999999) for i in range(0,10)]
	listemail=[listname[i]+"@gmail.com" for i in range(0,10)]
	# Nhập thông tin của một person vào list:
	print(" Danh sách Person: ")
	listperson=[]
	for i in range(0,10):
		listperson.append(vars(person(listname[i],listphone[i],listemail[i])))
	for i in listperson:
		print(i)

	import random
	print(" Danh sách Student:")
	# Nhập dữ liệu cho student-professor:
	liststunumber=["ST"+str(random.randint(1,11)) for i in range(0,10)]
	listAvemark=[random.randint(40,99)/10 for i in range(0,10)]
	listsalary=[random.randint(100,999) for i in range(0,10)]
	# Nhập thông tin của một student-proffessor vào list:
	# Student:
	liststudent=[]
	listprofessor=[]
	for i in range(0,10):
		liststudent.append(vars(student(listname[i],listphone[i],listemail[i],liststunumber[i],listAvemark[i])))
	for i in liststudent:
		print(i)
	# Professor:
	print(" Danh sách Professor")
	for i in range(0,10):
		listprofessor.append(vars(professor(listname[i],listphone[i],listemail[i],listsalary[i])))		
	for i in listprofessor:
		print(i)
	# Sắp xếp person:
	print(" Sắp xếp Person theo name:")
	sortedper=sorted(listperson, key= lambda x: x['name'], reverse=True)
	for i in sortedper:
		print(i)
	# Sắp xếp student:
	print(" Sắp xếp Student theo average_mark:")
	sortedstu=sorted(liststudent, key= lambda y: y['average_mark'], reverse=True)
	for i in sortedstu:
		print(i)
	# Sắp xếp professor:
	print(" Sắp xếp Professor theo salary:")
	sortedpro=sorted(listprofessor, key= lambda z: z['salary'])
	for i in sortedpro:
		print(i)
	# Lưu danh sách vào tập tin:
	import pickle
	# Mở file và ghi vào file:
	# Person:
	openfile=open('savelistper', "wb")
	pickle.dump(listperson,openfile)
	openfile.close()
	# Student:
	openfile=open('saveliststu', "wb")
	pickle.dump(liststudent,openfile)
	openfile.close()
	# Professor:
	openfile=open('savelistpro', "wb")
	pickle.dump(listprofessor,openfile)
	openfile.close()

	# Đọc file và in ra màn hình:
	# Person
	openfile=open('savelistper', "rb")
	printfile=pickle.load(openfile)
	for i in printfile:
		print(i)
	openfile.close()
	# Student:
	openfile=open('saveliststu', "rb")
	printfile=pickle.load(openfile)
	for i in printfile:
		print(i)	 
	openfile.close()
	# Professor:
	openfile=open('savelistpro', "rb")
	printfile=pickle.load(openfile)
	for i in printfile:
		print(i)
	openfile.close()


# Chạy chường trình:
main()	
