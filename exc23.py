aniversariante = input('aniversariante? (sim/nao)')
ingresso = input('tem inresso? (sim ou nao)')

if aniversariante == 'sim':
    aniversariante == True
else:
    aniversariante = False

if ingresso == 'sim':
    ingresso = True
else:
    ingresso = False

if aniversariante == True or ingresso == True:
    print ('acesso liberado')
else:
    print('acesso negado, compre um ingresso na portaria ou pelo site')
      