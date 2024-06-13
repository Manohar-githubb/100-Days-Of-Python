# Creating a class
# class User:
#     pass        #pass is used to pass to next lines of code.
# user_1=User()   #create an object
# user_1.id="001"
# user_1.username="Manu"
# print(user_1.id)
# print(user_1.username)

#creating a constructor
# class User:
#     def __init__(self):
#         print("Here is the constructor created")     # This will be printed twice because there are two objects created under same class    
# user_1=User()   
# user_1.id="001"
# user_1.username="Manu"
# print(user_1.id)
# print(user_1.username)
# user_2=User()   
# user_2.id="002"
# user_1.name="Manohar"

#Accessing an attritude
# class User:
#     def __init__(self,user_id,username):
#         self.id=user_id
#         self.username=username     
# user_1=User("001","Manu")   
# print(user_1.id)
# print(user_1.username)

#we can also create an empty attritude without passing it and can make it work
# class User:
#     def __init__(self,user_id,username):
#         self.id=user_id
#         self.username=username
#         self.followers=0     
# user_1=User("001","Manu") 
# print(user_1.followers)      #This line will be printed succesfully

#Adding methods to a class
# class User:
#     def __init__(self,user_id,username):
#         self.id=user_id
#         self.username=username
#         self.followers=0 
#         self.following=0
#     def follow(self,user):
#         user.followers+=1
#         self.following+=1
            
# user_1=User("001","Manu")
# user_2=User("002","Anjana")
# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)