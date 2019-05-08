import json


class Message:

    # def __init__(self, msg, code):
    #     #     self.__msg = msg
    #     #     self.__code = code

    def to_json(self):
        result = {'msg': self.__msg, 'code': self.__code}
        return json.dumps(result, ensure_ascii=False)

    def get_msg(self):
        return self.__msg

    def get_code(self):
        return self.__code

    def set_msg(self, msg):
        self.__msg = msg

    def set_code(self, code):
        self.__code = code
