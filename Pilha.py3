import random
#Criar 4 paginas
for k in range(4):
    pilha = []
    pagina = []

    def criaPilha(pil):# criar pilhas randomicas
        while len(pil)<8:
            pil.append(random.randint(0, 9))
        pagina.append(pilha)

    for i in range(4):#Adicionar 4 pilhas na pagina
        pilha=[]
        criaPilha(pilha)

    print(f"pagina {k + 1} cheia: {pagina}")#Exibir pilha criada

    for a in range(4):#Remover 20% dos elementos
        for j in range(2):
            pagina[a].pop(-1)

    print(f"pagina {k+1} -20% (dois elementos): {pagina}")#Exibir novo estado da pilha;

    for a in range(4):#Remover 20% dos elementos
        pagina[a].pop(-1)

    print(f"pagina {k+1} -20%(um elemento): {pagina}\n")#Exibir novo estado da pilha;
