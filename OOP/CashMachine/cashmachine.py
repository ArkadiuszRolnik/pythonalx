class CashMachine:

    def __init__(self):
        self.bills = []

    @property
    def is_available(self):
        if self.bills:
            return True
        return False

    def put_money(self, bills):

        self.bills.extend(bills)

    def withdraw_money(self, amount):
        if self.is_available:
            to_withdraw = []
            for bill in sorted.self.bills, :
                if bill + sum(to_withdraw) <= amount:
                    to_withdraw.append(bill)

                for bill in to_withdraw:
                    self.bills.remove(bill)
                return to_withdraw
        return []

    pass

