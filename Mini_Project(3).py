

class Member():
    def __init__(self,name,member_id,email,phone_number):
        self.name=name
        self.member_id=member_id
        self.email=email
        self.phone_number=phone_number

    def __str__(self):
        return f"Name:{self.name},Member id:{self.member_id},Phone Number:{self.phone_number} is added to System!"

    def update_contact(self,email=None, phone_number=None):
        if email is not None:
            self.email = email
        if phone_number is not None:
            self.phone_number = phone_number

    
      
      
class LibraryMemberManagement():
    def __init__(self,member_list=[]):
        self.member_list=member_list

    def add_member(self,member):
        self.member_list.append(member)
        print(f"{member} has been added to library Memember System!")

    def remove_member(self,member_id):
        found=False
        for id in self.member_list:
            if id.member_id == member_id:
                self.member_list.remove(id)
                print(f"{id} has been found in the system and removed from it!")
                found=True
                break
        if not found:
            print(f"{id} is not found in the system!")

    def display_member(self):
        for member in self.member_list:
            print(f" Name: {member.name}, Member id: {member.member_id},Email: {member.email},Phone Number: {member.phone_number}")

    def search_member(self,name):
        found=False
        for i in self.member_list:
            if i.name == name:
                print(f"{i.name} member found existing.")
                found=True
                break
        if not found:
            print(f"{i.name} not found existing")

    
    def update_member_contact(self,member_id, email=None, phone_number=None):
        found=False
        for i in self.member_list:
            if i.member_id == member_id:
                i.member.update_contact(email=None, phone_number=None)
                found=True
                break
        if not found:
            print(f"{member_id} Not found.Cant update information")




library_member_management=LibraryMemberManagement()

member_1=Member("Can",997,"can1@gmail.com","8406579043")
member_2=Member("Asli",456,"asli@gmail.com","6758974356")
member_3=Member("Tolga",773,"tolga@gmail.com","213896864")


library_member_management.add_member(member_1)
library_member_management.add_member(member_2)
library_member_management.add_member(member_3)

library_member_management.display_member()

library_member_management.remove_member(997)





    









