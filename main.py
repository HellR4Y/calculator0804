from tracker import (
    add_expense,
    get_expenses,
    get_total,
    get_by_category
)

def display_menu():
    print("\nКалькулятор расходов")
    print("1. Добавить расход")
    print("2. Показать все расходы")
    print("3. Показать общую сумму")
    print("4. Фильтр по категории")
    print("5. Выход")

def main():
    while True:
        display_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            try:
                amount = float(input("Введите сумму: "))
                category = input("Введите категорию: ")
                description = input("Введите описание (необязательно): ")
                add_expense(amount, category, description)
                print("Расход успешно добавлен!")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "2":
            all_expenses = get_expenses()  # Здесь специально сделана ошибка для отладки
            if not all_expenses:
                print("Нет расходов для отображения")
            else:
                for idx, expense in enumerate(all_expenses, 1):
                    print(f"{idx}. {expense['category']}: {expense['amount']} руб. - {expense['description']}")

        elif choice == "3":
            total = get_total()
            print(f"Общая сумма расходов: {total} руб.")

        elif choice == "4":
            category = input("Введите категорию для фильтра: ")
            filtered = get_by_category(category)
            if not filtered:
                print(f"Нет расходов в категории '{category}'")
            else:
                for idx, expense in enumerate(filtered, 1):
                    print(f"{idx}. {expense['amount']} руб. - {expense['description']}")

        elif choice == "5":
            print("Выход из программы")
            break

        else:
            print("Неверный ввод, попробуйте еще раз")

if __name__ == "__main__":
    main()