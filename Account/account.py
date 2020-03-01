
# file = open("balanced.txt",'w')
# file.write("Welcome to the Balance sheet")

class Account:

    def __init__(self,filepath):
        self.files = filepath  # making 'filepath' usable in def
        with open(filepath,'r') as file:
            self.bal = int(file.read())

    def withdraw(self,wamt):
        self.bal = self.bal - wamt
        with open(self.files,'w') as file:
            file.write(str(self.bal))

    def deposit(self,damt):
        self.bal = self.bal + damt
        with open(self.files,'w') as file:
            file.write(str(self.bal))

    # def commit(self):
    #     with open(self.files,'w') as files:
    #         files.write(str(self.bal))

acc = Account("balanced.txt")
print("The balance is {} Rs".format(acc.bal))
drawMoney = int(input("Enter the money to withdraw: "))
acc.withdraw(drawMoney)
depositM = int(input("Enter the money to deposit: "))
acc.deposit(depositM)
#acc.commit()
print("Remaining money is the acount is {} Rs".format(acc.bal))

class AcconInherit(Account):

    def __init__(self,files):
        Account.__init__(self,files)

    def transfer(self,trans):
        self.baltra = self.bal - trans
        with open(self.files, 'w') as file:
            file.write(str(self.baltra))

transIn = AcconInherit("balanced.txt")
moneytrans = int(input("Enter the money to transfer : " ))
transIn.transfer(moneytrans)
print("Remaining amount is Rs. {}".format(transIn.baltra))
