# Програма повинна мати функцію main(), яка управляє основним циклом обробки команд.
# Реалізуйте функцію parse_input(), яка розбиратиме введений користувачем рядок на команду та її аргументи. Команди та аргументи мають бути розпізнані незалежно від регістру введення.
# Ваша програма повинна очікувати на введення команд користувачем та обробляти їх за допомогою відповідних функцій. В разі введення команди "exit" або "close", програма повинна завершувати виконання.
# Напишіть функції обробники для різних команд, такі як add_contact(), change_contact(), show_phone() тощо.
# Використовуйте словник Python для зберігання імен і номерів телефонів. Ім'я буде ключем, а номер телефону – значенням.
# Ваша програма має вміти ідентифікувати та повідомляти про неправильно введені команди.

# також додав завантаження та зберігання у файл

from pathlib import Path


def get_contact_filepath():
    datapath = Path("./data/contacts.dat")
    if not datapath.exists():
        with open(datapath, "w+"):
            return datapath

    return datapath


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    try:
        name, phone = args
    except ValueError:
        print("invalid params. The correct is add ContactName phoneNo")
        return
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    try:
        name, phone = args
    except ValueError:
        print("invalid params. The correct is: change ContactName phoneNo")
        return
    contacts[name] = phone
    return "Contact changed."


def remove_contact(args, contacts):
    try:
        name = args
    except ValueError:
        print("invalid params. The correct is: remove ContactName")
        return
    contacts.pop(name)
    return "Contact removed."


def show_contacts(contacts):
    maxlen = 10
    for name in contacts.keys():
        if len(name) > maxlen:
            maxlen = len(name)
    maxlen += 2
    print(f"{'Contact Name':{maxlen}} \t Phone number")
    for name in contacts.keys():
        print(f"{name:{maxlen}} \t {contacts[name]}")


def get_allowed_commands():
    return ["close", "exit", "add", "change", "remove", "show", "phone"]


def save_contacts(contacts, path):
    with open(path, "w") as file:
        for name in contacts.keys():
            file.write(f"{name};{contacts[name]}\n")


def load_contacts(path):
    contacts = {}
    with open(path, "r") as file:
        for contactline in file.readlines():
            contacts[contactline.split(";")[0]] = contactline.split(";")[1].strip()
    return contacts


def get_phone(args, contacts):
    try:
        name = args
    except ValueError:
        print("invalid params. The correct is: phone ContactName")
        return
    if contacts.keys().__contains__(name):
        print(contacts[name])
    else:
        print(f"Contact with name {name} is not found.")


def main():
    contacts = load_contacts(get_contact_filepath())
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "close":
                print("Good bye!")
                save_contacts(contacts, get_contact_filepath())
                break
            case "exit":
                print("Good bye!")
                save_contacts(contacts, get_contact_filepath())
                break
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "remove":
                print(remove_contact(args, contacts))
            case "show":
                show_contacts(contacts)
            case "phone":
                get_phone(args, contacts)
            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()
