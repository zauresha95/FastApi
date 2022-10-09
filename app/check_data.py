
import schemas
import models
import re
class Check_Client():
    def check_email(email: str):
        if re.match('(\w|\.)+\@+[a-zA-Z]+\.[a-zA-Z]+',email):
            return True
        return False

    def check_phone(phone: int):
        if re.match('7[0-9]+',str(phone)) and len(str(phone)) == 11:
            return True
        return False  