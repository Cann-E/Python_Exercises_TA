

class Member():
    def __init__(self,name,member_id,email,phone_number):
        self.name=name
        self.member_id=member_id
        self.email=email
        self.phone_number=phone_number

    def __str__(self):
        return f"Name: {self.name}, Member ID: {self.member_id}, Email: {self.email}, Phone: {self.phone_number}"


    def update_contact(self,email=None, phone_number=None):
        if email is not None:
            self.email = email
        if phone_number is not None:
            self.phone_number = phone_number

    
      
      
class LibraryMemberManagement():
    def __init__(self, member_list=None):
        if member_list is None:
            member_list = []
        self.member_list = member_list


    def add_member(self,member):
        self.member_list.append(member)
        print(f"{member} has been added to library Memember System!")

    def remove_member(self, member_id):
        found = False
        for member in self.member_list:
            if member.member_id == member_id:
                self.member_list.remove(member)
                print(f"{member.name} has been found in the system and removed from it!")
                found = True
                break
        if not found:
            print(f"Member ID {member_id} is not found in the system!")


    def display_member(self):
        for member in self.member_list:
            print(f" Name: {member.name}, Member id: {member.member_id},Email: {member.email},Phone Number: {member.phone_number}")

    def search_member(self,name):
        found=False
        for i in self.member_list:
            if i.name == name:
                print(f"{name} member found existing.")
                found=True
                break
        if not found:
            print(f"{name} not found existing")

    
    def update_member_contact(self,member_id, email=None, phone_number=None):
        found=False
        for i in self.member_list:
            if i.member_id == member_id:
                i.update_contact(email, phone_number)
                print(f"{i.name} is updated with new email and phone number.")
                found=True
                break
        if not found:
            print(f"Member ID {member_id} not found in the system. Cannot update contact information.")




library_member_management=LibraryMemberManagement()

member_1=Member("Can",997,"can1@gmail.com","8406579043")
member_2=Member("Asli",456,"asli@gmail.com","6758974356")
member_3=Member("Tolga",773,"tolga@gmail.com","213896864")


library_member_management.add_member(member_1)
library_member_management.add_member(member_2)
library_member_management.add_member(member_3)

library_member_management.display_member()

library_member_management.remove_member(997)
library_member_management.remove_member(67)



library_member_management.search_member("Tolga")
library_member_management.search_member("Can")

library_member_management.update_member_contact(456,"aslinewemail@gmail.com","11111111111")
library_member_management.update_member_contact(997,"cannewemail@gmail.com","2222222")








    









