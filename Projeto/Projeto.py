alunos = {}
cursos = {}
matriculas = {}

def cadastrar_aluno():
    id_aluno = input("ID do aluno: ")
    nome = input("Nome do aluno: ")
    if id_aluno in alunos:
        print("Aluno já cadastrado.")
    else:
        alunos[id_aluno] = nome
        print("Aluno cadastrado com sucesso!")

def cadastrar_curso():
    id_curso = input("ID do curso: ")
    nome = input("Nome do curso: ")
    if id_curso in cursos:
        print("Curso já cadastrado.")
    else:
        cursos[id_curso] = nome
        print("Curso cadastrado com sucesso!")

def listar_alunos():
    print("\n--- Alunos Cadastrados ---")
    for id, nome in alunos.items():
        print(f"{id}: {nome}")

def listar_cursos():
    print("\n--- Cursos Cadastrados ---")
    for id, nome in cursos.items():
        print(f"{id}: {nome}")

def matricular_aluno():
    id_aluno = input("ID do aluno: ")
    id_curso = input("ID do curso: ")
    if id_aluno not in alunos:
        print("Aluno não encontrado.")
        return
    elif id_curso not in cursos:
        print("Curso não encontrado.")
        return
    elif id_aluno not in matriculas:
        matriculas[id_aluno] = []
    elif id_curso in matriculas[id_aluno]:
        print("Aluno já está matriculado nesse curso.")
    else:
        matriculas[id_aluno].append(id_curso)
        print("Aluno matriculado com sucesso!")

def listar_matriculas():
    print("\n--- Matrículas ---")
    for id_aluno, cursos_ids in matriculas.items():
        nome_aluno = alunos.get(id_aluno)
        nomes_cursos = [cursos[cid] for cid in cursos_ids]
        print(f"{nome_aluno} está matriculado em: {', '.join(nomes_cursos)}")

def menu():
    while True:
        print("\n=== Sistema de Cadastro de Alunos e Cursos ===")
        print("1. Cadastrar Aluno")
        print("2. Cadastrar Curso")
        print("3. Listar Alunos")
        print("4. Listar Cursos")
        print("5. Matricular Aluno em Curso")
        print("6. Listar Matrículas")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            cadastrar_curso()
        elif opcao == "3":
            listar_alunos()
        elif opcao == "4":
            listar_cursos()
        elif opcao == "5":
            matricular_aluno()
        elif opcao == "6":
            listar_matriculas()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()

