class Schedule:
    def __init__(self, name, phone, mail, favorite=False):
        self.name = name
        self.phone = phone
        self.mail = mail
        self.favorite = favorite


def create_contacts(schedules):
    name =  input("Digite seu nome:")       
    phone = input("Digite seu telefone:")       
    mail =  input("Digite seu e-mail:")        

    schedules.append(Schedule(name, phone, mail))
    return

def view_all_contacts(schedules, show_only_favorites=False):
    if not schedules:
        print("Nenhum contato encontrado.")
        return
    
    print("\nAgenda:")
    for index, schedule in enumerate(schedules, start=1):
        if show_only_favorites and not schedule.favorite:
            continue

        favorite = "✓" if schedule.favorite else " "
        name = schedule.name
        phone = schedule.phone
        mail = schedule.mail
        print(f"{index}.[{favorite}] Nome: {name}, Telefone: {phone}, E-mail: {mail}")
    return

def edit_contacts(index, schedules):
 try:
    index = int(index) -1

    if 0 <= index < len(schedules):
        print("Editando contato:")

        name = input("Digite o novo nome (ou pressione Enter para manter): ")
        phone = input("Digite o novo telefone (ou pressione Enter para manter): ")
        mail = input("Digite o novo e-mail (ou pressione Enter para manter): ")

        if name:
            schedules[index].name = name
        if phone:
            schedules[index].phone = phone
        if mail:
            schedules[index].mail = mail
        
        print("Contato editado com sucesso!")
    else:
        print("Índice inválido.")
 except ValueError:
        print("O índice fornecido não é um número válido.")
 return

def check_favorite_contacts(index, schedules):
    try:
        index = int(index) -1
        
        if 0 <= index < len(schedules):
            if schedules[index].favorite:
                schedules[index].favorite = False
                print(f"Contato '{schedules[index].name}' desmarcado como favorito!")
            else:
                schedules[index].favorite = True
                print(f"Contato '{schedules[index].name}' marcado como favorito!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("O índice fornecido não é um número válido.")
    return

def delete_contacts(index, schedules):
  try:
    index = int(index) - 1

    if 0 <= index < len(schedules):
            removed_schedule = schedules.pop(index)
            print(f"Contato '{removed_schedule.name}' deletado com sucesso!")
    else:
            print("Índice inválido.")
  except ValueError:
        print("O índice fornecido não é um número válido.")
  return