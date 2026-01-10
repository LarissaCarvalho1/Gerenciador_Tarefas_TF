# Lista que armazenará as tarefas
tarefas = []
id_atual = 1


def menu():
    while True:
        print("""
            ===== GERENCIADOR DE TAREFAS =====
            1 - Criar tarefa
            2 - Listar tarefas
            3 - Atualizar tarefa
            4 - Excluir tarefa
            0 - Sair
        """)

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            criar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            atualizar_tarefa()
        elif opcao == "4":
            excluir_tarefa()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida.\n")

menu()
