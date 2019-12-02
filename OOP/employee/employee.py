class Employee:

    def __init__(self, f_name, l_name, rph):

        self.first_name = f_name
        self.last_name = l_name
        self.rate_per_hour = rph
        self.registered_hours = 0 # to trzeba zainicjować

    def register_time(self, time):
        self.registered_hours = time

    def pay_salary(self):
        if self.registered_hours <= 8:

            to_pay = self.registered_hours * self.rate_per_hour
        else:
            to_pay = 8 * self.rate_per_hour + (self.registered_hours - 8) * self.rate_per_hour * 2
        self.registered_hours = 0
        return to_pay

