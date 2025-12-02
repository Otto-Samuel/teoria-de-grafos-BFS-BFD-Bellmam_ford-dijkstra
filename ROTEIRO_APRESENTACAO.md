# 🎤 ROTEIRO DE APRESENTAÇÃO - ALGORITMOS DE GRAFOS

> **Tempo total: 15-20 minutos**  
> Use este roteiro como guia enquanto fala

---

## 📌 INTRODUÇÃO (2 min)

**O que você diz:**

"Boa tarde! Somos [NOMES], e vamos apresentar um projeto sobre **ALGORITMOS DE CAMINHAMENTO EM GRAFOS**.

Hoje vamos aprender 4 algoritmos fundamentais que usam:
- **BFS** - Busca em Amplitude
- **DFS** - Busca em Profundidade  
- **Dijkstra** - Caminho mais curto (pesos positivos)
- **Bellman-Ford** - Caminho mais curto (pesos negativos)

Tudo isso em um grafo real com **16 cidades brasileiras**!"

---

## 1️⃣ CONCEITOS BÁSICOS (3 min)

### O que é um Grafo?

**O que você diz:**

"Antes de tudo, vamos entender o que é um grafo.

Um **grafo** é uma estrutura matemática com:
- **Vértices** - os pontos (representam cidades, pessoas, objetos)
- **Arestas** - as linhas que conectam vértices (representam conexões)
- **Pesos** - valores nas arestas (distância, custo, tempo)"

**Exemplo visual que você deve desenhar (ou mostrar):**

```
        [Cidade A]
         /   |   \
       10    15   20
      /      |     \
   [B]     [C]    [D]
```

**O que você diz:**

"Em nosso projeto:
- **Vértices** = 16 cidades brasileiras (São Paulo, Rio, Belo Horizonte, etc)
- **Arestas** = Rotas entre as cidades
- **Pesos** = Distância em quilômetros

Por que estudar grafos?
- 🗺️ GPS e mapas (encontrar melhor rota)
- 🌐 Redes sociais (conexões entre pessoas)
- 🚚 Logística (otimizar entregas)
- 📡 Roteamento de internet"

---

## 2️⃣ BFS - BUSCA EM AMPLITUDE (2.5 min)

### Conceito

**O que você diz:**

"O primeiro algoritmo é **BFS** - Breadth First Search, ou Busca em Amplitude.

Imaginem que vocês estão em uma cidade (origem) e querem explorar TODAS as cidades, mas explorando por **nível de distância**:
- Nível 0: A cidade onde estou
- Nível 1: Todas as cidades vizinhas (diretas)
- Nível 2: Cidades vizinhas das vizinhas
- E assim por diante..."

### Como Funciona

**O que você diz:**

"O algoritmo funciona assim:

1. Comece com a cidade inicial (uma fila com 1 cidade)
2. Tire a primeira cidade da fila
3. Para cada vizinha dela que AINDA NÃO VISITEI:
   - Marque como visitada
   - Registre qual é a mãe/pai (de onde vim)
   - Adicione à fila
4. Volte para o passo 2 até a fila ficar vazia

É como uma onda que se expande!"

### Estrutura de Dados

```python
def bfs(graph, start):
    parent = {}                    # Armazena o pai de cada vértice
    visited = set()                # Vértices já visitados
    q = deque([start])             # Fila com vértices a processar
    visited.add(start)
    parent[start] = None           # Origem não tem pai
    
    while q:                       # Enquanto houver vértices na fila
        u = q.popleft()            # Tire o primeiro
        for v, _ in graph.adj.get(u, []):  # Para cada vizinho
            if v not in visited:   # Se não visitou ainda
                visited.add(v)     # Marca como visitado
                parent[v] = u      # Registra quem é o pai
                q.append(v)        # Adiciona à fila
    
    return parent
```

**O que você diz:**

"A estrutura usa uma **fila** (FIFO - First In, First Out).
Isso garante que exploramos por níveis."

### Características

| Aspecto | Valor |
|---------|-------|
| **Tempo** | O(V + E) |
| **Espaço** | O(V) |
| **Pesos negativos?** | ❌ Não |
| **Melhor para** | Caminho mais curto em grafos sem peso |

### Aplicações

- Encontrar caminho mais curto (grafos sem pesos)
- Verificar se o grafo é conectado
- Análise de distância entre nós

