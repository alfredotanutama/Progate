from atm_card import ATMCard

class Customer:
    def __init__(self,id,custPin=1234,custBalance=10000):
        self.id=id
        self.pin=custPin
        self.balance=custBalance
    
    #untuk verifikasi data
    def checkId(self):
        return self.id
    def checkPin(self):
        return self.pin
    def checkBalance(self):
        return self.balance
    
    #untuk debet kredit
    def WithdrawBalance(self,nominal):
        self.balance-=nominal
    def depositBalance(self,nominal):
        self.balance+=nominal