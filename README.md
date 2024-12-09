Alunos: Alexandre Silva, Sandro Gomes, Luiz Eduardo e Gabriel Henrique

Colégio: SESI Paulista

Professores:
Thays Luana (Matemática)
Eduardo Hernande (Desenvolvimento de Sistemas)

Projeto Trigotech
O projeto TrigonTech foi uma atividade do curso de Desenvolvimento de Sistemas, em parceria com a disciplina de Matemática.
Sua finalidade era criar um algoritmo na linguagem Python, utilizando a biblioteca math que contém várias funções matemáticas
incluindo cálculos trigonométricos. O foco é transformar ângulos de graus para radianos e, em seguida, calcular a tangente.

Entrada do Usuário
O programa solicita ao usuário que digite um ângulo em graus. Esse valor é lido como uma string, mas é convertido para float
para garantir que o usuário possa digitar valores com casas decimais.

Validação do Ângulo
Primeiro, verifica se o ângulo é positivo. Caso contrário, lança um erro (ValueError) com uma mensagem informando
que o ângulo deve ser positivo.

Conversão de Graus em Radianos
No Python, as funções trigonométricas utilizam radianos em vez de graus. Portanto, o primeiro passo no algoritmo
é converter o ângulo fornecido pelo usuário de graus para radianos.

Cálculo da tangente
Por fim, a função calcular_tangente realiza o cálculo da tangente de um ângulo. Que é dada a razão entre o seno e o cosseno
do ângulo inserido pelo usuário.
