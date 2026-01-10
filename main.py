# Lista que armazenará as tarefas
tarefas = []
id_atual = 1

# Função para criar tarefa
def criar_tarefa():
    global id_atual
    print("""
            ===== CRIAR TAREFA =====
        """)
    titulo = input("Título da tarefa: ")
    descricao = input("Descrição da tarefa: ")

    tarefa = {
        "id": id_atual,
        "titulo": titulo,
        "descricao": descricao,
        "status": "Pendente"
    }

    tarefas.append(tarefa)
    id_atual += 1
    print("Tarefa criada com sucesso!\n")

# Função para listar tarefas
def listar_tarefas():
    if not tarefas:
        print("\nNenhuma tarefa cadastrada.\n")
        return

    print("""
            ===== LISTA DE TAREFAS =====
        """)
    for tarefa in tarefas:
        print(f"""
            ID: {tarefa['id']}
            Título: {tarefa['titulo']}
            Descrição: {tarefa['descricao']}
            Status: {tarefa['status']}
            -------------------------
        """)


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
