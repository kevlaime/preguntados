import pygame
from constantes import *
from preguntas import *
from funciones import *

pygame.init()

fondo_pantalla = pygame.transform.scale(pygame.image.load(MEDIA_IMAGE_FONDO),PANTALLA)
cuadro_pregunta = crear_elemento_juego(MEDIA_IMAGE_PREGUNTA,ANCHO_PREGUNTA,ALTO_PREGUNTA,80,80)
lista_respuestas = crear_respuestas_preguntados(MEDIA_IMAGE_PREGUNTA,ANCHO_BOTON,ALTO_BOTON,125,245)

evento_tiempo = pygame.USEREVENT 
pygame.time.set_timer(evento_tiempo,1000)

def mostrar_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict,lista_preguntas:list) -> str:    
    retorno = "juego"
    pregunta_actual = lista_preguntas[datos_juego["indice"]]
    
    if datos_juego["vidas"] == 0 or datos_juego["tiempo_restante"] == 0:
        print("GAME OVER")
        retorno = "terminado"
    
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                for i in range(len(lista_respuestas)):
                    if lista_respuestas[i]["rectangulo"].collidepoint(evento.pos):
                        respuesta = (i + 1)
                        if verificar_respuesta(datos_juego,pregunta_actual,respuesta) == True:
                            CLICK_SONIDO.play()
                        else:
                            ERROR_SONIDO.play()
                        
                        datos_juego["indice"] += 1
                        if datos_juego["indice"] >= len(lista_preguntas):
                            datos_juego["indice"] = 0
                            mezclar_lista(lista_preguntas)
                        
                        pregunta_actual = pasar_pregunta(lista_preguntas,datos_juego["indice"],cuadro_pregunta,lista_respuestas)                        
        elif evento.type == evento_tiempo:
            datos_juego["tiempo_restante"] -= 1

    pantalla.blit(fondo_pantalla,(0,0))
    pantalla.blit(cuadro_pregunta["superficie"],cuadro_pregunta["rectangulo"])

    for i in range(len(lista_respuestas)):
        pantalla.blit(lista_respuestas[i]["superficie"],lista_respuestas[i]["rectangulo"])
    
    #cuadro_pregunta["superficie"].blit(texto_pregunta,(0,0))
    mostrar_texto(cuadro_pregunta["superficie"],pregunta_actual["pregunta"],(10,10),FUENTE_PREGUNTA)
    mostrar_texto(lista_respuestas[0]["superficie"],pregunta_actual["respuesta_1"],(20,20),FUENTE_RESPUESTA,COLOR_BLANCO)
    mostrar_texto(lista_respuestas[1]["superficie"],pregunta_actual["respuesta_2"],(20,20),FUENTE_RESPUESTA,COLOR_BLANCO)
    mostrar_texto(lista_respuestas[2]["superficie"],pregunta_actual["respuesta_3"],(20,20),FUENTE_RESPUESTA,COLOR_BLANCO)
    
    mostrar_texto(pantalla,f"PUNTUACION: {datos_juego['puntuacion']}",(10,10),FUENTE_TEXTO)
    mostrar_texto(pantalla,f"VIDAS: {datos_juego['vidas']}",(10,40),FUENTE_TEXTO)
    mostrar_texto(pantalla,f"TIEMPO: {datos_juego['tiempo_restante']} seg",(300,10),FUENTE_TEXTO)
    
    return retorno
    