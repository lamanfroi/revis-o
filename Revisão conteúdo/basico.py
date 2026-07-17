#1. O básico

print("Hello, World!") # O comando print exibe informações no terminal.
caixa = float(input('Que informação você gostaria de salvar?')) # O comando input serve para recebermos e guardarmos dados
print(caixa)

#2. Armazenamento e tipos de dados

nome = 'Luiz' # Tipo de dado String: texto
idade = 21 # Tipo de dado Int: número inteiro
idadeComMeses = 21.7 # Tipo de dado Float: número fracionado
verdadeiro_ou_falso = True # Tipo de dado Bool: verdadeiro ou falso

#3. Operadores e Lógica


# Operadores Aritméticos
soma = 1 + 1 # O operador aritmético '+' serve para somar
subtracao = 1 - 1 # O operador aritmético '-' serve para subtrair
multiplicacao = 2 * 2 # O operador aritmético '*' serve para multiplicar
divisao = 3 / 2 # O operador aritmético '/' serve para dividir
divisao_por_inteiro = 4 // 2 # O operador aritmético '//' serve para dividir por inteiro

# Operadores Relacionais

if soma == subtracao: # O operador '==' serve para comparar se uma variável/numéro/texto é igual ao outro.
    print('soma é igual a subtração')
elif soma != subtracao: # O operador '!=' serve para comparar se uma variável/numéro/texto é diferente ao outro.
    print('soma é diferente de subtração')
elif soma > subtracao: # O operador '!=' serve para comparar se uma variável/numéro/texto é maior que outro.
    print('soma é maior que a subtração')
elif soma < subtracao: # O operador '!=' serve para comparar se uma variável/numéro/texto é menor que outro.
    print('soma é menor que a subtração')
elif soma >= subtracao: # O operador '!=' serve para comparar se uma variável/numéro/texto é maior ou igual ao outro.
    print('soma é maior ou igual a subtração')
elif soma <= subtracao: # O operador '!=' serve para comparar se uma variável/numéro/texto é menor ou igual ao outro.
    print('soma é menor ou igual a subtração')

#4. Controle de Fluxo

idade = int(input('Digite a sua idade'))
if idade >= 18: # Serve para fazer verificações de verdadeiro ou falso. "Se" for verdadeiro, então o código funciona. "Se" for falso, o código passa para a próxima linha.
    print('Você pode acessar o site.')
elif idade >= 16:
    print('Você pode acessar alguns conteúdos do site.')
else:
    print('Você não pode acessar o site por conta da idade.')

assistente_virtual = int(input('Digite o número 1 para jogar o primeiro jogo. Digite o número 2 para jogar o segundo jogo.'))

if assistente_virtual == 1:
    cor = int(input('Digite 1 para a cor do seu personagem ser vermelha. Digite 2 para ser amarela. Digite 3 para ser verde.'))
    if cor == 1:
        print('A cor do personagem é vermelha.')
    elif cor == 2:
        print('A cor do personagem vai ser amarela.')
    elif cor == 3:
        print('A cor do personagem vai ser verde.')
    else:
        print('Você digitou algo errado, tente novamente.')
elif assistente_virtual == 2:
    print('Segundo jogo')

cinema = True
ensolarado = False

# Operadores Lógicos

nao_ir_cinema = not cinema

if cinema == True and ensolarado == True: # O operador 'AND' serve para fazer 2 verificações dentro de um if/elif. Se uma delas for falsa, então o if não funcionará e passará para próxima linha.
    print('Eu vou ao cinema.')
elif cinema == True or ensolarado == True: # O operador 'OR' serve para fazer 2 verificações dentro de um if/elif. Se uma ou mais das verificações forem verdadeiras, então o código funciona. Se uma for verdadeira e a outra falsa, o código continua funcionando.
    print('Eu vou ao cinema.')
