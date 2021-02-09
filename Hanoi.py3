pilha1=[]
pilha2=[]
pilha3=[]

def criarTorre(tam):
    for i in range(1,tam+1,1):
        pilha1.append(i)
        pilha1.sort(reverse=True)

def mover(deOnde, paraOnde, auxiliar,al):
    if al >= 1:
        mover(deOnde,auxiliar,paraOnde,al-1)
        moverDisco(deOnde,paraOnde)
        print(pilha1, pilha2, pilha3)
        mover(auxiliar,paraOnde,deOnde,al-1)

def moverDisco(do,tp):
    tp.append(do[-1])
    do.pop(-1)

def começar(discos):
    criarTorre(discos)
    mover(pilha1,pilha2,pilha3,discos)

começar(4)
print(pilha1,pilha2,pilha3)