---

## 3️⃣ DFS - BUSCA EM PROFUNDIDADE (2.5 min)

### Conceito

**O que você diz:**

"Agora, o segundo algoritmo: **DFS** - Depth First Search, ou Busca em Profundidade.

Enquanto BFS vai por **níveis**, DFS vai em **profundidade**:
- Escolha um caminho
- Vá o máximo longe possível nesse caminho
- Quando chegar em um beco sem saída, **volte para trás** (backtrack)
- Tente outro caminho

É como explorar uma floresta labiríntica indo o mais fundo possível!"

### Como Funciona

**O que você diz:**

"Funciona assim:

1. Comece em uma cidade
2. Visite um vizinho não visitado (qualquer um)
3. Recursivamente, faça o passo 2 para esse vizinho
4. Quando não há mais vizinhos não visitados, **retroceda**
5. Tente outro vizinho não visitado da cidade anterior
6. Repita até visitar tudo"

### Estrutura de Dados

```python
def dfs(graph, start):
    parent = {}      # Pai de cada vértice
    order = []       # Ordem de descoberta
    visited = set()  # Visitados
    
    def visit(u, p):           # Função recursiva
        visited.add(u)         # Marca como visitado
        parent[u] = p          # Registra pai
        order.append(u)        # Registra ordem
        for v, _ in graph.adj.get(u, []):  # Para cada vizinho
            if v not in visited:
                visit(v, u)    # Chamada recursiva! Vai fundo!
    
    visit(start, None)
    return parent, order
```

**O que você diz:**

"Usa **recursão**! Cada chamada vai mais fundo na árvore.
Quando retorna, tenta outro caminho."

### Características

| Aspecto | Valor |
|---------|-------|
| **Tempo** | O(V + E) |
| **Espaço** | O(V) |
| **Pesos negativos?** | ❌ Não |
| **Melhor para** | Detectar ciclos, topologia |

### Aplicações

- Detectar ciclos em grafos
- Ordenação topológica
- Encontrar componentes conectadas

### BFS vs DFS

| BFS | DFS |
|-----|-----|
| Nível por nível | Fundo primeiro |
| Usa fila | Usa recursão/pilha |
| Melhor para distância | Melhor para ciclos |

---

## 4️⃣ DIJKSTRA - CAMINHO MAIS CURTO (3 min)

### Conceito

**O que você diz:**

"Agora vem um dos **algoritmos mais famosos**: **Dijkstra**!

BFS e DFS nos mostram COMO chegar, mas não nos mostram o **MELHOR caminho** em termos de distância.

Dijkstra resolve isso! Ele encontra o **caminho mais curto** entre dois pontos quando temos pesos nas arestas.

É o algoritmo que o **GPS usa** para calcular a melhor rota!"

### Como Funciona

**O que você diz:**

"Funciona assim:

1. Todas as cidades começam com distância = ∞ (infinito)
   - Exceto a origem, que é 0
2. Escolha a cidade não visitada com MENOR distância
3. Para cada vizinha dessa cidade:
   - Calcule: distância_origem + peso_aresta
   - Se for menor que a distância atual, ATUALIZE
4. Marque como visitada
5. Repita 2-4 até visitar todas

É como ir expandindo do centro para fora, sempre pegando o mais perto!"

### Estrutura de Dados

```python
def dijkstra(graph, source):
    dist = {v: math.inf for v in graph.vertices()}  # Distâncias
    parent = {v: None for v in graph.vertices()}    # Pais
    dist[source] = 0.0
    pq = [(0.0, source)]  # Fila de prioridade: (distância, vértice)
    
    while pq:
        d, u = heapq.heappop(pq)  # Pega o de MENOR distância
        
        if d > dist[u]:           # Se já achamos um melhor, ignora
            continue
        
        for v, w in graph.adj.get(u, []):  # Para cada vizinho
            nd = d + w                      # Nova distância
            if nd < dist[v]:                # Se é melhor
                dist[v] = nd                # Atualiza
                parent[v] = u               # Registra pai
                heapq.heappush(pq, (nd, v))  # Adiciona à fila
    
    return dist, parent
```

**O que você diz:**

"A diferença importante é a **fila de prioridade** (min-heap).
Sempre pegamos o vértice com MENOR distância.
Isso garante que encontramos o caminho mais curto."

