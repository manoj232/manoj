import base64
class person:
       user=int(input("enter 1 to encrypt 2 to decrypt"))
       if user==1:  
         def encrypt():
             x=input("enter u r mobile  to operate encode and decode")
             z=base64.b64encode(x.encode('utf-8',errors='struct'))
            
             print(z)
         e=encrypt()
        
         
       elif user==2:
           def decrypt():
               y=input("enter u r mobile  to operate encode and decode")
               z=base64.b64decode(y.decode('utf-8',errors='struct'))
               
               print(z)
           d=decrypt()
           
           
       else:
           print("wrong input")
