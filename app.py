print("""
█▀▄▀█ █▀▀ █░█   █▄▄ █▀█ █░░ █▀ █▀█     ▄▀█ █▄░█ █▀█ ▀█▀ █▀▀   █▀ █▀▀ █░█ █▀   █▀▀ ▄▀█ █▀ ▀█▀ █▀█ █▀
█░▀░█ ██▄ █▄█   █▄█ █▄█ █▄▄ ▄█ █▄█     █▀█ █░▀█ █▄█ ░█░ ██▄   ▄█ ██▄ █▄█ ▄█   █▄█ █▀█ ▄█ ░█░ █▄█ ▄█
""")

def cost_breakdown(list):
    result = 0
    for item in list:  
        if isinstance(item, (int, float, complex)):
            result+= item

    return result

              
def user_input_typeexpense():
    type_expense = input("Descrição (ou ENTER pra fechar): ")
    return type_expense
def user_input_cost():
    cost = (input("Valor: "))
    try: 
        return float(cost)
    except: 
        print('Digite somente numero...')
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
                list.append(type)
                list.append(cost)
                print(list)
            except:
                print('Valores incorretos... Encerrando o programa')

if __name__ == '__main__':
    main()