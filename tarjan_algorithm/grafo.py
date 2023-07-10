class Grafo:
    def __init__(self, vertices, arestas) -> None:
        self.n_vetices = vertices
        self.n_arestas = arestas
        self.vertices = [Vertice(i) for i in range(vertices)]
        self.tempo = 0
        self.n_cfc = 0
        
    def cria_lista_adj(self, source, dest):
        self.vertices[source].lista_adj.append(dest)
        
    def dfs(self, vert_atual, tarj_utils):
        # salvando o tempo de descobrimento do vertice atual 
        tarj_utils.descoberta[vert_atual] = self.tempo
        
        # salvando o low do vertice atual
        tarj_utils.low[vert_atual]  = self.tempo
        
        # inserindo na pilha
        tarj_utils.esta_na_pilha[vert_atual] = True
        tarj_utils.pilha.append(vert_atual)
        
        self.tempo += 1
        
        # percorrendo a lista de adjacencia
        for vizinho in self.vertices[vert_atual].lista_adj:
            
            # se vizinho ainda nao foi descoberto(esta branco), entao ir para ele
            if tarj_utils.descoberta[vizinho] == -1:
                self.dfs(vizinho, tarj_utils)
                
                # fazendo o calculo do low na volta da recursao
                tarj_utils.low[vert_atual] = min(tarj_utils.low[vert_atual], tarj_utils.low[vizinho])
            
            # se o vizinho ja foi descoberto previamente, calcular o low
            elif tarj_utils.esta_na_pilha[vizinho]:
                tarj_utils.low[vert_atual] = min(tarj_utils.low[vert_atual], tarj_utils.low[vizinho])
                
        # desempilhando uma componente fortemente conexa
        vert_aux = -1
        if tarj_utils.low[vert_atual] == tarj_utils.descoberta[vert_atual]:
            lista_cfc = []
            while vert_aux != vert_atual:
                vert_aux = tarj_utils.pilha.pop()
                lista_cfc.append(vert_aux)
                tarj_utils.esta_na_pilha[vert_aux] = False
            
            # inserindo a componente fortemente conexa, ordenada, na lista de repostas
            lista_cfc.sort()
            tarj_utils.resposta.append(lista_cfc)
            self.n_cfc += 1
        
        
        
    
    def tarjan(self, tarj_utils):
        for vertice in range(self.n_vetices):
            if tarj_utils.descoberta[vertice] == -1:
                self.dfs(vertice, tarj_utils)
    
  
# classe para auxiliar a criacao do grafo      
class Vertice:
    def __init__(self, vertice) -> None:
        self.vertice = vertice
        self.lista_adj = []
        self.visitado = False
        self.antecessor = -1
    
# classe para auxiliar o algoritmo de tarjan, possui listas e valores necessarios para rodar o algoritmo     
class TarjanUtils:
    def __init__(self, num_vert):
        self.low = [-1 for _ in range(num_vert)]
        self.esta_na_pilha = [False for _ in range(num_vert)]
        self.descoberta = [-1 for _ in range(num_vert)]
        self.resposta = []
        self.pilha = []
        
        
    def printar_resposta(self):
        # ordenando a lista que contem as componenetes fortemente conexas
        self.resposta.sort()
        
        # printando as cfc
        for cfc in self.resposta:
            print(' '.join(map(str, cfc)))
        
        
if __name__ == '__main__':
    # lendo a quantidade de vertices e arestas e criando grafo e utilitarios de tarjan
    vert, aresta = [int(x) for x in input().split()]
    grafo = Grafo(vert, aresta)
    tarjan_utils = TarjanUtils(vert)
    
    # criando a lista de adjacencia do grafo
    for i in range(grafo.n_arestas):
        vert_source, vert_dest = [int(x) for x in input().split()]
        grafo.cria_lista_adj(vert_source, vert_dest)
       
    # chamada para o algoritmo de tarjan     
    grafo.tarjan(tarjan_utils)
    
    # imprimindo as respostas
    print(grafo.n_cfc)
    tarjan_utils.printar_resposta()