nome = input("digite seu nome:")
materia = input("digite sua materia:")
n1 = int(input("digite sua nota:"))
n2 = int(input("digite sua nota 2:"))
m = (n1 + n2)/2
if m >=6:
    print(f'o usuario {nome} foi aprovdo na mteria de {materia} com a media {m}')
else:
    print(f'o usuario{nome} foi reprovado na máteria de {materia} com a media {m}')