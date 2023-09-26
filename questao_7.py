valor_compra = float(input("Digite o valor da compra"))

if valor_compra > 100:
    desconto = valor_compra * 0.10
elif valor_compra >= 50:
    desconto = valor_compra * 0.05
else:
    desconto = 0.0

valor_total = valor_compra - desconto

print(f"Desconto: R${desconto:.2f}")
print(f"Valor total a pagar: R${valor_total:.2f}")