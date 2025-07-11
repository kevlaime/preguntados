import pygame
from constantes import *
from funciones import *

pygame.init()

boton_suma = crear_elemento_juego(MEDIA_IMAGE_MAS_VOLUMEN,60,60,420,200)
boton_resta = crear_elemento_juego(MEDIA_IMAGE_MENOS_VOLUMEN,60,60,20,200)
boton_volver = crear_elemento_juego(MEDIA_IMAGE_PREGUNTA,100,40,10,10)

def mostrar_ajustes(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    retorno = "ajustes"
    
    fondo_ajustes = pygame.transform.scale(pygame.image.load(MEDIA_IMAGE_FONDO), PANTALLA)
    pantalla.blit(fondo_ajustes, (0, 0))
    
    centro_x = PANTALLA[0] // 2
    centro_y = PANTALLA[1] // 2

    boton_suma["rectangulo"].center = (centro_x + 100, centro_y)
    boton_resta["rectangulo"].center = (centro_x - 100, centro_y)
    boton_volver["rectangulo"].topleft = (10, 10)

    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if boton_suma["rectangulo"].collidepoint(evento.pos):
                if datos_juego["volumen_musica"] <= 95:
                    datos_juego["volumen_musica"] += 5
                    CLICK_SONIDO.play()
                else:
                    ERROR_SONIDO.play()
            elif boton_resta["rectangulo"].collidepoint(evento.pos):
                if datos_juego["volumen_musica"] > 0:
                    datos_juego["volumen_musica"] -= 5
                    CLICK_SONIDO.play()
                else:
                    ERROR_SONIDO.play()
            elif boton_volver["rectangulo"].collidepoint(evento.pos):
                retorno = "menu"
                CLICK_SONIDO.play()
             
    pantalla.blit(boton_suma["superficie"],boton_suma["rectangulo"])
    pantalla.blit(boton_resta["superficie"],boton_resta["rectangulo"])
    pantalla.blit(boton_volver["superficie"],boton_volver["rectangulo"])
    
    mostrar_texto(pantalla, "VOLUMEN DE LA MÚSICA", (centro_x - 120, centro_y - 70), FUENTE_RESPUESTA)
    mostrar_texto(pantalla, f"{datos_juego['volumen_musica']} %", (centro_x - 30, centro_y - 30), FUENTE_VOLUMEN)
    mostrar_texto(boton_volver["superficie"],"VOLVER",(5,5),FUENTE_RESPUESTA,COLOR_BLANCO)
    
    return retorno
