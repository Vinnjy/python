import pickle


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display(self):
        print(f"User: {self.name}, Email: {self.email}\n")


user = User("Alex", "alex@mail.ru")

# Сериализация (сохранение в файл)
with open("user.txt", "wb") as f:
    pickle.dump(user, f)

# Десериализация (загрузка из файла)
with open("user.txt", "rb") as f:
    loaded_user = pickle.load(f)

loaded_user.display()