class User:
    def __init__(self, username=None, password=None, profile_picture=None):
        self.username = username
        self.password = password
        self.profile_picture = profile_picture
    
    def to_dict(self):
        return {
            "username": self.username,
            "profile_picture": self.profile_picture
        }

    @classmethod
    def from_dict(cls, data):
        return cls(username=data.get("username"), profile_picture=data.get("profile_picture"))