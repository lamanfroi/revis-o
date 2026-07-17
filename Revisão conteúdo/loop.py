import time

#loop = True
# while loop:
#    assistente_virtual = int(input('Digite 1 para saber a hora do dia. Digite 2 para qualquer coisa. Digite 3 para qualquer coisa'))
#    if assistente_virtual == 1:
#        tempo_atual = time.ctime()
#        print(tempo_atual)
#    elif assistente_virtual == 2:
#        print('qualquer coisa')
#    elif assistente_virtual == 3:
#        print('Qualquer coisa')

for i in range(10):
    assistente_virtual = int(input('Digite 1 para saber a hora do dia. Digite 2 para qualquer coisa. Digite 3 para quebrar o loop.'))
    if assistente_virtual == 1:
        tempo_atual = time.ctime()
        print(tempo_atual)
    elif assistente_virtual == 2:
        print('qualquer coisa')
    elif assistente_virtual == 3:
        print('Quebra de loop')
        break # O 'break' serve para quebrar o loop


# Loop while: Ocorre sempre que a variável do while (ou o próprio while) for verdadeiro. O loop continua infinitamente até que se quebre.
# Loop for: Ocorre em um determinado tamanho (range), podendo ser maior ou menor de acordo com o que o usuário quer. O loop pode ser para utilizando o break, porém, ele não é infinito, ele funciona apenas na quantidade que o usuário inseriu dentro dos parâmetros '()'.