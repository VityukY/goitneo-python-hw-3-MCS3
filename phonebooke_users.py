from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.value}"


class Name(Field):
    def __init__(self, name):
        self.value = name.title()


class Phone(Field):
    def __init__(self, value):
        if len(value) == 10 and value.isdigit():
            self.value = value
        else:
            raise ValueError()


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        print("new user record created")

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                print("Phone deleted")

    def edit_phone(self, old_phone, new_phone):
        cur_index = None
        for p in self.phones:
            if p.value == old_phone:
                cur_index = self.phones.index(p)
                new_phone = Phone(new_phone)
                self.phones.insert(cur_index, new_phone)
                self.phones.remove(p)
                print("Phone edited")

    def find_phone(self, search_phone):
        res = None
        for phone in self.phones:
            if phone.value == search_phone:
                res = phone
        return res

    def __repr__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    # Реалізовано метод add_record, який додає запис до self.data.
    def add_record(self, contact):
        self.data[contact.name.value] = contact
        print("record added to address book")

    # Реалізовано метод find, який знаходить запис за ім'ям.
    def find(self, name):
        for name, record in self.data.items():
            if name == name.title():
                return record

    # Реалізовано метод delete, який видаляє запис за ім'ям.
    def delete(self, name):
        for record in self.data.values():
            if record.name.value == name.title():
                self.data.pop(name)
                print("Succes delete")
                break

    # Створення нової адресної книги


book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)
# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555


# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555


# Видалення запису Jane
book.delete("Jane")
