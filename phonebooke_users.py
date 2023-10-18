import re
from collections import UserDict
from celebration_calendar import get_birthdays_per_week  # але треба реворкнути
from datetime import datetime
from custom_exception import *


class Field:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.value}"


class Name(Field):
    def __init__(self, name):
        self.value = name.title()


class Birthday(Field):
    def __init__(self, value):
        if re.search("\d{2}.\d{2}.\d{4}", value):
            self.value = value
        else:
            raise DateFormatError()


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
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

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

    # Реалізовано метод find, який знаходить запис за ім'ям.
    def find(self, name):
        for key, record in self.data.items():
            if key == name.title():
                return record

    # Реалізовано метод delete, який видаляє запис за ім'ям.
    def delete(self, name):
        for record in self.data.values():
            if record.name.value == name.title():
                self.data.pop(name)
                print("Succes delete")
                break

    def show_birthday(self, name):
        return self[name].birthday.value

    #        for key, record in self.data.items():
    #            if key == name.title():
    #                if record.birthday:
    #                    print(f"{name}'s Birthday at {record.birthday.value}")
    #                    return record.birthday.value
    #                else:
    #                    print(f"{name} birthday is not added")
    #                    return None

    def birthdays(self):
        birthdays_list = []
        for key, record in self.items():
            if record.birthday:
                dateTimeObj = datetime.strptime(record.birthday.value, "%d.%m.%Y")
                birthdays_list.append(
                    {"name": key, "birthday": dateTimeObj},
                )

        get_birthdays_per_week(birthdays_list)


book = AddressBook()
if __name__ == "__main__":
    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    # Пошук конкретного телефону у записі John
    john.add_birthday("19.10.2023")

    print(f"{john.name}: Birth {john.birthday}")  # Виведення: 5555555555

    book.show_birthday("John")
    # Видалення запису Jane
    book.birthdays()
