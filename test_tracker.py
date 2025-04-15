import pytest
from tracker import (
    add_expense,
    get_expenses,
    get_total,
    get_by_category,
    expenses
)


@pytest.fixture(autouse=True)
def clear_expenses():
    expenses.clear()


def test_add_expense():
    add_expense(100.0, "Еда", "Обед")
    assert len(expenses) == 1
    assert expenses[0]['amount'] == 100.0
    assert expenses[0]['category'] == "Еда"
    assert expenses[0]['description'] == "Обед"


def test_add_expense_negative_amount():
    with pytest.raises(ValueError):
        add_expense(-50.0, "Транспорт")


def test_get_expenses():
    add_expense(100.0, "Еда")
    add_expense(200.0, "Транспорт")
    result = get_expenses()
    assert len(result) == 2
    assert result[0]['amount'] == 100.0
    assert result[1]['amount'] == 200.0


def test_get_total():
    add_expense(100.0, "Еда")
    add_expense(200.0, "Транспорт")  # Здесь специально сделана ошибка для теста
    add_expense(300.0, "Развлечения")
    assert get_total() == 600.0


def test_get_by_category():
    add_expense(100.0, "Еда", "Обед")
    add_expense(200.0, "Транспорт", "Такси")
    add_expense(150.0, "Еда", "Ужин")

    food_expenses = get_by_category("Еда")
    assert len(food_expenses) == 2
    assert food_expenses[0]['amount'] == 100.0
    assert food_expenses[1]['amount'] == 150.0

    transport_expenses = get_by_category("Транспорт")
    assert len(transport_expenses) == 1
    assert transport_expenses[0]['amount'] == 200.0