# Trabalho em Grupo — Estrutura de Dados: Python Collections 
![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Gráficos%202D-red?logo=plotly&logoColor=white)
![Git](https://img.shields.io/badge/Git-Versionamento-orange?logo=git&logoColor=white)

Este projeto visa descrever e avaliar o funcionamento das estruturas de dados do Python e de seu módulo **collections**. Através de testes de desempenho (benchmarks), analisamos o custo computacional das operações de **inserção, busca e remoção**, ilustrando as diferenças entre estruturas baseadas em **hashing, sequenciais e imutáveis** por meio de gráficos comparativos.
---

## 👨‍💻 Integrantes do Grupo
- **Gleidson Luan Sena Alves**  
- **Ivan Vitor Dias de Oliveira**  
- **Antonio Gemesson Sousa de Oliveira**

---

## 📚 Estruturas Analisadas

​O projeto abrange a análise das características, vantagens e desvantagens das seguintes estruturas:

- ​**Nativas**: dict, list, set, tuple.
- **​Módulo Collections**: NamedTuple, Deque, ChainMap, Counter, DefaultDict, OrderedDict, UserDict, UserList.

- **​Nota**: A estrutura UserString não foi contemplada na análise prática pois não funciona como um container de múltiplos elementos, descaracterizando o conceito de tabela de símbolos comparável às demais.

---

## ​📊 Principais Resultados da Análise 
​Com base nos testes de tempo de execução, chegamos às seguintes conclusões sobre o comportamento das estruturas:

### ​1. Tempo de Inserção ⏱️
- **Mais Rápidas (Lineares)**: list, deque e userList. Funcionam como vetores dinâmicos ou listas duplamente encadeadas, sendo extremamente otimizadas para inserções no final (e extremidades, no caso do deque).

- **Desempenho Médio (Hashing)**: dict, set, defaultDict, orderedDict. O cálculo do hash e o tratamento de colisões adicionam um custo extra em comparação à simples alocação sequencial.

- **​Mais Lentas (Imutáveis)**: tuple e namedTuple. Por serem imutáveis, qualquer "inserção" exige a recriação completa do objeto, tornando-as inviáveis para cenários de escrita frequente.

### ​2. Tempo de Consulta (Busca) 🔍
​- **Excelência (Hashing)**: dict, set, Counter e ChainMap apresentaram tempos próximos de O(1). São as escolhas ideais para grandes volumes de dados onde a velocidade de acesso é crítica.

- **Baixo Desempenho (Lineares)**: list, tuple e deque dependem de varredura sequencial O(n). O tempo de busca cresce linearmente com o tamanho da coleção.

### ​3. Tempo de Exclusão ❌
​- **Eficientes**: Estruturas baseadas em hash (dict, set, etc.) removem elementos quase instantaneamente após localizar a chave.

- **Intermediárias**: Estruturas lineares precisam buscar o elemento sequencialmente antes de removê-lo, elevando o custo.

​- **Ineficientes**: Estruturas imutáveis (tuple) exigem a cópia de toda a estrutura (menos o item removido) para um novo objeto.

___

## 🛠️ Ferramentas Utilizadas
- **[Python](https://www.python.org/)** — linguagem de programação principal do projeto.  
- **[Git](https://git-scm.com/)** — versionamento e controle do código.  
- **[Matplotlib](https://matplotlib.org/)** — geração de gráficos de desempenho das estruturas do python collections
