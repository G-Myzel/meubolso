print("""
█▀▄▀█ █▀▀ █░█   █▄▄ █▀█ █░░ █▀ █▀█     ▄▀█ █▄░█ █▀█ ▀█▀ █▀▀   █▀ █▀▀ █░█ █▀   █▀▀ ▄▀█ █▀ ▀█▀ █▀█ █▀
█░▀░█ ██▄ █▄█   █▄█ █▄█ █▄▄ ▄█ █▄█     █▀█ █░▀█ █▄█ ░█░ ██▄   ▄█ ██▄ █▄█ ▄█   █▄█ █▀█ ▄█ ░█░ █▄█ ▄█
""")

def cost_breakdown(list):
    result = 0
    for item in list:  
            result += item['cost']

    return result

              
def user_input_typeexpense():
    type_expense = input("Descrição (ou ENTER pra fechar): ")
    return type_expense
def user_input_cost():
    while True:
        cost = input("Valor: ")
        try:
            return float(cost)
        except ValueError:
            print('Digite somente numero...')

def user_input_category():
    cost_type = input("Digite a descrição do gasto: ")
    return cost_type
def registration_form(description, cost, costCategory):
    registered_obj = {"description": description, "cost": cost, "costCategory": costCategory}
    return registered_obj

def main ():
    list = []
    while True:   
        type = user_input_typeexpense()
        if type == '':
            if len(list) > 0:
                print(f'Voce gastou R${cost_breakdown(list):.2f}')
            break
        else: 
            try: 
                cost = user_input_cost()
                category = user_input_category()
                list.append(registration_form(type, cost, category))
                for item in list:
                    print(f'{item['description']} - {item['cost']} - {item['costCategory']}')
                
            except ValueError:
                print('Valores incorretos.  .. Encerrando o programa')
                return
        cost_breakdown(list)

if __name__ == '__main__':
    main()