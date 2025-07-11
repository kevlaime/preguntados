import pygame
from constantes import *
from funciones import *

pygame.init()
lista_botones = crear_botones_menu(MEDIA_IMAGE_PREGUNTA,ANCHO_BOTON,ALTO_BOTON,115,125,4)
fondo_menu = pygame.transform.scale(pygame.image.load(MEDIA_IMAGE_FONDO),PANTALLA)  
lista_nombres_botones = ["JUGAR","AJUSTES","RANKINGS","SALIR"]

def mostrar_menu(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event]) -> str:
    retorno = manejar_eventos(cola_eventos)
    dibujar_pantalla(pantalla)

    return retorno

def manejar_eventos(cola_eventos:list[pygame.event.Event]):
    retorno = "menu"
    
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                for i in range(len(lista_botones)):
                    if lista_botones[i]["rectangulo"].collidepoint(evento.pos):
                        CLICK_SONIDO.play()
                        if i == 0:
                            retorno = "juego"
                        elif i == 1:
                            retorno = "ajustes"
                        elif i == 2:
                            retorno = "rankings"
                        elif i == 3:
                            retorno = "salir"
    
    return retorno

def dibujar_pantalla(pantalla:pygame.Surface) -> None:
    pantalla.blit(fondo_menu,(0,0))
    for i in range(len(lista_botones)):
        pantalla.blit(lista_botones[i]["superficie"],lista_botones[i]["rectangulo"])
        mostrar_texto(lista_botones[i]["superficie"],lista_nombres_botones[i],(80,10),FUENTE_TEXTO,COLOR_BLANCO)