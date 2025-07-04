import pygame
from constantes import *
from funciones import *
from rankings import *
from configuracion import *
from terminado import *
from menu import *
from juego import *

pygame.init()

pygame.display.set_caption("Preguntados")
icono = pygame.image.load(MEDIA_IMAGE_ICONO)
pygame.display.set_icon(icono)

# ventana = pygame.display.set_mode((PANTALLA))
# run = True
# datos_juego = {"puntuacion":0, "vidas":CANTIDAD_VIDAS, "nombre":None}
# reloj = pygame.time.Clock()
# #Evento de tiempo
# tiempo_1_s = pygame.USEREVENT + 1
# pygame.time.set_timer(tiempo_1_s,1000)
# tiempo_15_s = pygame.USEREVENT + 2
# pygame.time.set_timer(tiempo_15_s,15000,2)
# tiempo_restante = 30
# fuente = pygame.font.SysFont("Arial", 15, bold=True)
# texto = fuente.render(f"TIMER: {tiempo_restante}", True, COLOR_NEGRO)

ventana = pygame.display.set_mode(PANTALLA)
run = True
reloj = pygame.time.Clock()
datos_juego ={"puntuacion":0,"vidas":3,"nombre":"","tiempo_restante":TIEMPO_JUEGO,"volumen_musica":0,"indice":0}
ventana_actual = "menu"
bandera_juego = False
mezclar_lista(lista_preguntas)
#Deberia venir del json
lista_rankings = []

while run:
    reloj.tick(FPS)
    cola_eventos = pygame.event.get()
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            ventana_actual = "salir"
    
    if ventana_actual == "menu":
        ventana_actual = mostrar_menu(ventana,cola_eventos)
    elif ventana_actual == "juego":
        if bandera_juego == False:
            #MUSICA SOLO EN EL JUEGO
            porcentaje_volumen = datos_juego["volumen_musica"] / 100
            pygame.mixer.music.load(MUSICA_JUEGO)
            pygame.mixer.music.set_volume(porcentaje_volumen)
            pygame.mixer.music.play(-1)
            bandera_juego = True
        ventana_actual = mostrar_juego(ventana,cola_eventos,datos_juego,lista_preguntas)
    elif ventana_actual == "ajustes":
        ventana_actual = mostrar_ajustes(ventana,cola_eventos,datos_juego)
        
        #MUSICA EN TODO EL JUEGO
        # porcentaje_volumen = datos_juego["volumen_musica"] / 100
        # pygame.mixer.music.set_volume(porcentaje_volumen)
    elif ventana_actual == "rankings":
        ventana_actual = mostrar_rankings(ventana,cola_eventos,lista_rankings)
    elif ventana_actual == "salir":
        print("SALIENDO DE LA APLICACION")
        run = False
    elif ventana_actual == "terminado":
        if bandera_juego == True:
            #MUSICA EN SOLO EL JUEGO
            pygame.mixer.music.stop()
            bandera_juego = False
        
        ventana_actual = mostrar_fin_juego(ventana,cola_eventos,datos_juego,lista_rankings)
    
    pygame.display.flip()

pygame.quit()

# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
        
#         elif event.type == tiempo_1_s:
#             tiempo_restante -= 1
#             texto = fuente.render(f"TIMER: {tiempo_restante}", True, COLOR_NEGRO)
#             print("paso un segundo")
        
#         elif event.type == tiempo_15_s:
#             print("paso 15 segundos")
            
#     texto = fuente.render(f"TIMER: {tiempo_restante}", True, COLOR_NEGRO)
#     ventana.fill((COLOR_BLANCO))
#     ventana.blit(texto,(10,10))
#     pygame.draw.circle(ventana, COLOR_NEGRO,(100,400),50)

#     if tiempo_restante == 0:
#         run = False

#     pygame.display.update()