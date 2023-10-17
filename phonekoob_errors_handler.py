from custom_exception import *


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except ExistError:
            return "This name is already taken "
        except WrongFormatError:
            return "Sorry only numbers accepted to phone, try again"
        except NotFoundError:
            return f"There no {args[0][0]} in your contacts, please try to add it"
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
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts.keys():
        raise NotFoundError
    if not phone.isdigit():
        raise WrongFormatError
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):  # тре перевріка на "мало даних", "нема контакту"
    if not args:
        raise NeedDataError
    name = args[0]
    if name not in contacts.keys():
        raise NotFoundError
    phone = contacts[name]
    return phone


def get_all(contacts):
    if contacts:
        for name, contact in contacts.items():
            print("Name: {} Phone number: {}".format(name, contact))
    else:
        print("Phone book is empty, you need more friend less code in your life")


def main():
    contacts = {}
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
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
