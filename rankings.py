import pygame
from constantes import *
from funciones import *

pygame.init()

boton_volver = crear_elemento_juego(MEDIA_IMAGE_PREGUNTA,100,40,10,10)

def mostrar_rankings(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],lista_rankings:list) -> str:
    retorno = "rankings"
    
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                CLICK_SONIDO.play()
                retorno = "menu"
    
    pantalla.fill(COLOR_BLANCO)
    pantalla.blit(boton_volver["superficie"],boton_volver["rectangulo"])
    mostrar_texto(pantalla,f"TOP 10",(150,200),FUENTE_VOLUMEN,COLOR_NEGRO)
    lista_ordenada = sorted(lista_rankings, key=lambda x: x["puntaje"], reverse=True)
    for i, partida in enumerate(lista_ordenada[:10]):
        texto = f"{i+1}. {partida['nombre']} - {partida['puntaje']} pts - {partida['fecha']}"
        mostrar_texto(pantalla, texto, (80, 150 + i*30), FUENTE_RESPUESTA)
    
    mostrar_texto(boton_volver["superficie"],"VOLVER",(5,5),FUENTE_RESPUESTA,COLOR_BLANCO)

    return retorno