def cost_breakdown(expenses):
    return sum(item["cost"] for item in expenses)


def user_input_typeexpense():
    return input("Descrição do gasto (ENTER para encerrar): ").strip()


def user_input_cost():
    while True:
        entrada = input("Valor (ex.: 25,90): ").strip().replace(",", ".")
        try:
            valor = float(entrada)
        except ValueError:
            print("Digite um valor numérico.")
            continue
        if valor <= 0:
            print("O valor precisa ser maior que zero.")
            continue
        return valor


def user_input_category():
    while True:
        categoria = input("Categoria: ").strip()
        if categoria:
            return categoria
        print("A categoria não pode ficar vazia.")


def registration_form(description, cost, cost_category):
    return {
        "description": description,
        "cost": cost,
        "costCategory": cost_category,
    }


def show_expenses(expenses):
    if not expenses:
        print("Nenhum gasto registrado.")
        return
    for item in expenses:
        print(
            f"{item['description']} — R$ {item['cost']:.2f} "
            f"({item['costCategory']})"
        )


def show_summary(expenses):
    if not expenses:
        print("Nenhum gasto registrado.")
        return

    total = cost_breakdown(expenses)
    totals_by_category = {}
    for item in expenses:
        category = item["costCategory"]
        totals_by_category[category] = totals_by_category.get(category, 0) + item["cost"]

    print(f"Total gasto: R$ {total:.2f}")
    print("Por categoria:")
    for category, amount in sorted(totals_by_category.items()):
        print(f"- {category}: R$ {amount:.2f}")


def main():
    expenses = []
    print("MEU BOLSO — controle simples de gastos")

    while True:
        description = user_input_typeexpense()
        if not description:
            break

        cost = user_input_cost()
        category = user_input_category()
        expenses.append(registration_form(description, cost, category))
        print("Gasto registrado.")

    print("\nGastos:")
    show_expenses(expenses)
    print()
    show_summary(expenses)


if __name__ == "__main__":
    main()
