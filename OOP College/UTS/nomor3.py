class BankAccount: #Class
    total_accounts = 0 #Class Variable

    def __init__(self, account_name, balance):
        self.account_name = account_name #Instance Variable
        self.__balance = balance #Encapsulation

        #Memperbarui class variable ketika instance baru dibuat
        BankAccount.total_accounts += 1 

    #Method
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} berhasil disetorkan ke {self.account_name}. Saldo sekarang : {self.__balance}")
        else:
            print("Jumlah setoran harus lebih dari 0")
        
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} berhasil dikeluarkan dari {self.account_name}. Saldo sekarang : {self.__balance}")
        else:
            print("Jumlah penarikan tidak valid atau saldo tidak cukup")
        
    def get_balance(self):
        return self.__balance
    
    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts

#Object
account1 = BankAccount("Pak Bambang", 3000)
account2 = BankAccount("Pak Yusuf", 4000)


print(f"Total Duit Pak Bambang : {account1.get_balance()}")
print(f"Total Duit Pak Yusuf : {account2.get_balance()}")
print(f"Total Akun Bank : {BankAccount.get_total_accounts()}")

account1.deposit(600)
account2.withdraw(500)

print(f"Total Duit Pak Bambang : {account1.get_balance()}")
print(f"Total Duit Pak Yusuf : {account2.get_balance()}")
print(f"Total Akun Bank : {BankAccount.get_total_accounts()}")
