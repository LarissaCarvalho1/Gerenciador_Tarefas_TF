import sys
sys.path.append("src")

import main


def setup_function():
    main.tarefas.clear()
    main.id_atual = 1


def test_criar_tarefa(monkeypatch):
    entradas = iter([
        "Estudar Pytest",
        "Criar testes unitários",
        "Alta"
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    main.criar_tarefa()

    assert len(main.tarefas) == 1
    assert main.tarefas[0]["titulo"] == "Estudar Pytest"
    assert main.tarefas[0]["prioridade"] == "Alta"


def test_atualizar_tarefa(monkeypatch):
    main.tarefas.append({
        "id": 1,
        "titulo": "Antigo",
        "descricao": "Desc antiga",
        "prioridade": "Baixa",
        "status": "Pendente"
    })

    entradas = iter([
        "1",
        "Novo título",
        "Nova descrição",
        "Alta",
        "Concluída"
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    main.atualizar_tarefa()

    assert main.tarefas[0]["titulo"] == "Novo título"
    assert main.tarefas[0]["status"] == "Concluída"


def test_excluir_tarefa(monkeypatch):
    main.tarefas.append({
        "id": 1,
        "titulo": "Teste",
        "descricao": "Desc",
        "prioridade": "Média",
        "status": "Pendente"
    })

    monkeypatch.setattr("builtins.input", lambda _: "1")

    main.excluir_tarefa()

    assert len(main.tarefas) == 0
