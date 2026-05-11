class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.estado = "pendurada"

lista_tarefas = []

def adicionar_tarefa():
    texto = input("\nDescrição da nova tarefa: ")
    nova_tarefa = Tarefa(texto)
    lista_tarefas.append(nova_tarefa)
    print("Sucesso: Tarefa adicionada!")

def listar_tarefas(filtro=None, pause=True):
    print(f"\n--- LISTA ({filtro if filtro else 'TODAS'}) ---")
    encontrou = False
   
    for i, tarefa in enumerate(lista_tarefas):
        if filtro and tarefa.estado != filtro:
            continue
        print(f"{i} - [{tarefa.estado}] {tarefa.descricao}")
        encontrou = True
   
    if not encontrou:
        print("Nenhuma tarefa encontrada.")
   
    if pause:
        print("\n" + "-"*30)
        input("Pressione Enter para voltar ao menu...")

def marcar_concluida():
    listar_tarefas(filtro="pendurada", pause=False)
   
    if len(lista_tarefas) == 0:
        return

    try:
        indice = int(input("\nDigite o número da tarefa para concluir: "))
        lista_tarefas[indice].estado = "concluída"
        print("Sucesso: Status atualizado!")
    except:
        print("Erro: Número inválido!")

def visualizar_detalhes():
    listar_tarefas(pause=False)
   
    if len(lista_tarefas) == 0:
        return

    try:
        indice = int(input("\nDigite o número para ver detalhes: "))
        t = lista_tarefas[indice]
       
        detalhes = {
            "O que fazer": t.descricao,
            "Como está": t.estado,
            "Prioridade": "Normal"
        }
       
        print("\n DETALHES ")
        for chave, valor in detalhes.items():
            print(f"{chave}: {valor}")
       
        input("\nPressione Enter para continuar...")
    except:
        print("Erro: Tarefa não encontrada!")

def menu():
    while True:
        print("\n SISTEMA DE GESTÃO")
        print("1. Adicionar tarefa")
        print("2. Listar todas")
        print("3. Marcar como concluída (ver penduradas)")
        print("4. Ver apenas concluídas")
        print("5. Ver apenas penduradas")
        print("6. Detalhar tarefa (ver tudo)")
        print("0. Sair")
       
        opcao = input("Escolha uma opção: ")

        if opcao == "1": adicionar_tarefa()
        elif opcao == "2": listar_tarefas()
        elif opcao == "3": marcar_concluida()
        elif opcao == "4": listar_tarefas("concluída")
        elif opcao == "5": listar_tarefas("pendurada")
        elif opcao == "6": visualizar_detalhes()
        elif opcao == "0":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
