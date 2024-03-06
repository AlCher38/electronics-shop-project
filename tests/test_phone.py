from src.phone import Phone
import pytest

@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)

def test_phone_attributes(phone):
    assert phone.name == "iPhone 14"
    assert phone.price == 120_000
    assert phone.quantity == 5
    assert phone.number_of_sim == 2

def test_phone_repr(phone):
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"

def test_phone_addition(phone):
    phone2 = Phone("Samsung", 80_000, 3, 1)
    assert phone + phone2 == 8

def test_phone_addition_invalid_type(phone):
    with pytest.raises(TypeError) as e:
        phone + 10

    assert str(e.value) == "Unsupported operand types"
