class User:

    def __init__(self, user_id, name):
        print("new user being created ")
        self.id = user_id
        self.username = name


user_1, user_2 = User("001", "Eric Qiu"), User("002", "Daniel Park")

print(user_1.username)
print(user_2.id)