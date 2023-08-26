class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("007", "James Bond")
user2 = User("08", "Steven Gerrard")

# user1.follow(user2)
print(user1.following)
