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
    prioridade = input("Prioridade (Baixa / Média / Alta): ")

    tarefa = {
        "id": id_atual,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
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
            Prioridade: {tarefa['prioridade']}
            Status: {tarefa['status']}
            -------------------------
        """)

# Função para edição de tarefa
def atualizar_tarefa():
    print("""
            ===== ATUALIZAR TAREFA =====
        """)
    id_tarefa = int(input("Informe o ID da tarefa a ser atualizada: "))

    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefa["titulo"] = input("Novo título: ")
            tarefa["descricao"] = input("Nova descrição: ")
            tarefa["prioridade"] = input("Nova prioridade: ")
            tarefa["status"] = input("Novo status (Pendente / Concluída): ")
            print("Tarefa atualizada com sucesso!\n")
            return

    print("Tarefa não encontrada.\n")

# Função para excluir tarefa
def excluir_tarefa():
    print("""
            ===== EXCLUIR TAREFA =====
        """)
    id_tarefa = int(input("Informe o ID da tarefa a ser excluída: "))

    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefas.remove(tarefa)
            print("Tarefa excluída com sucesso!\n")
            return

    print("Tarefa não encontrada.\n")


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

if __name__ == "__main__":
    menu()

