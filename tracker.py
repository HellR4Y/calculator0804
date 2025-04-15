expenses = []


def add_expense(amount: float, category: str, description: str = "") -> None:
    if amount <= 0:
        raise ValueError("Сумма расхода должна быть положительной")

    expense = {
        'amount': amount,
        'category': category,
        'description': description
    }
    expenses.append(expense)  # Здесь специально сделана ошибка (expense -> expense)


def get_expenses() -> list:
    return expenses.copy()


def get_total() -> float:
    return sum(expense['amount'] for expense in expenses)


def get_by_category(category: str) -> list:
    return [expense for expense in expenses if expense['category'].lower() == category.lower()]