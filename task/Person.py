from datetime import datetime, date
class Person:
    def __init__(self, surname, first_name, birth_date, nick_name = ''):
        self.surname = surname
        self.first_name = first_name
        if nick_name == '':
            self.nick_name = first_name
        else:
            self.nick_name = nick_name
        date_format = "%Y-%m-%d"
        datetime_object = datetime.strptime(birth_date, date_format)
        self.birth_date = datetime_object.date()
    def get_age(self):
        today = date.today()
        delta_in_days = today - self.birth_date
        return int(delta_in_days.days / 365.25)

    def get_fullname(self):
        return "{0} {1}".format(self.surname, self.first_name)
petroff = Person("Petrov", "Petro", "1952-01-02")
print(petroff.surname)
print(petroff.first_name)
print(petroff.first_name)
print(petroff.nick_name)
print(petroff.birth_date)
print(petroff.get_fullname())
print(petroff.get_age())
