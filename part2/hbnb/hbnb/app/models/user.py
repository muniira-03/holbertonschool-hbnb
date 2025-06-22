class User:
    def __init__(self, id, email, password, first_name=None, last_name=None):
        self.id = id
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
