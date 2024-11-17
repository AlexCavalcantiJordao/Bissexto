# Script para determinar se um ano bissexto....

def eBissexto(a):
    if((a % 4 == 0) and (a % 100 != 0)):
        return True
    if((a % 4 == 0) and (a % 100 == 0) and (a % 400 == 0)):
        return True
    return False

ano = int(input("Digite o ano: "))
print(f"{ano} é Bissexto ? {eBissexto(ano)}")