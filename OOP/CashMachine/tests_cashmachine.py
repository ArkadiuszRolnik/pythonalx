from cashmachine import CashMachine

def test_create_cashmachine():
    cm = CashMachine()
    assert True

def test_cash_machine_is_not_available_when_there_is_no_bills():
    cm = CashMachine()
    assert cm.is_available is False

def test_cash_machine_is_available_after_put_money():
    cm = CashMachine()
    cm.put_money([100, 100, 200, 50])
    assert cm.is_available is True

def test_cash_machine_withdraw_money():
    cm = CashMachine()
    assert cm.withdraw_money(100) == []
    cm.put_money([100])
    assert cm.withdraw_money(100) == [100]
    cm.put_money([50, 50])
    assert cm.withdraw_money(100) == [50, 50]
    cm.put_money([50, 50, 50])
    assert cm.withdraw_money(100) == [50, 50]
    cm.put_money([100])

