a = int(input("Digite o valor do lado a: "))
b = int(input("Digite o valor do lado b: "))
c = int(input("Digite o valor do lado c: "))
if a < b+c and b < a+c and c < a+b:
    if a == b and b == c:
        print("Triângulo Equilátero")
    elif a == b or b == c or a == c:
        print("Triângulo Isósceles")
    elif a != b and b != c and a != c:
        print("Triângulo Escaleno")
else:
    print("Não é um triângulo")
