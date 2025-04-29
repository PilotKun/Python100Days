
#* How are Classes made

class User:
    def __init__(self, user_id, username, followers=0, following=0):
        self.id = user_id
        self.username = username
        self.followers = followers
        self.following = following
    

    def follow(self, user):
        user.followers += 1
        self.following += 1

user1 = User("001", "Keerthi")
user2 = User("002", "Amey")

user1.follow(user2)

print(user1.username, user1.followers)
print(user2.username, user2.followers)



