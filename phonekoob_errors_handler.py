from custom_exception import *
from phonebooke_users import *


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Please use correct formats, for name - letters, for numbers - ten digits), for dates - DD.MM.YYYY, thank you."
        except ExistError:
            return "This name is already taken "
        except WrongFormatError:
            return "Sorry only numbers accepted to phone, try again"
        except ChangePhoneError:
            return "For changing phone please give data in tex format 'Name Old_phone New_phone' "
        except NotFoundError:
            return (
                f"There no {args[0][0].title()} in your contacts, please try to add it"
            )

        except DateFormatError:
            return "Birthday date must be in format DD.MM.YYYY"
        except NeedDataError:
            return "Please give name for search"

    return inner


@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts.keys():
        raise ExistError
    if not phone.isdigit():
        raise WrongFormatError
    record = Record(name)
    record.add_phone(phone)
    contacts.add_record(record)
    return f"Contact {record.name.value} added."


@input_error
def change_contact(args, contacts):
    name, phone_old, phone_new = args

    if name.title() not in contacts.keys():
        raise NotFoundError
    if not phone_new.isdigit() or not phone_old.isdigit():
        raise ChangePhoneError
    record = contacts.find(name)
    record.edit_phone(phone_old, phone_new)
    return f"Contact {record.name.value} updated."


@input_error
def show_phone(args, contacts):  # тре перевріка на "мало даних", "нема контакту"
    if not args:
        raise NeedDataError
    name = args[0].title()
    if name not in contacts.keys():
        raise NotFoundError
    record = contacts.find(name)
    # phone = record.phones[0].value
    return f"{record.name.value} phone: {record.phones[0].value}"


@input_error
def get_all(contacts):
    if contacts:
        for name, record in contacts.items():
            print("Name: {} Phone number: {}".format(name, record.phones[0].value))
    else:
        print("Phone book is empty, you need more friend and less code")


@input_error
def add_birthday(args, contacts):
    name, birthday = args
    if name.title() not in contacts.keys():
        raise NotFoundError
    record = contacts.find(name)
    record.add_birthday(birthday)
    return f"{record.birthday.value} was added as birthday for {record.name.value}"


@input_error
def show_birthday(args, contacts):
    if not args:
        raise NeedDataError
    name = args[0].title()
    if name not in contacts.keys():
        raise NotFoundError
    record = contacts.find(name)
    if record.birthday:
        return f"{record.name.value} birthday: {record.birthday.value}"
    else:
        return f"There is not bithday for {record.name.value}"


def birthdays(contatcts):
    contatcts.birthdays()


def main():
    contacts = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            get_all(contacts)
        elif command == "add-birthday":
            print(add_birthday(args, contacts))
        elif command == "show-birthday":
            print(show_birthday(args, contacts))
        elif command == "birthdays":
            birthdays(contacts)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
