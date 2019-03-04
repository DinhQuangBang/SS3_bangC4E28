shop = ["T-Shirt", "Sweater"]

while True:
     print ("--- WELCOME TO OUR SHOP ---\n"
            "===========================\n"
            "Choose (C or R or U or D)\n"
            "\n")
     
     chon = str (input ("What do you want ? "))
     
     if (chon == "R"):
         print ("Our Items: ")
         for index, item in enumerate (shop):
             print (index + 1, item, sep= ". ")
     
     
     elif (chon == "C"):
         add = input ("Enter Your Item: ")
         shop.append (add)
         print ("Our item: ") 
         
         for index, item in enumerate (shop):
             print (index + 1, item, sep= ". ") 
     
     
     elif (chon =="U"):
          upp = int (input ("Update position: "))
          upd = input ("New item? ")
          shop [upp-1] = upd
          print ("Our item: ")
          
          for index, item in enumerate (shop):
             print (index + 1, item, sep= ". ")
     
     
     elif (chon == "D"):
         delete = int (input ("Delete position? "))
         del shop[delete - 1]
         print ("Our item: ")  
         
         for index, item in enumerate (shop):
             print (index + 1, item, sep= ". ")   
     
     else:
         print ("YOU ENTERED WRONG. PLEASE RE-ENTER") 


