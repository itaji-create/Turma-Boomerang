extra_hours = float(input("Digite as horas extras"))
missed_hours = float(input("Digite as horas faltadas"))

if extra_hours > (missed_hours * 1.5) :
    print("Bônus de R$ 500.00")
else:
    print("Sem bônus")