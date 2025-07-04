import pygame
from constantes import *

pygame.init()

pygame.display.set_caption("Preguntados")
icono = pygame.image.load("media/image/icono.png")
pygame.display.set_icon(icono)

ventana = pygame.display.set_mode((PANTALLA))

run = True

datos_juego = {"puntuacion":0, "vidas":CANTIDAD_VIDAS, "nombre":None}

reloj = pygame.time.Clock()

#Evento de tiempo
tiempo_1_s = pygame.USEREVENT + 1
pygame.time.set_timer(tiempo_1_s,1000)
tiempo_15_s = pygame.USEREVENT + 2
pygame.time.set_timer(tiempo_15_s,15000,2)

tiempo_restante = 30
#Sonido
#sonido_click = pygame.mixer.Sound("")

#TEXTO
fuente = pygame.font.SysFont("Arial", 15, bold=True)
texto = fuente.render(f"TIMER: {tiempo_restante}", True, COLOR_NEGRO)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        elif event.type == tiempo_1_s:
            tiempo_restante -= 1
            texto = fuente.render(f"TIMER: {tiempo_restante}", True, COLOR_NEGRO)
            print("paso un segundo")
        
        elif event.type == tiempo_15_s:
            print("paso 15 segundos")
            
    texto = fuente.render(f"TIMER: {tiempo_restante}", True, COLOR_NEGRO)
    ventana.fill((COLOR_BLANCO))
    ventana.blit(texto,(10,10))
    pygame.draw.circle(ventana, COLOR_NEGRO,(100,400),50)

    if tiempo_restante == 0:
        run = False

    pygame.display.update()

pygame.quit()
