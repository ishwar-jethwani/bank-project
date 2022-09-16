from curses.ascii import isalpha, isdigit
import random
import json
class BankAccount:
    def __init__(self,name,aadharcard,pancard,address,photo):
        self.name = name
        self.adhar_no = aadharcard
        self.pan_no = pancard
        self.address = address
        self.photo = photo

    def open_account(self):
        account_no = random.randint(10000000000,99999999999)
        self.account_no = account_no
        data_list = []
        with open("data.json","r") as file:
            data = file.read()
            if len(data)>0:
                data = json.loads(data)
            else:
                data = []
        with open("data.json","w") as file:
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
    

name = str(input("name of account holder:"))
adhar_card = str(input("enter the adhar no:"))
if len(adhar_card)==12 and adhar_card.isdigit()==True:
    pass
else:
    print("please inter the coreect no")
pancard_no = str(input("Pancard Card No:"))

a = "APGPJ1234O"
if pancard_no[:2].isalpha()==True and pancard_no[3] in ["A","B","C","F","G","H","L","J","P","T"] and pancard_no[5:-1].isdigit()==True and pancard_no[-1].isalpha()==True:
    pass
else:
    print("please write correct pan card no.")


obj = BankAccount("ishwar","123456789","Smaya011","akjjbdfbjh","https://randomuser.me/api/portraits/thumb/men/0.jpg")
obj.open_account()

