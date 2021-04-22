# Programação Concorrente - Problema do Produtor e Consumidor

Implementação em Python para resolver o problema do Produtor e Consumidor. Esse problema consiste em ter um ou mais produtores, que produzem um certo protudo. Uma vez que um produto é construído por um produtor, ele deve esperar que um consumidor consuma seu produto, e somente então, poderá produzir um novo. Os consumidores, por sua vez, concorrem para ver quem conseguirá consumir o produto, somente um consumidor pode consumir um certo produto, os consumidores que não conseguirem o produto devem aguardar o próximo para tentar novamente.

**Tecnologias:**

- Python (3.8).



**Dependências:**

- threading
- time



## Módulos

- <u>Numero</u> 

  Esse módulo representa o produto criado, um número. Essa classe possui 3 atributos, o último numero que foi criado, um controlador para verificar se o número foi consumido ou nao e uma instância de controle das Threads.

  **Construtor:**

```pyth
Numero(numero: int)
```


  - `numero` : número inicial do produto.

    

- <u>Produtor</u>

  Esse módulo é responsável por produzir produtos. A classe é uma Thread, quando iniciada começará a produzir produtos e esperará alguém consumir para produzir o próximo. 

  **Construtor:**

```python
Produtor(numero: Numero, nome: str, [limit: int], [sleep_time: int])
```

  - `numero` : instância do produto;
  - `nome` : nome da Thread;
  - `limit` : maior número que o produtor pode produzir (condição para parada). Se nenhum valor for passado o _default_ será 10;
  - `sleep_time` : o tempo de _delay_, em segundos, após produzir um item e ele ser consumido, para produzir  outro. Se nenhum tempo por passado p _default_ será 1 segundo.



- <u>Consumidor</u>

  Esse módulo é responsável por consumir produtos. A classe é uma Thread, quando iniciada começará a buscar por produtos construidos e guardará os números que foram consumidos em uma lista. 

  **Construtor:**

```python
Consumidor(numero: Numero, nome: str, [limit: int], [sleep_time: int])
```

  - `numero` : instância do produto;
  - `nome` : nome da Thread;
  - `limit` : maior número que o consumidor pode consumir (condição para parada). Se nenhum valor for passado o _default_ será 10;
  - `sleep_time` : o tempo de _delay_, em segundos, após consumir um item, para procurar por outro. Se nenhum tempo por passado p _default_ será 2 segundos.



- <u>Teste</u>

  O módulo é onde podemos visualizar o funcionamento dos outros módulos. Nele são criados uma instância do produto e de produtor e algumas instâncias de consumidor, e então são iniciados os processos de produzir e consumir.

  

## Execução 

Para executar o sistema bastar executar o módulo Teste com o comando abaixo:

```bash
python Teste.py
```