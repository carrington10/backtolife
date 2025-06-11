class bank:
    def __init__(self,name,dob,address,accountn):
         self.name = name
         self.dob= dob
         self.address = address
         self.accountn = accountn

    def listaccountinfo(self):
      return (f"This is your account info \nName:{self.name} \nDob:{self.dob} \nAccount Number:{self.accountn}")    
    


account1 = bank("tom","09/24/2000","san antonio tx","3346597849");
print(account1.listaccountinfo());