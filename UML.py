# Khởi tạo các class:
class Customer:
	def __init__(self,name,address):
		self.name= name
		self.address=address
	def getInfo (self, name, address) -> str:
		return f" Name : {self.name}, Address: {self.address}"

class Item:
	def __init__(self,name,shippingweight, description: str):
		self.name=name
		self.shippingweight= shippingweight
		self.description=description
		self.price= input()
		self.tax=input()
		self.instock= input()
	def getInfoitem(self)-> str:
		return  f""" Name: {self.name}
		             Price: {self.price}
		             Tax: {self.tax}
		             Instock: {self.instock}"""

class Ordertail:
	item : list[Item]
	def __init__(self,quatity,taxStatus,item):
		self.quatity=quatity
		self.taxStatus=taxStatus
		self.item=item
	def Calcsub:
		pass
	def Calcweight:
		pass
	def Calctax:
		pass


class Order(Customer):
	ordertail: list[Ordertail]
	def __init__(self,name,address,date,status, ordertail):
		customer.__init__(name,address)
		self.date=date
		self.status=status
	def Totalwweight:
		pass
	def Calctotal:
		pass

class Payment(Order):
	def __init__(self,name,address,date,status,ordertail,amount):
		Order.__init__(name,address,date,status)
		self.amount=amount
class Cash(Payment):
	def __init__(self,name,address,date,status,ordertail,amount, cashTendered):
		self.cashTendered=cashTendered
class Check(Payment):
	def __init__(self,name,address,date,status,ordertail,amount,name,bankID):
		self.name=name
		self.bankID=bankID
class Credit(Payment):
	def __init__(self,name,address,date,status,ordertail,amount,number,type,expDate)
								
	


