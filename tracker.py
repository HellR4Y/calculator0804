expenses = []


def add_expense(amount: float, category: str, description: str = "") -> None:
    """
    Добавляет новый расход в список расходов.

    Args:
        amount (float): Сумма расхода
        category (str): Категория расхода
        description (str, optional): Описание расхода. По умолчанию "".
    """
    if amount <= 0:
        raise ValueError("Сумма расхода должна быть положительной")

    expense = {
        'amount': amount,
        'category': category,
        'description': description
    }
    expenses.append(expense)  # Здесь специально сделана ошибка (expense -> expense)


def get_expenses() -> list:
    """
    Возвращает список всех расходов.

    Returns:
        list: Список словарей с расходами
    """
    return expenses.copy()


def get_total() -> float:
    """
    Возвращает общую сумму всех расходов.

    Returns:
        float: Общая сумма расходов
    """
    return sum(expense['amount'] for expense in expenses)


def get_by_category(category: str) -> list:
    """
    Возвращает расходы только по указанной категории.

    Args:
        category (str): Категория для фильтрации

    Returns:
        list: Отфильтрованный список расходов
    """
    return [expense for expense in expenses if expense['category'].lower() == category.lower()]