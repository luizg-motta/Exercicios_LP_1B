a = float(input("Digite a altura da parede em metros: "))
l = float(input("Digite a largua da parede em metros: "))
area = (a*l)
tinta = (area/2)

print("Com altura de {} e largura de {} sua área é de {} e será necessário usar {} litros de tinta".format(a, l, (area), (tinta)))