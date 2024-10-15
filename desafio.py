
schedules = []
import schedule

while True:
    print("\nAgenda:")
    print("1. Salvar contatos")
    print("2. Visualizar contatos")
    print("3. Visualizar favoritos")
    print("4. Editar contatos")
    print("5. Marcar/Desmarcar contatos favoritos")
    print("6. Deletar contatos")
    print("7. Sair")

    choice = input("Digite sua escolha\n")
    if choice == "1":
        schedule.create_contacts(schedules)
    elif choice == "2":
        schedule.view_all_contacts(schedules)
    elif choice == "3":
         schedule.view_all_contacts(schedules,show_only_favorites=True) 
    elif choice == "4":
        schedule.view_all_contacts(schedules)
        index_schedule = input("Digite numero da agenda que deseja atualizar\n")
        schedule.edit_contacts(index_schedule, schedules)
    elif choice == "5":
        schedule.view_all_contacts(schedules)
        index_schedule = input("Digite numero da agenda que deseja marcar/desmarcar\n")
        schedule.check_favorite_contacts(index_schedule, schedules)
    elif choice == "6":
        schedule.view_all_contacts(schedules)
        index_schedule = input("Digite numero da agenda que deseja remover\n")
        schedule.delete_contacts(index_schedule, schedules)
    elif choice == "7":
        break

    print("\nPrograma finalizado")