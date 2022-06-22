
myrun = True
class Atm(object):
    def __init__(self,atm_card_number,pin_number):
        self.atm_card_number = atm_card_number
        self.pin_number = pin_number
    def CashWidrawl(self):
        money = input("Money needed to widraw: ")
        pin = input("Enter pin again: ")
        myrun = True
        if pin == hdfc.pin_number:
            print(money+" Rupees widrawed")
            return True
        else:
            print("Wrong pin entered")
            myrun = False
    
    def BalanceInquiry(self):
        pin = input("Enter pin again: ")
        if pin == hdfc.pin_number:
            print("You have 107051")
        else:
            print("Wrong pin entered")

account_number = input("Please enter account number: ")
pin_original = input("Please enter the pin: ")
hdfc = Atm(account_number,pin_original)
if(myrun):
    yes_no = input("Would you like to widraw cash(Y-Yes,N-No): ")
    if yes_no == "Y":
        hdfc.CashWidrawl()
        yes_no3 = input("Would you like to check your balance(Y-Yes,N-No): ")
        if yes_no3 == "Y":
            hdfc.BalanceInquiry()
            print("Thank you")
            print("Visit again")
        else:
            print("Thank you")
            print("Visit again")
    else:
        yes_no2 = input("Would you like to check your balance(Y-Yes,N-No): ")
        if yes_no2 == "Y":
            hdfc.BalanceInquiry()
            print("Thank you")
            print("Visit again")
        else:
            print("Thank you")
            print("Visit again")