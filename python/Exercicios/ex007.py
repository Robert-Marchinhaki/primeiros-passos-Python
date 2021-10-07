# CALCULANDO A MÉDIA FINAL DE UM ALUNO EM DETERMINADA MATÉRIA

mnpu = float(input('Digite qual sua nota na prova1 dessa matéria:'))
mnpd = float(input('Digite qual sua nota na prova2 dessa matéria:'))
mnt = float(input('Digite qual sua nota nos trabalhos dessa matéria:'))
sn = mnpu + mnpd + mnt
medn = sn / 3
meso = medn * 2
print('Sua nota total nessa materia é {:.0f}, então sua média é {:.0f}'.format(sn, medn))

# exercio feito pelo professor

#n1 = float(input('Primeira nota do aluno:'))
#n2 = float(input('Segunda nota do aluno:'))
#media = (n1 + n2) / 2
#print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, media))