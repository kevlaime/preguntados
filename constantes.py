import pygame
pygame.init()

ANCHO_VENTANA = 800
ALTO_VENTANA = 600
PANTALLA = (ANCHO_VENTANA,ALTO_VENTANA)
FPS = 30

CANTIDAD_VIDAS = 3
PUNTUACION_ACIERTO = 100
PUNTUACION_ERROR = 25

COLOR_BLANCO = (255,255,255)
COLOR_NEGRO = (0,0,0)
COLOR_VERDE = (0,255,0)
COLOR_ROJO = (255,0,0)
COLOR_AZUL = (18,58,240)
COLOR_VIOLETA = (134,23,219)

ANCHO_PREGUNTA = 350
ALTO_PREGUNTA = 150
ANCHO_BOTON = 250
ALTO_BOTON = 60
ANCHO_CUADRO = 250
ALTO_CUADRO = 50
CUADRO_TEXTO = (250,50)

TAMAÑO_BOTON_VOLUMEN = (60,60)
TAMAÑO_BOTON_VOLVER = (100,40)
CLICK_SONIDO = pygame.mixer.Sound("media/audio/mouse-click.mp3")
ERROR_SONIDO = pygame.mixer.Sound("media/audio/error.mp3")
MUSICA_JUEGO = pygame.mixer.Sound("media/audio/game-music.mp3")
FUENTE_PREGUNTA = pygame.font.SysFont("Arial",30,True)
FUENTE_RESPUESTA = pygame.font.SysFont("Arial",20,True)
FUENTE_TEXTO = pygame.font.SysFont("Arial",25,True)
FUENTE_VOLUMEN = pygame.font.SysFont("Arial",50,True)
FUENTE_CUADRO = pygame.font.SysFont("Arial",40,True)
MEDIA_IMAGE_ICONO = "media/image/icono.png"
MEDIA_IMAGE_FONDO = "media/image/fondo.png"
MEDIA_IMAGE_PREGUNTA = "media/image/boton-pregunta.png"
MEDIA_IMAGE_RESPUESTA = "media/image/boton-respuesta.png"


BOTON_JUGAR = 0
BOTON_CONFIG = 1
BOTON_PUNTUACIONES = 2
BOTON_SALIR = 3

CANTIDAD_VIDAS = 3
PUNTUACION_ACIERTO = 100
PUNTUACION_ERROR = 25
TIEMPO_JUEGO = 30