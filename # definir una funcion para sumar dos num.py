# definir una funcion para sumar dos numeros 
def restar(num1, num2):
    if num1 >0 and num2 >0:
        resta = num1 - num2
        return f"la resta de {num1} y {num2}es:{resta}"
    else:
        return "ambos numeros deben ser mayores que cero"
    
# solicitar al usuario numeros 
num1 = float(input("ingrese un numero: "))
num2 = float(input("ingrese un numero: "))

# la funcion debe mostrar resultado 
resultado = restar(num1, num2)
print(resultado)
