class Aluno:
    def __init__(self, nome, idade, matricula, curso, nota):
        self.nome      = nome
        self.idade     = idade
        self.matricula = matricula
        self.curso     = curso
        self.nota      = nota

    def __str__(self):
        return f"nome {self.nome} | idade {self.idade} | matricula {self.matricula} | curso {self.curso} | nota {self.nota}"

alunos = []

def menu():
    print(f"===== Menu Do Crud De Alunos =====\n1 - Cadastrar Alunos\n2 - Listar Alunos\n3 - Atalizar Lista\n4 - Remover Aluno\n5 - Buscar por nome\n0 - Sair")

def cadastrar():
    nome      = input("Nome: ")
    idade     = input("idade: ")
    matricula = input("matricula: ")
    curso     = input("curso: ")
    nota      = input("nota: ")
    aluno     = Aluno(nome, idade, matricula, curso, nota)
    alunos.append(aluno)
    print ("Aluno cadastrado com sucesso!!")

def listar():
    if not alunos:
       print("Nenhum Aluno Cadastrado")
       return
    print("\nLista de alunos: ")
    for aluno in alunos:
        print(aluno)

def atualizar():
    mat = input("Informe a matricula do aluno a atualizar: ")
    for aluno in alunos:
        if aluno.matricula == mat:
            print(f"Atualizar aluno: {aluno.nome}")
            aluno.nome  = input("Novo nome: ")
            aluno.idade = input("Nova idade: ")
            aluno.curso = input("Novo curso: ")
            aluno.nota  = input("Nova nota: ")
            print ("Aluno atualizar com sucesso!")
            return
    print("Matricula não encontrada.")

def remover():
    mat = input("Informe a matricula do aluno a remover: ")
    for aluno in alunos:
        if aluno.matricula == mat:
           alunos.remove(aluno)
           print("Aluno removido")
        return
    print ("Aluno não encontrado")

def buscar():
    nom = input("Informe o nome do aluno: ")
    for aluno in alunos:
        if aluno.nome == nom:
          print(aluno)
          return
    print("Aluno não encontrado!!")






while True:
    menu()
    opcao = input ("Escolha a opção: ")

    if   opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        atualizar()
    elif opcao == "4":
        remover()
    elif opcao == "5":
        buscar()
    elif opcao == "0":
        print("Encerrando...")
        break
    else:
        print("opção invalida")


def exportar_para_txt(aluno):
    with open("alunos.txt", "a", encoding="utf-8") as f:
        f.write(f"{aluno.matricula});{aluno.nome};{aluno.idade};{aluno.curso};{aluno.nota}\n")




