
from datetime import datetime,timedelta

class Field():
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value

# class Birthday validate birthday entered by user
class Birthday(Field):

    @Field.value.setter
    def value(self, value):
        if value != None:
            if datetime.today().date() >= datetime.strptime(value, "%d.%m.%Y").date():
                self._value = datetime.strptime(value, "%d.%m.%Y").date()
            else:
                print(f"Incorect birthday date, use format dd.mm.yy")

# class Record stores all contacts information
class Record():
    def __init__(self, name, phones = [],mails = [], birthday = None, address = None) -> None:
        self.name = name
        self.phones = phones
        self.mails = mails
        self.address = address
        self.birthday = Birthday(birthday)

    # to see what Record contains
    def __str__(self) -> str:
        return f"Name: {self.name}, Phones: {[phone for phone in self.phones]}, Mails: {[mail for mail in self.mails]}, Birthday: {self.birthday.value}, Address: {self.address}"
    




class PersonalAssistant:
    def __init__(self):
        self.contacts = []
        self.notes = []

    # task_1/ creates Record object and put it in contacts list for later use
    def add_contact(self):
        
        inputs = input('Enter name: ')
        record = Record(inputs)
        inputs = input('Enter phone number: ')
        record.phones.append(inputs)
        inputs = input('Enter maill: ')
        record.mails.append(inputs)
        inputs = input('Enter birthday: ')
        record.birthday = Birthday(inputs)
        inputs = input('Enter address: ')
        record.address = inputs
        self.contacts.append(record)
        
    # task_2/ return a list of contacts whose birthday is after a specified number of days from the current date
    def get_birthdays(self):
        days = int(input('Enter amount of days: '))
        today = datetime.today()
        next_birthday = today.date() + timedelta(days=days)
        for user in self.contacts:
            ignor_year = user.birthday.value.replace(year=today.year) #to ignore year
            if today.date() <= ignor_year <= next_birthday:
                print(f'\n{user.name}, {user.phones}')

        


    def task_3(self):
        3+3


    # task 4
    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        print(f'Contact {name} not found.')
        return None

    # task 5
    def redaction_contact(self, name):
        contact = self.search_contact(name) # проходимся по контактах
        if contact:
            print('Enter new information:')
            new_name = input('Enter new name: ')
            new_phones = input('Enter new phone(s) separated by commas: ').split(',')
            new_mails = input('Enter new email(s) separated by commas: ').split(',')
            new_birthday = input('Enter new birthday, use format dd.mm.yyyy: ')
            new_address = input('Enter new address: ')

            contact.name = new_name
            contact.phone = [phone.strip() for phone in new_phones]
            contact.birthday = Birthday(new_birthday)
            contact.mails = [mail.strip() for mail in new_mails]   
            contact.address = new_address
            print(f'Contact {name} redactioned successfully')

    def delete_contact(self, name):
        contact = self.search_contact(name) #проходимся по контактах
        if contact:
            self.contacts.remove(contact)
            print(f'Contact {name} deleted successfully')


    def task_6(self):
        6+6

    def task_7(self):
        7+7

    def task_8(self):
        8+8

    def task_9(self):
        9+9

    def task_10(self):
        10+10

    def task_11(self):
        11+11





def main():
    assistant = PersonalAssistant()
    while True:
        print("\nВведіть команду (для допомоги введіть 'help'):")
        command = input("> ").lower()

        if command == 'help':
            print("Доступні команди: exit")
        elif command == 'add_contact':
            assistant.add_contact()
        elif command == "birthday_day":
            assistant.get_birthdays()
        elif command == 'search_contact':
            assistant.search_contact()
        elif command == 'redaction_contact':
            assistant.redaction_contact()
        elif command == 'delete_contact':
            assistant.delete_contact()
            
        elif command == 'exit':
            print("До побачення!")
            break

        else:
            print("Невідома команда. Введіть 'help' для списку доступних команд.")

if __name__ == "__main__":
    main()