### Características

| Aspecto | Valor |
|---------|-------|
| **Tempo** | O((V + E) log V) |
| **Espaço** | O(V) |
| **Pesos negativos?** | ❌ NÃO |
| **Melhor para** | Caminho mais curto (pesos positivos) |

### ⚠️ LIMITAÇÃO IMPORTANTE

**O que você diz:**

"Dijkstra tem UMA LIMITAÇÃO MUITO IMPORTANTE:

**Não funciona com pesos negativos!**

Por quê? Porque o algoritmo assume que uma vez que visitou um vértice,
encontrou o melhor caminho. Mas com pesos negativos, pode haver um caminho
melhor vindo de trás.

Exemplo:
- Rota A → B custa 10
- Rota B → C custa -15
- Rota A → D → C custa 5

Dijkstra pode escolher A → B → C = -5 como final.
Mas um peso negativo pode mudar isso depois!"

### Aplicações

- 🗺️ GPS e mapas (melhor rota)
- 🌐 Roteamento em redes
- 🚚 Planejamento logístico

---

## 5️⃣ BELLMAN-FORD - O VERSÁTIL (3 min)

### Conceito

**O que você diz:**

"O último algoritmo é **Bellman-Ford**.

Ele é basicamente 'Dijkstra com esteróides' porque:
1. Funciona com pesos NEGATIVOS
2. Detecta ciclos negativos

A troca? É mais lento. Mas quando você PRECISA de pesos negativos,
é sua única opção!"

### Como Funciona

**O que você diz:**

"Bellman-Ford funciona assim:

1. Todas as distâncias começam como ∞ (infinito)
   - Exceto origem = 0
2. Repita (V-1) vezes:
   - Para CADA aresta do grafo:
     - Se dist[origem] + peso < dist[destino]:
       - ATUALIZE a distância
3. Depois, faça UMA verificação final procurando melhorias
   - Se ainda houver melhoria, há um **ciclo negativo**!

Por que (V-1)? Qualquer caminho simples tem no máximo V-1 arestas.
Depois de V-1 iterações, todas as distâncias corretas estão lá.
Se ainda muda, alguém 'tomou emprestado' de um ciclo negativo!"

### Estrutura de Dados

```python
def bellman_ford(graph, source):
    vertices = graph.vertices()
    dist = {v: float('inf') for v in vertices}
    parent = {v: None for v in vertices}
    dist[source] = 0.0
    n = len(vertices)
    edges = graph.edges()
    
    # Relaxar arestas (V-1) vezes
    for i in range(n - 1):
        updated = False
        for u, v, w in edges:  # Para CADA aresta
            if dist[u] + w < dist[v]:  # Se melhora
                dist[v] = dist[u] + w
                parent[v] = u
                updated = True
        if not updated:  # Se nada mudou, pode parar
            break
    
    # Verificar ciclo negativo
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return None, None  # CICLO NEGATIVO DETECTADO!
    
    return dist, parent
```

### Características

| Aspecto | Valor |
|---------|-------|
| **Tempo** | O(V × E) |
| **Espaço** | O(V) |
| **Pesos negativos?** | ✅ SIM |
| **Ciclos negativos?** | ✅ Detecta |
| **Melhor para** | Pesos negativos, ciclos |

### Dijkstra vs Bellman-Ford

| Dijkstra | Bellman-Ford |
|----------|--------------|
| O((V+E)logV) | O(V × E) |
| Pesos positivos | Pesos positivos/negativos |
| Rápido | Lento |
| Sem detecção de ciclos | Detecta ciclos negativos |

**O que você diz:**

"Dijkstra é 4-10x mais rápido. Então use Dijkstra se possível.
Mas se tem pesos negativos, Bellman-Ford é sua única opção!"

### Aplicações

- 💰 Detecção de arbitragem em mercados financeiros
  - Se há ganho (peso negativo) que cria ciclo, você pode lucrar infinito!
- 📡 Protocolos de roteamento (RIP - Routing Information Protocol)
- 📊 Problemas com custos/ganhos negativos

---

## 🖥️ EXECUÇÃO PRÁTICA (3 min)

### Como Rodar

**O que você faz (mostrar na tela):**

```bash
cd src
python main.py
```

**Tempo de espera:** ~2 segundos

### O que Aparece - Explicação Prática

