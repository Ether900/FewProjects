primeiro = int(input('Primeiro: '))
frequencia = int(input('Frequencia: '))
cont = 1  # um a mais do total é ele que conta as progressões
total = 0  # quantidade de vezes que a progressão é feita
mais = 10  # Considera o minimo de 10 progressões
while mais != 0:  # se colocar zero encerra o programa
    total += mais  # conta a partir dos 10 para dar o número final de progressões
    while cont <= total:  # junto com o mais dá quando o programa deve ser interrompido
        print(f'{primeiro}', end=' > ')
        primeiro += frequencia  # forma da progressão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos mais gostaria de ver [0 para encerrar]: '))
print(f'Progressão finalizada com {cont} termos')
