# Define personajes y nombres
define ray = Character("Ray")
define padre = Character("Padre")
define narrador = Character(None)  # narrador sin nombre

# Inicio del juego
label start:
    scene black
    $ renpy.movie_cutscene("videos/Intro.webm")
    play sound "bg-steam-motor-loopeable.ogg" loop
    pause 1
    show bg_room with fade

    narrador "El sonido del vapor era lo único constante en New Braithe City."
    narrador "Ray abre los ojos de golpe. El techo gotea, el cuarto huele a óxido."

    ray "Hola... Mi nombre es Raymundo, y esta... esta es mi vida."

    show ray tired with dissolve
    narrador "El cuarto está destrozado. Tuberías rotas, una prótesis sin terminar, y él en medio de todo eso."
    ray "Mi vida de mierda."

    # Música estilo rock
    play music "rock_intro.ogg" fadein 1.0

    # Montaje corto
    narrador "Desde que terminé la escuela a los 16, mi vida se resume en buscar trabajo."
    narrador "Papá enfermó hace un año, así que me toca traer algo a casa, aunque sea poco."

    # Mini tutorial o escena interactiva
    jump tutorial_recoleccion


label tutorial_recoleccion:
    scene bg_junkyard with fade
    play sound "metal_clank.ogg"

    narrador "Hoy toca recolectar piezas en el Chatarrero. No hay paga fija, solo lo que encuentres."
    ray "Vamos, Ray... quizá hoy sí sale algo decente."

    # Aquí podrías usar un menú o minijuego básico
    menu:
        "¿Qué hará Ray?"
        "Buscar entre la chatarra":
            $ resultado = "pan"
            narrador "Encuentras una bolsa con un pan de plátano y unas monedas oxidadas."
        "Seguir buscando piezas útiles":
            $ resultado = "metal"
            narrador "Solo piezas rotas y un par de tornillos. Día perdido."

    jump casa_noche


label casa_noche:
    scene bg_home_night with fade
    stop music fadeout 1.0
    play music "soft_ambient.ogg"

    narrador "Ray llega a casa. La lámpara parpadea entre sombras."
    ray "No conseguí nada hoy..."

    show padre neutral at left
    padre "Ahh, no te preocupes, hijo. La primera chamba nunca es fácil. A veces, ella te escoge."

    ray "Todo lo que conseguí hoy son diez pesos... y este tonto pan de plátano."
    padre "...¿Pan de qué?"
    ray "De plátano, ¿por?"

    padre "¡EL PAN! ¡CÓMETE EL PAN! ¡AHORA!"

    play sound "panic.ogg"
    show ray surprised
    ray "¿Qué demonios pasa?!"

    narrador "El padre prácticamente se lo mete a la fuerza. Ray mastica confundido."
    padre "Solo... cuida que tu hermana no lo toque, ¿sí?"

    scene black with fade
    show logo "game_logo.png"
    play music "main_theme.ogg"
    narrador "Capítulo 1: El pan de plátano y otras tragedias cotidianas."

    return
