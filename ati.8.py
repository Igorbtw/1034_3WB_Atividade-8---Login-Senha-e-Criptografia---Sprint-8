import pygame
import sys
from pygame import *

init()


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


def abrir_jogo():

#fundo do dia para noite

 iraio_x = 140
timer = 0
running = True
clock = time.Clock()


invincible_png = image.load('invincible.png')

invincible_png = transform.scale(invincible_png, (200, 200))

invincible_font = font.Font("invinciblefont.TTF", 50)

texto = invincible_font.render("casa do invencível", True, (0, 0, 0))

mixer.music.load("dav4d.mp3")

mixer.music.play(-1)

window = display.set_mode((1280, 720))

among = mixer.Sound("amongus.mp3")
baby1 = mixer.Sound("baby1.mp3")
error = mixer.Sound("error.mp3")
triste = mixer.Sound("triste.mp3")


# Variáveis da nuvem (EXTRA)

nuvem_x = 800

nuvem_y = 100

velocidade_nuvem = 3

#loop principal 

relogio = time.Clock()

#programa para fazer o programa fechar com o X do windows

modo_fundo = False

uuu=255
iii=188
ooo=99
background_color = (uuu, iii, ooo)


aaa = (uuu-(600//5.75))
bbb = (iii+(600//25))
ccc = (ooo+(600//3.95))


while running:
    dt = clock.tick(60) / 1000 
    
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            running = False
            sys.exit()
        
        if ev.type == KEYDOWN:
            if ev.key == K_SPACE:
                modo_fundo = not modo_fundo

        
        if ev.type == MOUSEBUTTONDOWN:
            if ev.button == 2:
                if modo_fundo == True:
                    triste.play()
                else:
                    if raio_x > 0 and raio_x < 430:
                        baby1.play()
                    elif raio_x >= 430 and raio_x < 860:
                        among.play()
                    elif raio_x >= 860:
                        error.play()

    # Lógica das cores 
    if modo_fundo:
        background_color = (245, 178, 64)
    else:
        if raio_x < 600:
            
            r = max(0, min(255, uuu - (raio_x // 5.75)))
            g = max(0, min(255, iii + (raio_x // 25)))
            b = max(0, min(255, ooo + (raio_x // 3.95)))
            background_color = (r, g, b)
        else:
            r = max(0, min(255, aaa - ((raio_x - 600) // 5)))
            g = max(0, min(255, bbb - ((raio_x - 600) // 4.3)))
            b = max(0, min(255, ccc - ((raio_x - 600) // 4.5)))
            background_color = (r, g, b)


    # Teclas e Movimento
    keys = key.get_pressed()
    mouse_keys = mouse.get_pressed()

    keys = key.get_pressed()
    mouse_keys = mouse.get_pressed()

    if raio_x < 1350:
        if keys[K_d] or mouse_keys[0]: 
            raio_x = raio_x + 300 * dt
    if raio_x > 10:
        if keys[K_a] or mouse_keys[2]: 
            raio_x = raio_x - 300 * dt
                    

    # Movimento da nuvem
    nuvem_x += velocidade_nuvem
    if nuvem_x <= -300 or nuvem_x >= 1300: 
        velocidade_nuvem = -velocidade_nuvem

    # --- DESENHOS ---

    # Fundo (usando a cor dinâmica)
    window.fill(background_color)

    # Grama 
    draw.rect(window, (100, 150, 50), (0, 550, 1280, 170))

    # Sol
    mover_sol = (int(raio_x),150)


    draw.circle(window, (255, 255, 0), (raio_x, 150), 50)
    draw.line(window, (255, 255, 0), (raio_x, 80), (raio_x, 50), 5)
    draw.line(window, (255, 255, 0), (raio_x, 220), (raio_x, 250), 5)
    draw.line(window, (255, 255, 0), (raio_x-70, 150), (raio_x-100, 150), 5)
    draw.line(window, (255, 255, 0), (raio_x + 70, 150), (raio_x + 100, 150), 5)
    draw.line(window, (255, 255, 0), (raio_x - 50, 100), (raio_x - 75, 75), 5)
    draw.line(window, (255, 255, 0), (raio_x + 50, 200), (raio_x + 75, 225), 5)
    draw.line(window, (255, 255, 0), (raio_x - 50, 200), (raio_x - 75, 225), 5)
    draw.line(window, (255, 255, 0), (raio_x + 50, 100), (raio_x + 75 , 75), 5)

    # Casa 
    draw.rect(window, (245, 245, 220), (450, 350, 200, 200))
    draw.polygon(window, (60, 60, 60), [(450, 350), (550, 200), (650, 350)])
    draw.rect(window, (139, 69, 19), (560, 430, 60, 120)) 
    draw.circle(window, (0, 0, 0), (610, 490), 5) 
    draw.rect(window, (0, 0, 128), (480, 430, 60, 60)) 

    # Árvore
    draw.rect(window, (101, 67, 33), (830, 450, 40, 100)) 
    draw.circle(window, (34, 139, 34), (850, 400), 70) 

    # Nuvem Animada
    draw.circle(window, (255, 255, 255), (int(nuvem_x), nuvem_y), 30)
    draw.circle(window, (255, 255, 255), (int(nuvem_x) + 30, nuvem_y - 15), 40)
    draw.circle(window, (255, 255, 255), (int(nuvem_x) + 70, nuvem_y), 35)
    draw.circle(window, (255, 255, 255), (int(nuvem_x) + 40, nuvem_y + 15), 30)

    # invincible
    window.blit(invincible_png, (50, 310)) 

    # texto
    window.blit(texto, (400, 50))

display.update()


# TELA
largura = 1280
altura = 720
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('login')

# CORES
branco = (255, 255, 255)
preto = (0, 0, 0)
cinza = (180, 180, 180)
azul = (109, 109, 235)
fonte = pygame.font.SysFont("Arial", 30)

# INPUTS
tela_atual = "login"
mensagem = ""

texto_email = ""
texto_senha = ""
campo_ativo = None  # "email" ou "senha"

placeholder = 'Digite seu email aqui'
placeholder1 = 'Digite sua senha aqui (8 caracteres)'

input_rect = pygame.Rect(393, 303, 454, 40)
input_rect1 = pygame.Rect(393, 403, 454, 40)
bot_rec = pygame.Rect(510, 500, 200, 54)

def desenhar():
    tela.fill(branco)

    titulo = fonte.render('Faça seu login', True, preto)
    tela.blit(titulo, (530, 200))

    # CAIXAS
    pygame.draw.rect(tela, preto, input_rect, 2)
    pygame.draw.rect(tela, preto, input_rect1, 2)
    pygame.draw.rect(tela, azul, bot_rec)
    # EMAIL
    if texto_email == "" and campo_ativo != "email":
        texto_surface = fonte.render(placeholder, True, cinza)
    else:
        texto_surface = fonte.render(texto_email, True, preto)

    tela.blit(texto_surface, (input_rect.x + 10, input_rect.y + 5))

    # SENHA (com *)
    if texto_senha == "" and campo_ativo != "senha":
        texto_surface = fonte.render(placeholder1, True, cinza)
    else:
        senha_visivel = "*" * len(texto_senha)
        texto_surface = fonte.render(senha_visivel, True, preto)

    tela.blit(texto_surface, (input_rect1.x + 10, input_rect1.y + 5))


    if tela_atual == "login":
        pygame.draw.rect(tela, (0, 0, 0), bot_rec, 2)

        text_avancar = fonte.render('Avançar', True, branco)
        tela.blit(text_avancar, (560, 508))
        if mensagem != "":
            msg_surface = fonte.render(mensagem, True, (255, 0, 0))
            tela.blit(msg_surface, (450, 460))

    elif tela_atual == "menu":
        tela.fill(branco)
        abrir_jogo()

rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        # CLIQUE
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(evento.pos):
                campo_ativo = "email"
            elif input_rect1.collidepoint(evento.pos):
                campo_ativo = "senha"
            elif bot_rec.collidepoint(evento.pos):
                if valida_email(texto_email) and valida_senha(texto_senha):
                    tela_atual = "menu"
                    mensagem = ""
                else:
                    mensagem = "Email ou senha inválidos"
            else:
                campo_ativo = None

        # DIGITAÇÃO
        if evento.type == pygame.KEYDOWN and campo_ativo:
            if campo_ativo == "email":
                if evento.key == pygame.K_BACKSPACE:
                    texto_email = texto_email[:-1]
                else:
                    texto_email += evento.unicode

            elif campo_ativo == "senha":
                if evento.key == pygame.K_BACKSPACE:
                    texto_senha = texto_senha[:-1]
                else:
                    texto_senha += evento.unicode

     
        

    desenhar()
    pygame.display.flip()

pygame.quit()
sys.exit()
