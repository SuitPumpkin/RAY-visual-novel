# Define personajes y nombres
define ray = Character("Ray")
define padre = Character("Padre")
define narrador = Character(None)  # narrador sin nombre
# Definir imagenes
image ray confused = "images/Ray_confused.png"
image ray talking = "images/Ray_talking.png"
image ray neutral = "images/Ray_neutral.png"

#Definir posiciones
define center = Position(xalign=0.5, yalign=-1.5)
define left = Position(xalign=-0.1, yalign=-1.5)
define right = Position(xalign=1.2, yalign=-1.5)

# Inicio del juego
label start:
    scene black
    play sound "bg-steam-motor-loopeable.ogg" loop
    pause 1
    narrador "El sonido del vapor era lo único constante en New Braithe City."
    narrador "CAPITULO 1: LA RATA CON TINER Y OTRAS HISTORIAS COTIDIANAS"
    stop sound fadeout 1.0
    scene bg_cuarto_destrozado with fade
    $ renpy.movie_cutscene("videos/Intro.webm")
    show ray neutral at center with fade
    ray "Hola... Mi nombre es Raymundo, y esta..."
    show ray talking at left with move
    ray "esta es mi vida."
    show ray neutral with dissolve
    narrador "El cuarto está destrozado. Tuberías rotas, una prótesis sin terminar, y él en medio de todo eso."
    show ray talking with dissolve
    ray "Mi vida de mierda."

    play music "rock_intro.ogg" fadein 1.0

    # Montaje corto del dia de ray
    narrador "Aqui iría un montaje de fondo mostrando el dia de Ray. (PENDIENTE)"

    ray "Desde que terminé la escuela a los 16, mi vida ha sido esto…"
    ray "Buscar chamba, sobrevivir y... tratar de que el viejo no se muera antes de que yo consiga pagar la renta."
    stop music fadeout 5.0
    show ray confused with dissolve
    ray "Papá enfermó hace ya un año. Cada día puede trabajar menos. Así que… me toca a mí."
    ray "He hecho de todo: cargar chatarra, limpiar calderas, hasta cuidar autómatas borrachos… pero nada dura."

    narrador "AQUI SEGUIRIA EL RESTO DE LA HISTORIA..."
    #etc...