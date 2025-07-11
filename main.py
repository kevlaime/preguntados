import pygame
import json
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

ventana = pygame.display.set_mode(PANTALLA)
run = True
reloj = pygame.time.Clock()

datos_juego ={"puntuacion":0,"vidas":3,"nombre":"",
              "tiempo_restante":TIEMPO_JUEGO,"volumen_musica":0,"indice":0, "racha": 0,
              "comodines":{
                    "bomba": True,
                    "x2" : True,
                    "doble_chance": True,
                    "pasar": True
                },
                "x2_activo": False,
                "doble_chance_activa": False,
                "intento_extra": False
            }

ventana_actual = "menu"
bandera_juego = False
mezclar_lista(lista_preguntas)

try:
    with open("partidas.json", "r", encoding="utf-8") as archivo:
        lista_rankings = json.load(archivo)
except FileNotFoundError:
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
            porcentaje_volumen = datos_juego["volumen_musica"] / 100
            pygame.mixer.music.load(MUSICA_JUEGO)
            pygame.mixer.music.set_volume(porcentaje_volumen)
            pygame.mixer.music.play(-1)
            bandera_juego = True
        ventana_actual = mostrar_juego(ventana,cola_eventos,datos_juego,lista_preguntas)
    elif ventana_actual == "ajustes":
        ventana_actual = mostrar_ajustes(ventana,cola_eventos,datos_juego)
        
    elif ventana_actual == "rankings":
        ventana_actual = mostrar_rankings(ventana,cola_eventos,lista_rankings)
    elif ventana_actual == "salir":
        print("SALIENDO DE LA APLICACION")
        run = False
    elif ventana_actual == "terminado":
        if bandera_juego == True:
            pygame.mixer.music.stop()
            bandera_juego = False
        
        ventana_actual = mostrar_fin_juego(ventana,cola_eventos,datos_juego,lista_rankings)
    
    pygame.display.flip()

pygame.quit()