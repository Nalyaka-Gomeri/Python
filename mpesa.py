from datetime import datetime
class Mpesa:
	"""
	This is my billion dollar idea
	"This class has this Attributes:phone_number,name,id_number,age,balance"
	"This class has these functions:
	transfer_money,
	buy_airtime,
	pay_bill,
	withdraw,
	deposit,
	check_balance,
	get_loan,
	pay_loan"
	"""
	def __init__(self,phone_number,first_name,last_name):
		self.phone_number=phone_number
		self.first_name=first_name
		self.last_name=last_name
		self.balance=0
		self.deposits=[]
		self.withdrawals=[]
		self.loan=[]
	def show_balance(self):
		return self.balance
	def deposit(self,amount):
		self.balance+=amount
		d=datetime.now().strftime("%c")
		description={"date":d,"amount":amount}
		self.deposits.append(description)
		message="Dear {},you have deposited {} at {}.Your new balance is {}".format(self.first_name,amount,d,self.balance)
		return message

	def withdraw(self):
		d=datetime.now().strftime("%c")
		amount=int(input("Please enter withdrawal amount"))
		description={"date":d,"amount":amount}
		self.withdrawals.append(description)
		if self.balance<amount:
			return "Your account balance is insuffecient"
		else:
			self.balance-=amount
			message="Dear {},you have withdrawn {} at {}.Your new balance is {}".format(self.first_name,amount,d,self.balance)
			return message
	def ministatement(self):
	    for deposit in self.deposits:
	    	print("Dear {},on{},you deposited{}".format(self.first_name,deposit["date"],deposit["amount"]))
	    for withdraw in self.withdrawals:
	    	print("Dear {},on{},you withdrew{}".format(self.first_name,withdraw["date"],withdraw["amount"]))
	    return	
	def loan(self):
	    amount=int(input("Kindly enter the loan amount"))
	    if amount>self.loan:
	       diff=amount-self.loan
	       self.loan=0
	       return self.deposit(diff)
	    else:
	    	self.loan+=amount
	def loanbalance(self):
		return self.loan
	def payloan(self):
		amount=int(input("kindly enter amount"))
		if amount>self.loan
		   diff=amount-self.loan
		   self.loan=0
		   return self.deposit(diff)
		else:
			self.loan-=amount

	def ministatement(self):
		for deposit in self.deposits:
			print("Dear {} {},on{},you deposited{}".format(self.first_name,self.last_name,deposit["date"],deposit["amount"]))
		for withdrawals in self.withdrawals:
		    print("Dear {} {},on{},you withdrew{}".format(self.first_name,self.last_name,withdrawals["date"],withdrawals["amount"]))
		return