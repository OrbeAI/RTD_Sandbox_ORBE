Principais erros com Python
****

Erros na hora de programar acontece.
Eles não são desejados, porém com certeza são esperados, e é do dia a dia de um cientista de dados saber lidar e resolver os erros. 

Algumas vezes os erros podem ser causado por uma simples distração como esquecer de criar uma variável, esquecer um parênteses ou vírgula, ou por conta de algo fora de nosso controle, como a atualização de uma biblioteca. 

Por conta disso nós temos no Python um interpretador de erro, uma ferramenta que identifica em qual local do nosso código está o erro e por qual razão ele aconteceu. 

Para saber resolver e corrigir o código é importante saber interpretá-la. Separamos aqui os tipos mais comuns de erro.

01.Erro de sintaxe
======

Este erro chamado de **SyntaxError**, talvez seja o erro mais comum no dia a dia de alguem que programa é seja o erro de sintaxe.
O erro de sintaxe acontece quando erramos na forma de escrever algum comando.
Como por exemplo escrever o comando ``print()`` sem os parênteses:

.. code-block:: python
   :linenos:
   
   #Imprimindo sem os parênteses
   print"Ana" 

Ao rodar este comando, automaticamente o interpretador de erro do Python nos retorna:

.. code-block:: python
   :linenos:

  SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Ana")?

Repare que além do nome do erro **SyntaxError** ele já deu uma possível solução, nos indicando que os parênteses estão faltando. 

02.Erro de nome
=====

Este erro, chamado **NameError** acontece quando uma variável não é encontrada, seja ela local ou global.
Ele pode acontecer pois podemos ter esquecido de criar a variável, ou as vezes estamos tentando chamar uma variável local em um código global.

Exemplo:

.. code-block:: python
   :linenos:

   #Imprimindo uma variável que não foi criada
   print(minha_variavel)

Este código errado irá retornar:

.. code-block:: python
   :linenos:

   NameError: name 'minha_variavel' is not defined

Além do nome do erro ele também retorna que o nome "minha_variavel" não está definido.

Este erro também aparece ao tentarmos rodar um comando de uma biblioteca que não importamos, ou importamos com o nome errado.

03.Erro de tipo
=====

Erro de tipo, chamado de **TypeError** aparece quando tentamos realizar uma operação com um objeto de tipo (string, int, float) errado. 

Por exemplo, vamos supor que tentamos realizar a multiplicação de duas strings **a** e **b**:

.. code-block:: python
   :linenos:

   #Multiplicando duas strings
   multiplicacao = "a" * "b"

Este comando irá nos retornar:

.. code-block:: python
   :linenos:

   TypeError: can't multiply sequence by non-int of type 'str'

Além do nome do erro, ele também explica que não é possível multiplicar uma sequência não inteira do tipo string.

04.Erro de atributo.
====

Erro de atributo ou **AttributeError** ocorre ao tentar utilizar algum atributo em um objeto errado.

Vamos supor que temos uma lista, armazenada com os valores 1, 2 e 3, e tentamos utilizar um atributo da bibliotecas pandas, como shape, por exmeplo.

.. code-block:: python
   :linenos:

   #Criando uma lista com os valores 1, 2 e 3
   lista = [1, 2, 3]

   #Utilizando o atributo shape
   lista.shape

O interpretador de erro irá nos retornar:

.. code-block:: python
   :linenos:

   AttributeError: 'list' object has no attribute 'shape'

Além do nome do erro, ele nos trás que o objeto lista, não tem o atributo shape.


05.Erro de Identação
====

Erro de identação ou **IndentationError** acontece quando erramos na identação de um comando.

Por exemplo ao errar na identação de um comando como o ``if, for, while``, etc. 
Imagine que nós estabelecemos uma condição, que quando realizada imprima o texto "Condição realizada", porém colocamos o comando ``print()`` fora da identação do ``if``

.. code-block:: python
   :linenos:
   
   #Criando uma variável chamada condicao e armazenando o valor de 1
   condicao = 1

   #Criando uma estrutura de condição que está sendo realizada
   if condião == 1:
   
   #Imprimindo fora de identação
   print("Condição realizada")

Este comando o print() está em uma posição errada, e irá nos retornar: 

.. code-block:: python
   :linenos:

   IndentationError: expected an indented block

Que além do nome do erro, também nos trás que é esperado um bloco de identação.

06.Erro de Index
====

Erro de index ou **IndexError** ocorre quando o index de uma sequência está fora de alcance. 

Imagine que você possui uma lista com os valores 1, 2 e 3 armazenados e tenta rodar um loop de 4 com o comando for.

Exemplo:

.. code-block:: python
   :linenos:

   #Criando uma lista e armazenando os valores 1, 2 e 3
   lista = [1, 2, 3] 

   #Criando um loop fora de alcance
   for variavel_do_for in range(4):
    print(lista[variavel_do_for]

Como não possuímos um alcance de 4, ele irá nos retornar:

.. code-block:: python
   :linenos:

   IndexError: list index out of range

Que além de nos trazer o nome do erro, também nos indica que a lista está fora de index.