#### 1. Grafo é criado com 16 vértices

**O que você diz:**

"Primeiro, criamos um grafo com 16 cidades. Vemos aqui uma amostra das
conexões. Cada aresta tem uma cidade de origem, seus vizinhos e as distâncias."

#### 2. BFS executa

```
Pais (parent) da BFS (primeiros 10 vértices):
  Vértice  0: parent = None
  Vértice  1: parent = 0
  Vértice 15: parent = 0
  Vértice  5: parent = 0
  ...
```

**O que você diz:**

"Vejam! Vértice 0 é a origem (parent = None).
Os vizinhos diretos dele (1, 15, 5) têm ele como pai.
Depois, cada nó tem um pai específico. Isso forma uma árvore!

Se eu quisesse voltar da cidade 15 até 0, ia: 15 → 0."

#### 3. DFS executa

```
Ordem de descoberta (primeiros 12 vértices):
  0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11
```

**O que você diz:**

"DFS descobrir na ordem: 0, 1, 2, 3, 4...

Reparem como é diferente do BFS! BFS ia por níveis, DFS vai fundo em
um caminho, depois volta. A ordem reflete isso."

#### 4. DIJKSTRA executa

```
Distâncias mais curtas da origem (vértice 0):
  0: 0.00
  1: 6.75
  2: 7.98
  3: 11.46
  ...
  7: 18.24

Exemplo: Caminho mais curto para vértice 7:
  0 → 5 → 7 (distância: 18.24)
```

**O que você diz:**

"Dijkstra calcula a distância MÍNIMA para CADA vértice.

Saindo do vértice 0:
- Vértice 1 está a 6.75 km
- Vértice 15 está a 5.90 km (mais perto!)
- Vértice 7 está a 18.24 km

E mostra também o CAMINHO: 0 → 5 → 7

Não é 0 → 1 → 2 → ... que seria mais longo. Dijkstra escolhe a rota
mais inteligente usando a estrutura do grafo."

#### 5. BELLMAN-FORD executa

```
(Mesmo resultado que Dijkstra, pois não há pesos negativos)
```

**O que você diz:**

"Como não temos pesos negativos, Bellman-Ford dá o mesmo resultado.

Mas se tivéssemos arestas negativas? Bellman-Ford ainda funcionaria!
E se detectasse um ciclo negativo, retornaria None, None."

#### 6. Tabela Comparativa Final

```
┌─────────────┬───────────────┬──────────────┬──────────────────────┐
│ Algoritmo   │ Complexidade  │ Pesos Neg.   │ Melhor para          │
├─────────────┼───────────────┼──────────────┼──────────────────────┤
│ BFS         │ O(V + E)      │ ❌ Não       │ Caminho curto (não-p)│
│ DFS         │ O(V + E)      │ ❌ Não       │ Ciclos, Topologia    │
│ Dijkstra    │ O((V+E)logV)  │ ❌ Não       │ Caminho curto (+)    │
│ Bellman-Ford│ O(V × E)      │ ✅ Sim       │ Ciclos negativos     │
└─────────────┴───────────────┴──────────────┴──────────────────────┘
```

**O que você diz:**

"Aqui temos o resumo de tudo:

- BFS e DFS: As mais rápidas, mas não calculam distância mínima
- Dijkstra: Rápida para pesos positivos (a maioria dos casos!)
- Bellman-Ford: Lenta, mas funciona com qualquer peso

Escolha depende do seu problema!"

---

## 🎯 RESUMO E CONCLUSÃO (2 min)

**O que você diz:**

"Para resumir:

**BFS - Breadth First Search**
- Explora nível por nível
- Usa fila
- Encontra caminho mais curto em grafos sem peso
- Complexidade: O(V + E)

**DFS - Depth First Search**
- Explora fundo depois volta
- Usa recursão
- Detecta ciclos
- Complexidade: O(V + E)

**DIJKSTRA - O mais popular**
- Encontra caminho mais curto com pesos
- Funciona APENAS com pesos positivos
- Usa min-heap
- Complexidade: O((V + E) log V)
- O **GPS usa isso**!

**BELLMAN-FORD - O mais versátil**
- Funciona com pesos negativos
- Detecta ciclos negativos
- Mais lento
- Complexidade: O(V × E)

Todos resolvem o mesmo problema (conectividade/caminho) de formas diferentes,
cada um com seus trade-offs entre velocidade e generalidade."

