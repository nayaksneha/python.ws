from contact import Contact
from beautifultable import BeautifulTable
class Inmmry:


    contact_lst = [] #class varible

    @classmethod
    def addContact(cls):
        name = input("enter the name")
        email = input("enter the email")
        mobile = input("enter the mobile")
        addr = input("enter the address")
        cls.contact_lst.append(Contact(name,email,mobile,addr))
        print(f"contact is added successfully with name:{name}")

    @classmethod
    def deleteContact(cls):
        name = input("enter the name")
        contact = cls.get_contact_by_name(name)
        if contact:
            cls.contact_lst.remove(contact)
            print(f"contact {name} is deleted succesfully")
            Inmmry._paint(cls.contact_lst)
        else:
            print(f"contact with name :{name} is not found")


        

    @classmethod
    def searchContact(cls):
        
        if len(cls.contact_lst) > 0:
            name = input("enter name to search")
            s_lst = list(filter(lambda x:name.lower() in x.get__name().lower(),cls.contact_lst))
            if len(s_lst) >0:
                Inmmry._paint(s_lst)
            else:
                print(f"there is no data found with the given search")
        else:
            print(f"contact book is empty...!")

    
    @classmethod
    def updateContact(cls):
        name = input("enter the name to update")
        contact = cls.get_contact_by_name(name)
        if contact:
            print("1.name 2.email 3.mobile 4.address")
            ch = int(input("enter the choice"))
            if ch == 1:
                print(f"old name:{contact.get__name()}")
                name = input("enter the new name:")
                if name:
                    contact.set__name(name)
            elif ch==2:
                print(f"old email :{contact.get__email()}")
                email = input("enter the new email")
                if email:
                    contact.set__email(email)
            elif ch == 3:
                print(f"old mobile : {contact.get__mobile()}")
                mobile = input("enter new mobile")
                if mobile:
                    contact.set__mobile(mobile)
            elif ch == 4:
                print(f"old address :{contact.get__addr()}")
                addr = input("enter new address")
                if addr:
                    contact.set__addr(addr)
        


    @classmethod
    def viewContact(cls):
        Inmmry._paint(cls.contact_lst)

    @staticmethod
    def _paint(lst):
        if len(lst)!= 0:
            table = BeautifulTable()
            table.column_headers = ["name","email","mobile","address"]
            for c in lst:
                table.append_row([c.get__name(),c.get__email(),c.get__mobile(),c.get__addr()])
            print(table)
        else:
            print("contact book is empty!")

    @classmethod
    def get_contact_by_name(cls,name):
        if len(cls.contact_lst)>0:
            contact = list(filter(lambda x:x.get__name().lower() == name.lower(),cls.contact_lst))
        return contact[0] if contact else None

