import json


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def print_user(self):
        print('username = %s, password = %s' % (self.username, self.password))

    def user_json(self):
        result = {'username': self.username, 'password': self.password}
        print(result)
        return json.dumps(result, ensure_ascii=False)
