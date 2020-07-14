segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
dia = segundos // 86400
segundos_rst = segundos % 86400
hora = segundos_rst // 3600
segundos_rst2 = segundos_rst % 3600
minutos = segundos_rst2 // 60
segundos_final = segundos_rst2 % 60
print(str(dia) + " dias, " + str(hora) + " horas, " + str(minutos) + " minutos e " + str(segundos_final) + " segundos.")