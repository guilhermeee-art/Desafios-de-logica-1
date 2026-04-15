'''
Tiago está operando o caixa de uma lanchonete e precisa de um sistema que some vários itens e aplique uma taxa de serviço opcional.
'''
1. Desafio: Menu de Restaurante Interativo
Contexto: Tiago está operando o caixa de uma lanchonete e precisa de um sistema que some vários itens e aplique uma taxa de serviço opcional.

Objetivo: Criar um programa que apresente um menu (1- Hambúrguer R$ 20, 2- Batata R$ 10, 3- Refri R$ 5). O programa deve permitir que Tiago adicione itens ao carrinho até que ele digite 0 para finalizar.

Conceito: while + if/elif/else + Acumulador.

Regra: Ao finalizar, pergunte se deseja adicionar 10% de taxa de serviço. Mostre o valor total final.

2. Desafio: Analisador de Clima Semanal
Contexto: Uma estação meteorológica coletou a temperatura máxima de cada um dos 7 dias da semana.

Objetivo: O programa deve receber as 7 temperaturas e, ao final, informar: a maior temperatura registrada, a menor e a média da semana.

Conceito: for + Lógica de Máximo e Mínimo.

Regra: Não use funções prontas como max() ou min(). Tente descobrir os valores usando apenas estruturas de decisão dentro do laço.

3. Desafio: Validação de Dados de Usuário
Contexto: Paula está criando um formulário de cadastro e precisa garantir que os dados façam sentido antes de salvá-los.

Objetivo: O programa deve solicitar: Nome (mais de 3 caracteres), Idade (entre 0 e 120) e Salário (maior que zero).

Conceito: Laços while individuais para validação (Data Cleaning).

Regra: O programa não deve avançar para a próxima pergunta enquanto a resposta atual for inválida, exibindo uma mensagem de erro específica para cada caso.

4. Desafio: Caixa Eletrônico (Saque)
Contexto: Um cliente quer sacar um valor X de um caixa eletrônico que possui apenas notas de R$ 50, R$ 20 e R$ 10.

Objetivo: Dado um valor inteiro de saque, o programa deve calcular a menor quantidade possível de notas de cada valor que o caixa deve entregar.

Conceito: Operadores de divisão inteira // e resto % dentro de uma lógica de decisão ou laço.

Regra: Se o usuário pedir um valor que não pode ser decomposto por essas notas (ex: R$ 7), o programa deve avisar que o valor é inválido para as notas disponíveis.

5. Desafio: Jogo da Adivinhação com Tentativas
Contexto: O computador escolheu um número secreto entre 1 e 50 e o jogador deve tentar adivinhar.

Objetivo: O programa deve permitir que o usuário tente até acertar, mas com um limite máximo de 7 tentativas.

Conceito: while + Contador + Feedback condicional.

Regra: A cada erro, o programa deve dizer se o número secreto é maior ou menor que o palpite atual. Se as tentativas acabarem, o programa exibe "Game Over" e revela o número.
