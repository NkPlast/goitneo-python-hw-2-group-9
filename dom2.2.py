from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(value)

class Record:
    def __init__(self, name, phones=[]):
        self.name = Name(name)
        self.phones = [Phone(phone) for phone in phones]

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for i, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return True
        return False

    def __str__(self):
        phones_str = ', '.join([str(phone) for phone in self.phones])
        return f"Name: {self.name}, Phones: {phones_str}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

# Демонстрация функциональности
book = AddressBook()

# Добавляем записи
john_record = Record("John", ["1234567890"])
jane_record = Record("Jane", ["9876543210"])
book.add_record(john_record)
book.add_record(jane_record)

# Выводим все записи
for record in book.data.values():
    print(record)

# Редактируем телефон
john_record.edit_phone("1234567890", "1112223333")
print("\nAfter editing John's phone:")
print(john_record)

# Удаляем запись
book.delete("Jane")
print("\nAfter deleting Jane:")
for record in book.data.values():
    print(record)
