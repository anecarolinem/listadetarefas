"""criar tarefa, lista, opção de desfazer e refazer

"""
def prim_list(todo_list):
    print()
    print('Tarefas:')
    print(todo_list)
    print()


def list_desfazer (todo_list,refazer):
   if not todo_list:
       print('Nada a desfazer')
       return
   last_todo =todo_list.pop() #retirar o último termo e retorna
   refazer.append(last_todo)
   print()


def list_refazer (todo_list,refazer):
   if not refazer:
       print('Nada a refazer')
       return
   last_refazer = refazer.pop() #retirar o último termo e retorna
   todo_list.append(last_refazer)




def adiciona(tarefa, todo_list):
   todo_list.append(tarefa)




if __name__ == '__main__':
    todo_list =[]
    refazer = []

    while True:
        tarefa = input('Digite uma tarefa ou desfazer, refazer, ls:  ' )

        if tarefa == 'ls':
            prim_list(todo_list)
            continue
        elif tarefa == 'desfazer':
            list_desfazer(todo_list, refazer)
            continue
        elif tarefa == 'refazer':
            list_refazer(todo_list,refazer)
            continue

        adiciona(tarefa,todo_list)