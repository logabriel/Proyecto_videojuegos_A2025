# Jungle Hero (Platformer)

## Descripción

**Jungle Hero** es un juego de plataformas 2D desarrollado como proyecto final para la materia Programación de Videojuegos A2025. Combina desafíos clásicos del género con una innovadora mecánica de rescate cooperativo. El objetivo es rescatar a todas las chicas en cada nivel para avanzar de nivel y completar la aventura.

El juego cuenta con seis niveles, y la dificultad aumenta progresivamente a medida que se avanza. Cada nivel presenta distintos enemigos con velocidades variables, diseñados para obstaculizar el progreso del jugador. Además, el jugador debe completar cada nivel en el menor tiempo posible, ya que si el reloj llega a cero antes de rescatar a todas las chicas, se pierde.

**Hay varias formas de fracasar:**

- Si los enemigos te atrapan, pierdes.

- Si caes desde una altura muy alta, mueres.

- En cualquiera de estos casos, debes reiniciar desde el primer nivel.

- El juego está diseñado para ser desafiante, exigiendo precisión, estrategia y rapidez para superar cada obstáculo.

## Cómo jugar

- El objetivo principal es rescatar a todas las chicas en cada nivel para poder avanzar al siguiente.
- Esquiva o elimina criaturas enemigas.
- El juego termina si mueren un jugador o si se acaba el tiempo.

## Controles

### Jugador 1
- **Mover derecha:** D
- **Mover izquierda:** A
- **Mover arriba:** W
- **Mover abajo:** S
- **Saltar:** Espacio
- **Atacar:** E

### Jugador 2
- **Mover derecha:** Teclado numérico 6
- **Mover izquierda:** Teclado numérico 4
- **Mover arriba:** Teclado numérico 8
- **Mover abajo:** Teclado numérico 5
- **Saltar:** Teclado numérico 0
- **Atacar:** Teclado numérico 7

### Generales
- **Pausa:** P
- **Salir:** Esc
- **Aceptar/Continuar:** Enter

## Requisitos

- Python 3.8+
- Pygame
- Dependencias listadas en `requirements.txt`

## Ejecución

Para ejecutar el juego **Jungle Hero**, sigue estos pasos desde la terminal:

# Entra al directorio del proyecto
```
cd Proyecto_videojuegos_A2025
```
# Crea un entorno virtual de Python
```
python3 -m venv .venv
```
# Activa el entorno virtual
```
source .venv/bin/activate  # En Linux
```
# Instala las dependencias necesarias
```
pip install -r requirements.txt
```
# Ejecuta el juego
```
python main.py
```

## Créditos

- **Autores:** Gabriel Perez y Eugenia Ramirez

- **Año:** 2025  
- **Materia:** Programacion de Videojuegos 
- **Universidad:** Universidad de los Andes

## Créditos de gráficos

Los siguientes recursos gráficos gratuitos fueron utilizados en este proyecto:

- Enemigos y sprites: [Free Enemy Sprite Sheets - Pixel Art](https://free-game-assets.itch.io/free-enemy-sprite-sheets-pixel-art)  
- Tileset de pantano: [Free Swamp 2D Tileset - Pixel Art](https://free-game-assets.itch.io/free-swamp-2d-tileset-pixel-art)  
- Personajes: [Free 3 Character Sprite - Pixel Art](https://free-game-assets.itch.io/free-3-character-sprite-pixel-art)

Agradecemos a los autores de estos recursos por compartir su trabajo bajo licencias que permiten su uso educativo y no comercial.

### Recursos

- Motor base: [Gale Engine](https://github.com/alejandromujica/gale)

## Licencia

Este proyecto es solo para fines educativos y no debe ser distribuido comercialmente.

---