### Quando Usar Cada Um

**O que você diz:**

"Decisão rápida:

1. Tenho pesos negativos?
   - SIM → Use Bellman-Ford
   - NÃO → Continue

2. Preciso só de conectividade ou caminho mais curto SEM peso?
   - SIM → Use BFS ou DFS
   - NÃO → Continue

3. Preciso de caminho mais curto com pesos positivos?
   - SIM → Use Dijkstra (mais rápido!)

Resumo:
- Sem pesos: BFS (ou DFS)
- Pesos positivos: Dijkstra
- Pesos negativos: Bellman-Ford"

### Arquitetura do Projeto

**O que você diz:**

"Nosso projeto está organizado assim:

```
src/
├── main.py           → Ponto de entrada, integra tudo
├── bfs_dfs_simple.py → BFS e DFS (2 funções simples)
├── dijkstra.py       → Dijkstra (1 função)
└── bellman_ford.py   → Bellman-Ford (1 função)
```

Cada algoritmo é uma função **pura e independente**.
Isso significa que você pode pegar o código de dijkstra.py e usar em
outro projeto sem modificações!

Seguimos o padrão **Clean Code**: cada arquivo tem uma responsabilidade,
nomes claros, documentação completa."

---

## 🚀 PRÓXIMAS POSSIBILIDADES

**O que você diz:**

"Se tivéssemos mais tempo, poderíamos implementar:

- **A* Search**: Dijkstra com heurística (mais rápido com direção)
- **Floyd-Warshall**: Distância entre TODOS os pares
- **Árvore Geradora Mínima**: Algoritmo de Prim ou Kruskal
- **Visualização**: Desenhar o grafo com matplotlib
- **Datasets maiores**: Testar com milhares de vértices
- **Benchmarking**: Comparar performance real"

---

## ❓ PERGUNTAS ESPERADAS & RESPOSTAS

### P: Por que não usar sempre Bellman-Ford se funciona com qualquer peso?

**R:** Velocidade! Dijkstra é O((V+E)logV), Bellman-Ford é O(V×E).
Para um grafo de 1000 vértices e 5000 arestas:
- Dijkstra: ~50.000 operações
- Bellman-Ford: ~5.000.000 operações

Se só tem pesos positivos, Dijkstra é 100x mais rápido!

### P: Como detectar ciclo negativo sem rodar Bellman-Ford?

**R:** Você precisa rodar Bellman-Ford. A detecção é feita na 4ª iteração:
se algo ainda muda, há ciclo negativo.

### P: Posso modificar o grafo para teste?

**R:** Sim! No código:
```python
g = Graph()
g.add_edge(0, 1, 10)
g.add_edge(1, 2, 5)
# ...

parent = bfs(g, 0)
```

### P: Por que BFS usa fila e DFS usa recursão?

**R:** Porque:
- BFS precisa visitar em ordem (nível por nível) → fila (FIFO)
- DFS precisa voltar quando toca fundo → recursão/pilha (LIFO)

---

## 📎 DICAS PARA APRESENTAÇÃO

✅ **Faça assim:**
- Pratique antes! Leia este roteiro 2-3 vezes
- Fale de forma natural, não decore
- Aponte na tela quando mostra output
- Deixe questões abertas: "Alguém sabe por quê?"
- Pause após explicar conceito complexo (Dijkstra)

❌ **Não faça:**
- Não leia código linha por linha
- Não fale muito rápido (especialmente em algoritmos)
- Não pule conceitos (Bellman-Ford sem explicar por quê diferente)
- Não fique em pé de costas pro público

---

## ⏱️ CRONOGRAMA SUGERIDO

| Parte | Tópico | Tempo |
|-------|--------|-------|
| 0 | Introdução | 2 min |
| 1 | Conceitos (Grafo) | 3 min |
| 2 | BFS | 2.5 min |
| 3 | DFS | 2.5 min |
| 4 | Dijkstra | 3 min |
| 5 | Bellman-Ford | 3 min |
| 6 | Demo prática | 3 min |
| 7 | Conclusão | 2 min |
| 8 | Perguntas | ? |
| **TOTAL** | | **~22 min** |

Se ficar apertado, corte tempo em DFS (mais simples que Dijkstra).

---

**Boa sorte na apresentação! 🎉**
