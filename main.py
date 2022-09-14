import random
import json
class BankAccount:
    def __init__(self,name,aadharcard,pancard,address,photo):
        self.name = name
        self.adhar_no = aadharcard
        self.pan_no = pancard
        self.address = self.address
        self.photo = self.photo

    def open_account(self):
        account_no = random.randint(10000000000,99999999999)
        data_list = []
        with open("data.json","r+") as file:
            data = file.read()
            data = json.loads(data)
            data_list.extend(data)
            

            
            






class Execute:
    pass

