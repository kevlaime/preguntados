import pygame
from constantes import *
from preguntas import *
from funciones import *

pygame.init()

fondo_pantalla = pygame.transform.scale(pygame.image.load(MEDIA_IMAGE_FONDO),PANTALLA)
cuadro_pregunta = crear_elemento_juego(MEDIA_IMAGE_PREGUNTA,ANCHO_PREGUNTA,ALTO_PREGUNTA,80,80)
lista_respuestas = crear_respuestas_preguntados(MEDIA_IMAGE_PREGUNTA,ANCHO_BOTON,ALTO_BOTON,125,245)

boton_bomba = crear_elemento_juego("media/image/boton-bomba.png", 80, 50, 480, 150)
boton_x2 = crear_elemento_juego("media/image/boton-x2.png", 80, 50, 480, 210)
boton_doble = crear_elemento_juego("media/image/boton-doble.png", 80, 50, 480, 270)
boton_pasar = crear_elemento_juego("media/image/boton-pasar.png", 80, 50, 480, 330)

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
                        resultado = verificar_respuesta(datos_juego, pregunta_actual, respuesta)
                        if resultado is True:
                            CLICK_SONIDO.play()
                        elif resultado is False:
                            ERROR_SONIDO.play()

                        if resultado is not None:
                            datos_juego["indice"] += 1
                            if datos_juego["indice"] >= len(lista_preguntas):
                                datos_juego["indice"] = 0
                                mezclar_lista(lista_preguntas)

                            pregunta_actual = pasar_pregunta(lista_preguntas, datos_juego["indice"], cuadro_pregunta, lista_respuestas)


            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if boton_bomba["rectangulo"].collidepoint(evento.pos) and datos_juego["comodines"]["bomba"]:
                    datos_juego["comodines"]["bomba"] = False
                    opciones = [1, 2, 3]
                    opciones.remove(pregunta_actual["respuesta_correcta"])
                    opcion_a_ocultar = random.choice(opciones)
                    lista_respuestas[opcion_a_ocultar - 1]["superficie"] = pygame.Surface((0, 0))
                    
                elif boton_x2["rectangulo"].collidepoint(evento.pos) and datos_juego["comodines"]["x2"]:
                    datos_juego["comodines"]["x2"] = False
                    datos_juego["x2_activo"] = True

                elif boton_doble["rectangulo"].collidepoint(evento.pos) and datos_juego["comodines"]["doble_chance"]:
                    datos_juego["comodines"]["doble_chance"] = False
                    datos_juego["doble_chance_activa"] = True

                elif boton_pasar["rectangulo"].collidepoint(evento.pos) and datos_juego["comodines"]["pasar"]:
                    datos_juego["comodines"]["pasar"] = False
                    datos_juego["indice"] += 1
                    pregunta_actual = pasar_pregunta(lista_preguntas, datos_juego["indice"], cuadro_pregunta, lista_respuestas)
        elif evento.type == evento_tiempo:
            datos_juego["tiempo_restante"] -= 1

    pantalla.blit(fondo_pantalla,(0,0))
    pantalla.blit(cuadro_pregunta["superficie"],cuadro_pregunta["rectangulo"])
    pantalla.blit(boton_bomba["superficie"], boton_bomba["rectangulo"])
    pantalla.blit(boton_x2["superficie"], boton_x2["rectangulo"])
    pantalla.blit(boton_doble["superficie"], boton_doble["rectangulo"])
    pantalla.blit(boton_pasar["superficie"], boton_pasar["rectangulo"])

    for i in range(len(lista_respuestas)):
        pantalla.blit(lista_respuestas[i]["superficie"],lista_respuestas[i]["rectangulo"])
    
    mostrar_texto(cuadro_pregunta["superficie"],pregunta_actual["pregunta"],(10,10),FUENTE_PREGUNTA)
    mostrar_texto(lista_respuestas[0]["superficie"],pregunta_actual["respuesta_1"],(20,20),FUENTE_RESPUESTA,COLOR_BLANCO)
    mostrar_texto(lista_respuestas[1]["superficie"],pregunta_actual["respuesta_2"],(20,20),FUENTE_RESPUESTA,COLOR_BLANCO)
    mostrar_texto(lista_respuestas[2]["superficie"],pregunta_actual["respuesta_3"],(20,20),FUENTE_RESPUESTA,COLOR_BLANCO)
    
    aciertos = pregunta_actual.get("aciertos", 0)
    fallos = pregunta_actual.get("fallos", 0)
    veces = pregunta_actual.get("veces_preguntada", 0)
    porcentaje = round((aciertos / veces) * 100) if veces > 0 else 0

    mostrar_texto(pantalla, f"Estadísticas:", (10, 390), FUENTE_RESPUESTA)
    mostrar_texto(pantalla, f"Aciertos: {aciertos}", (10, 420), FUENTE_RESPUESTA)
    mostrar_texto(pantalla, f"Fallos: {fallos}", (10, 450), FUENTE_RESPUESTA)
    mostrar_texto(pantalla, f"Preguntada: {veces} veces", (10, 480), FUENTE_RESPUESTA)
    mostrar_texto(pantalla, f"Porcentaje de aciertos: {porcentaje}%", (10, 510), FUENTE_RESPUESTA)

    mostrar_texto(pantalla,f"PUNTUACION: {datos_juego['puntuacion']}",(10,10),FUENTE_TEXTO)
    mostrar_texto(pantalla,f"VIDAS: {datos_juego['vidas']}",(10,40),FUENTE_TEXTO)
    mostrar_texto(pantalla,f"TIEMPO: {datos_juego['tiempo_restante']} seg",(300,10),FUENTE_TEXTO)
    
    return retorno
    