import pygame
import json
from datetime import datetime
from constantes import *
from funciones import *

pygame.init()
cuadro_texto = crear_elemento_juego(MEDIA_IMAGE_PREGUNTA,ANCHO_CUADRO,ALTO_CUADRO,200,200)

def mostrar_fin_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict,lista_rankings:list) -> str:
    retorno = "terminado"
    fondo_terminado = pygame.transform.scale(pygame.image.load(MEDIA_IMAGE_FONDO), PANTALLA)
    pantalla.blit(fondo_terminado, (0, 0))

    for evento in cola_eventos:
        if evento.type == pygame.KEYDOWN:
            limpiar_superficie(cuadro_texto,MEDIA_IMAGE_PREGUNTA,ANCHO_CUADRO,ALTO_CUADRO)
            tecla_presionada = pygame.key.name(evento.key)
            bloc_mayus = pygame.key.get_mods()
            
            if tecla_presionada == "backspace":
                datos_juego["nombre"] = datos_juego["nombre"][0:len(datos_juego["nombre"]) - 1]
            elif tecla_presionada == "space":
                datos_juego["nombre"] += " "
            elif len(tecla_presionada) == 1: 
                if bloc_mayus >= 8192 or bloc_mayus == 1 or bloc_mayus == 2 :
                    datos_juego["nombre"] += tecla_presionada.upper()
                else:
                    datos_juego["nombre"] += tecla_presionada
            elif tecla_presionada == "return":

                nombre = datos_juego["nombre"].strip()

                if len(nombre) >= 3 and nombre.replace(" ", "").isalpha():
                    nueva_partida = {
                        "nombre": nombre,
                        "puntaje": datos_juego["puntuacion"],
                        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }

                try:
                    with open("partidas.json", "r", encoding="utf-8") as archivo:
                        lista_json = json.load(archivo)
                except FileNotFoundError:
                    lista_json = []

                lista_json.append(nueva_partida)

                with open("partidas.json", "w", encoding="utf-8") as archivo:
                    json.dump(lista_json, archivo, indent=4)

                lista_rankings.clear()
                lista_rankings.extend(lista_json)

                reiniciar_estadisticas(datos_juego)
                retorno = "menu"
                
    pantalla.blit(cuadro_texto["superficie"],cuadro_texto["rectangulo"])
    
    mostrar_texto(pantalla,f"Usted obtuvo: {datos_juego['puntuacion']} puntos",(250,100),FUENTE_PREGUNTA)
    
    if datos_juego["nombre"] != "":
        limpiar_superficie(cuadro_texto,MEDIA_IMAGE_PREGUNTA,ANCHO_CUADRO,ALTO_CUADRO)
        mostrar_texto(cuadro_texto["superficie"],datos_juego['nombre'],(10,0),FUENTE_CUADRO,COLOR_BLANCO)

        if random.randint(1,2) == 1:
            mostrar_texto(cuadro_texto["superficie"],f"{datos_juego['nombre']}|",(10,0),FUENTE_CUADRO,COLOR_BLANCO)

    else:
        limpiar_superficie(cuadro_texto,MEDIA_IMAGE_PREGUNTA,ANCHO_CUADRO,ALTO_CUADRO)
        mostrar_texto(cuadro_texto["superficie"],"INGRESE SU NOMBRE",(10,10),FUENTE_RESPUESTA,"#8A7A7A")
        
    return retorno
