from tkinter import filedialog, messagebox
import csv
import numpy as np

list_linear = []
igualdade = []
filename = filedialog.askopenfile()

with open(f'{filename.name}') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        x = 0
        for i in row:
            row[x] = int(i)
            x = x + 1
        list_linear.append(row)

def separateList(lista):
    lenList = len(lista)
    if lenList == 2:
        igualdade.append(lista[0][2])
        igualdade.append(lista[1][2])
        del lista[0][2]
        del lista[1][2]
    elif lenList == 3:
        igualdade.append(lista[0][3])
        igualdade.append(lista[1][3])
        igualdade.append(lista[2][3])
        del lista[0][3]
        del lista[1][3]
        del lista[2][3]
    else:
        messagebox.showinfo(title="Mensagem", message="Sistema não identificado, selecione outro arquivo")
    print(list_linear, igualdade)

def resolver_sistema_linear(matriz_coeficientes, vetor_constantes):
    try:
        solucao = np.linalg.solve(matriz_coeficientes, vetor_constantes)
        return solucao
    except np.linalg.LinAlgError:
        return None

separateList(list_linear)
solucao = resolver_sistema_linear(np.array(list_linear), np.array(igualdade))

if solucao is not None:
    messagebox.showinfo(title="Resposta", message=f"A resposta do seu sistema é: {solucao}")
    print("Solução do sistema:")
    print(solucao)
else:
    print("O sistema não tem solução única.")