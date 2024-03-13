class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


test1 = User("001", "test")
test1.uid = "uid001"

test2 = User("002", "another_test")
test2.follow(test1)

print(vars(test1))
print(vars(test2))
