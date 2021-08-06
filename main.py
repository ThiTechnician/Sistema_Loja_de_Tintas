# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantvalor_latas de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math
import tkinter
from tkinter import *

tela = Tk()
tela.title("Loja de Tintas Aquarela")


area = ""
valor_lata = 0
valor_galao = 0
area_pintada = 0
indicacao = 0

imagem = tkinter.PhotoImage(file="imagem.png")
imagem_menor = imagem.subsample(3,3)
w = tkinter.Label(tela, image=imagem_menor)
w.grid(column = 0, row = 0)



areatexto = tkinter.Label(tela, text="  Digite a área a ser pintada em m2: ")
valor_latatexto = tkinter.Label(tela, text="Digite o valor da lata: ")
valor_galaotexto = tkinter.Label(tela, text="  Digite o valor do galão: ")
indicacao_compra = tkinter.Label(tela, text=indicacao)
indicacao_compra.grid(column = 0, row = 4)


areatexto.grid(column=1, row=0)
valor_latatexto.grid(column=1, row=1)
valor_galaotexto.grid(column=1, row=2)
area = tkinter.Entry(tela, width=30, textvariable=area_pintada)
valor_lata = tkinter.Entry(tela, width=30, textvariable=valor_lata)
valor_galao = tkinter.Entry(tela, width=30, textvariable=valor_galao)
area.grid(column=2, row=0, padx=0)
valor_lata.grid(column=2, row=1, padx=0)
valor_galao.grid(column=2, row=2, padx=0)

tela.mainloop()

#inicio do bloco lógico_______________________________________________________________________________________
total_galao = 0
total_lata = 0
total_misto = 0
melhor_escolha = 0

area_pintada = tkinter.StringVar()
tinta_necessaria = float(area_pintada) / 6
print("Necessário ", round(tinta_necessaria, 3), "L", )

total_lata = math.ceil(tinta_necessaria / 18)
total_galao = math.ceil(tinta_necessaria / 3.6)

desperdicio_lata = (total_lata * 18) - tinta_necessaria
desperdicio_galao = (total_galao * 3.6) - tinta_necessaria

diferenca_recipiente = math.floor(total_galao / 5)

indicacao = ("{} latas e {} galões".format(diferenca_recipiente,math.ceil(total_galao%5) )  )

if desperdicio_galao < desperdicio_lata:
    print("Melhor escolha é comprar {} galões".format(total_galao))
else:
    print("Melhor escolha é comprar {} latas".format(total_lata))



print("    ", total_lata)
print("    ", total_galao)

#final do bloco lógico_______________________________________________________________________________________
