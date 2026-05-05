def valida_email(email):
    return email[-8:] == "@puc.com"

print(valida_email("igorrodrigues301107@puc.com"))

def possuiMaiuscula(palavra):
    for letra in palavra:
        if 'A' <= letra <= 'Z': #letra.isupper
            return True
        return False

def possuiminuscala(palavra):
    for letra in palavra:
        if 'a' <= letra <= 'z': #letra.isupper
            return True
        return False

def possuinumero(palavra):
    for caracter in palavra:
        if '0' <= caracter <= '9':
            return True
        return False



def valida_senha(senha):
    check_tamanho = len(senha) >= 8
    check_maiscula = possuiMaiuscula(senha)
    check_minuscula = possuiminuscala(senha)
    check_numero = possuinumero(senha)
    return check_tamanho and check_maiscula and check_minuscula and check_numero


print("\nTestando a 'valida_senha': " )
print(valida_senha("Abc@1234"))
print(valida_senha("BCA@1234"))
print(valida_senha("def@1234"))
print(valida_senha("def@abcd"))
print(valida_senha("Def1234"))

#1 passo pegar a letra e converter para decima("z" setinha 90)
# 2 passo substituir o valor decimal de 65 ("z" s 90 s 65 s 25)
# 3 passo somar 3 ao resultado de 2
# 4 passo obter o resto da divisão do resultado de 3 por 26(28 % 28 = 2)
# 5 passo somar o resto a 65 e converter valor de volta para letra(2+65 s 67 s letra)

def criptografo_senha(senha):
    for char in senha:
        if char.isdigit():
            # Copiar lògica do maisculo, trocando ref para '0'
            pass
        elif 'A' <= char <= 'Z':
            ref = ord ('A') #65
            ascii_char = ord(char) #Etapa 1
            pos_alpha = ascii_char - ref #etapa2
            pos_cesar = pos_alpha + 3 #Etapa3
            pos_cesar = pos_cesar %26 #Etapa4
            letra_cesar = chr(ref + pos_cesar) #5etapa
            senha_cripto += letra_cesar


        elif 'a' <= char <= 'z' :
             # Copiar lògica do maisculo, trocando ref para 'a'
            pass
        else:
            senha_cripto += char
            return senha_cripto
        
print(criptografo_senha("ZARALHAR@"))
            
