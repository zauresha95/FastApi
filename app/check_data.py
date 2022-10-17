
import FastApi.app.schemas
import FastApi.app.models
import re
class Check_Client():
    def check_email(email: str):
        if re.match('(\w|\.)+\@+[a-zA-Z]+\.[a-zA-Z]+',email):
            return True
        return False

    def check_phone(phone: int):
        if re.match('7\d{10}',str(phone)):
            return True
        return False  