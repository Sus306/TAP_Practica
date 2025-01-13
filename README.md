# TAP_Practica
El código contiene implementaciones de agentes para interactuar con el entorno de Minecraft a través de la API mcpi. Cada agente tiene funcionalidades específicas, como colocar y detonar bloques de TNT, responder preguntas, y emitir mensajes personalizados. Estas clases están diseñadas para extender una clase base que maneja las interacciones básicas con el servidor de Minecraft.
Clase: TntBot
Un agente especializado en colocar y detonar bloques de TNT en el mundo de Minecraft.
**__init__()** Constructor que inicializa el bot heredando funcionalidades de MinecraftAgent.
**place_tnt(x, y, z) **Coloca un bloque de TNT activable en las coordenadas especificadas.
**explode_tnt(x, y, z)** Activa el TNT colocando fuego en la misma posición.
**random_tnt_placement**(radius=5) Coloca TNT aleatoriamente dentro de un radio alrededor del jugador y lo detona tras una breve pausa.
Clase: InsultBot
Un bot diseñado para interactuar con los jugadores a través del chat. 
**command_insultbot() **Genera un insulto aleatorio de una lista predefinida y lo envía al chat.
**interactive_chat() **Escucha comandos en el chat y responde con insultos cuando recibe "insultbot".
Clase: Agent
Clase base para relizar operaciones comunes en Minecraft, como enviar mensajes, obtener/establecer bloques, y detectar posiciones.
**__init__(name) **Inicializa el agente con un nombre y crea una conexión con el servidor de Minecraft.
**post_message(message)** Envía un mensaje al chat del servidor.
**get_position() **Obtiene la posición actual del jugador.
**set_block(x, y, z, block_id) **Coloca un bloque específico en las coordenadas dadas.
**get_block(x, y, z)** Obtiene el tipo de bloque en una posición específica.
Clase: OracleBotLlista
Un bot que responde preguntas basándose en una base de conocimiento simple.
**__init__(name)** Inicializa el bot con una base de conocimiento y respuestas por defecto.
**match_question(question)** Busca una respuesta a una pregunta en la base de conocimiento o devuelve una respuesta por defecto.
**answer_question(question)** Publica una respuesta basada en la pregunta recibida.
**listen_for_questions() **Escucha eventos de chat y responde preguntas detectadas.
Se ha incluido el bot adicional, Pyro4, usa Pyro4 para la comunicación remota, permitiendo controlar sus funciones desde un cliente RPC.The project includes unit tests to verify the functionality of the bots.
