import random
import json

class BankAccount:
    def open_account(self,kwargs):
        self.name = kwargs["name"]
        self.adhar_no = kwargs["adhar_no"] if "adhar_no" in kwargs else None
        self.pan_no = kwargs["pancard_no"] if "pancard_no" in kwargs else None
        self.address = kwargs["address"]
        self.photo = kwargs["photo"]
        account_no = random.randint(10000000000,99999999999)
        self.account_no = account_no
        data_list = []
        with open("data.json","r",encoding="utf-8") as file:
            data = file.read()
            if len(data)>0:
                data = json.loads(data)
            else:
                data = []
        with open("data.json","w",encoding="utf-8") as file:
            data_dict = {
                "name": self.name,
                "pancard_no": self.pan_no,
                "adhar_no": self.adhar_no,
                "address": self.address,
                "account_no": self.account_no,
                "profile_img":self.photo,
                "balance": 0
            }
            data_list.append(data_dict)
            data.extend(data_list)
            data = json.dumps(data)
            file.write(data)
            return print("your account no is",self.account_no)

    def search_customer(self,account_no ):
        with open("data.json","r",encoding="utf-8") as file:
            data = file.read()
            data = json.loads(data)
            for customer in data:
                if account_no ==customer["account_no"]:
                    return [customer,data]
            else:
                return print("customer not found!")

    def deposite(self,account_no,balance_deposite):
        custmer = self.search_customer(account_no)[0]
        balance = custmer["balance"]
        data = self.search_customer(account_no)[1]
        if balance==None:
            balance = 0
        balance+=float(balance_deposite)
        data[data.index(custmer)]["balance"]=balance
        with open("data.json","w",encoding="utf-8") as file:
            data = json.dumps(data)
            file.write(data)
        return balance

        
            
    def withdrow(self,account_no,balance_withdrow):
        custmer = self.search_customer(account_no)[0]
        balance = custmer["balance"]
        data = self.search_customer(account_no)[1]
        if balance==None:
            balance = 0
        balance-=float(balance_withdrow)
        data[data.index(custmer)]["balance"]=balance
        with open("data.json","w",encoding="utf-8") as file:
            data = json.dumps(data)
            file.write(data)
        return balance

    def check_balance(self,account_no):
        cust_balance = self.search_customer(account_no)[0]
        return cust_balance["balance"]



while True:
    q = str(input("press q for quit:")).upper()


    if q=="Q":
        print("thank you using this program:")
        break
    else:
        choose = int(input(""""
        1 for open account
        2 for deposite in account
        3 for withdrow from account
        4 for checke balance
        enter:"""))
        obj = BankAccount()
        if choose==1:
            name = str(input("name of account holder:"))
            adhar_card = str(input("enter the adhar no:"))
            pancard_no = str(input("Pancard Card No:"))
            address = str(input("Address:"))
            photo = str(input("add link of your photo:"))
            user_input = {
            "name":name,
            "address":address,
            "photo":photo
                    }

            if len(adhar_card)==12 and adhar_card.isdigit()==True:
                user_input["adhar_no"]= adhar_card
            else:
                print("please inter the coreect no")

            if pancard_no[:2].isalpha()==True and pancard_no[3] in ["A","B","C","F","G","H","L","J","P","T"] and pancard_no[5:-1].isdigit()==True and pancard_no[-1].isalpha()==True:
                user_input["pancard_no"]=pancard_no
            else:
                print("please write correct pan card no.")
            obj.open_account(user_input)
       
        elif choose==2:
            account_no = int(input("please enter your account no:"))
            amount = float(input("how mach do you want to deposite:"))
            print(obj.deposite(account_no,amount))
        elif choose==3:
            account_no = int(input("please enter your account no:"))
            amount = float(input("how mach do you want to withdrow:"))
            print(obj.withdrow(account_no,amount))
        elif choose==4:
            account_no = int(input("please enter your account no:"))
            print(obj.check_balance(account_no))
        else:
            print("please enter correct option")

        




