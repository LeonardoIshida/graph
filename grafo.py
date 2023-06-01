class Grafo:
    def __init__(self, vertices, arestas) -> None:
        self.n_vetices = vertices
        self.n_arestas = arestas
        self.vertices = [Vertice(i) for i in range(vertices)]
        self.tempo = 0
        
    def cria_lista_adj(self, source, dest):
        self.vertices[source].lista_adj.append(Vertice(dest))
        
    def dfs(self, atual, stack, on_stack, low, descoberta):
        descoberta[atual] = self.tempo
        low[atual] = self.tempo
        self.tempo += 1
        on_stack[atual] = True
        stack.append(atual)
        
        for n in self.vertices[atual].lista_adj:
            v = n.vertice
            if descoberta[v] == -1:
                self.dfs(v, stack, on_stack, low, descoberta)
                low[atual] = min(low[atual], low[v])
            
            elif on_stack[v]:
                low[atual] = min(low[atual], low[v])
                
        vert_aux = -1
        if low[atual] == descoberta[atual]:
            while vert_aux != atual:
                vert_aux = stack.pop()
                print(vert_aux, end=' ')
                on_stack[vert_aux] = False
            print()
        
        
        
    
    def tarjan(self):
        stack = []
        on_stack = [False for _ in range(self.n_vetices)]
        low = [-1 for _ in range(self.n_vetices)]
        descoberta = [-1 for _ in range(self.n_vetices)]
        
        for i in range(self.n_vetices):
            if descoberta[i] == -1:
                self.dfs(i, stack, on_stack, low, descoberta)
    
        
class Vertice:
    def __init__(self, vertice) -> None:
        self.vertice = vertice
        self.lista_adj = []
        self.visitado = False
        self.antecessor = -1
        
        
        
if __name__ == '__main__':
    vert, aresta = [int(x) for x in input().split()]
    grafo = Grafo(vert, aresta)
    
    for i in range(grafo.n_arestas):
        vert_source, vert_dest = [int(x) for x in input().split()]
        grafo.cria_lista_adj(vert_source, vert_dest)
        
    # for i in range(grafo.n_vetices):
    #     for j in range(len(grafo.vertices[i].lista_adj)):
    #         print(grafo.vertices[i].lista_adj[j].vertice)
            
    grafo.tarjan()
