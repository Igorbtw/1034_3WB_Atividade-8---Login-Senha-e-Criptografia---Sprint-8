def valida_email(email):
    return email[-8:] == "@puc.com"


def possuiMaiuscula(palavra):
    for letra in palavra:
        if 'A' <= letra <= 'Z': #letra.isupper
            return True #Retorna True se a alguma letra na palavra estiver no range de "A" ate "Z"
        return False

def possuiminuscala(palavra):
    for letra in palavra:
        if 'a' <= letra <= 'z': #letra.isupper
            return True  #Retorna True se a alguma letra na palavra estiver no range de "a" ate "z"
        return False

def possuinumero(palavra):
    for caracter in palavra:
        if '0' <= caracter <= '9':
            return True  #Retorna True se a alguma letra na palavra estiver no range de "0" ate "9"
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

def criptografa_senha(senha):
    senha_cripto = ""
    for char in senha:
        if char.isdigit():
            ref = ord('0')
            ascii_char = ord(char) #etapa 1
            pos_alpha = ascii_char - ref #etapa 2
            pos_cesar = pos_alpha + 3 #etapa 3
            pos_cesar = pos_cesar % 10 #etapa 4
            letra_cesar = chr(ref + pos_cesar) #etapa 5
            senha_cripto += letra_cesar
        elif 'A' <= char <= 'Z':
            ref = ord('A')
            ascii_char = ord(char) #etapa 1
            pos_alpha = ascii_char - ref #etapa 2
            pos_cesar = pos_alpha + 3 #etapa 3
            pos_cesar = pos_cesar % 26 #etapa 4
            letra_cesar = chr(ref + pos_cesar) #etapa 5
            senha_cripto += letra_cesar
        elif 'a' <= char <= 'z':
            ref = ord('a')
            ascii_char = ord(char) #etapa 1
            pos_alpha = ascii_char - ref #etapa 2
            pos_cesar = pos_alpha + 3 #etapa 3
            pos_cesar = pos_cesar % 26 #etapa 4
            letra_cesar = chr(ref + pos_cesar) #etapa 5
            senha_cripto += letra_cesar
        else:
            senha_cripto += char
    return senha_cripto

            
