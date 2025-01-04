import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

class MinecraftAgent:
    def __init__(self):
        # Conectar al servidor de Minecraft
        self.mc = minecraft.Minecraft.create()
        print("Conectado al servidor de Minecraft.")

    def send_message(self, message):
        # Enviar un mensaje al chat de Minecraft
        self.mc.postToChat(message)

    def place_block(self, x, y, z, block_type):
        # Colocar un bloque en las coordenadas dadas
        self.mc.setBlock(x, y, z, block_type)

    def destroy_block(self, x, y, z):
        # Destruir un bloque (reemplazarlo con aire)
        self.mc.setBlock(x, y, z, block.AIR.id)

    def get_player_position(self):
        # Obtener la posición actual del jugador
        return self.mc.player.getTilePos()

    def move_player(self, dx, dy, dz):
        # Mover al jugador a una nueva posición relativa
        pos = self.get_player_position()
        self.mc.player.setTilePos(pos.x + dx, pos.y + dy, pos.z + dz)

    def move_and_build(self, start_pos, length=5, height=3):
        # Construir un túnel o pasillo
        x, y, z = start_pos.x, start_pos.y, start_pos.z
        for i in range(length):
            for h in range(height):
                # Crear paredes
                self.place_block(x + i, y + h, z - 1, block.STONE.id)
                self.place_block(x + i, y + h, z + 1, block.STONE.id)
            # Crear techo y suelo
            self.place_block(x + i, y + height, z, block.STONE.id)
            self.place_block(x + i, y - 1, z, block.STONE.id)
        self.send_message(f"He construido un túnel de {length} bloques de largo.")

    def handle_command(self, command, *args):
        # Procesar comandos dinámicamente usando reflexión
        try:
            method = getattr(self, f"command_{command}")
            method(*args)
        except AttributeError:
            self.send_message(f"Comando '{command}' no reconocido.")
        except Exception as e:
            self.send_message(f"Error al ejecutar el comando '{command}': {e}")

    def command_tunel(self):
        pos = self.get_player_position()
        self.move_and_build(pos)

    def command_mover(self, dx, dy, dz):
        self.move_player(int(dx), int(dy), int(dz))
        self.send_message(f"Te he movido a {dx}, {dy}, {dz}.")

    def command_destruir(self):
        pos = self.get_player_position()
        self.destroy_block(pos.x + 1, pos.y, pos.z)
        self.send_message("He destruido el bloque frente a ti.")

    def command_adios(self):
        self.send_message("¡Adiós, nos vemos pronto!")
        raise StopIteration

    def command_insultbot(self):
        # Lista de insultos
        insults = [
            "¡Eres más lento que un caracol!",
            "¿De verdad eso es lo mejor que puedes hacer?",
            "¡He visto ovejas más inteligentes que tú!",
            "¿Acaso estás perdido?",
            "¡Tu construcción parece un queso suizo!",
        ]
        # Elegir un insulto aleatorio
        insult = random.choice(insults)
        self.send_message(insult)

    def interactive_chat(self):
        # Responder a comandos en el chat usando reflexión
        self.send_message("Dime 'túnel', 'mover dx dy dz', 'destruir', o 'insultbot'.")
        while True:
            try:
                chat_events = self.mc.events.pollChatPosts()
                for event in chat_events:
                    parts = event.message.lower().split()
                    command = parts[0]
                    args = parts[1:]
                    self.handle_command(command, *args)
            except StopIteration:
                break

if __name__ == "__main__":
    # Crear una instancia del agente
    agent = MinecraftAgent()

    # Enviar un mensaje de saludo
    agent.send_message("Hola, Minecraft! Estoy listo para ayudarte.")

    # Esperar un momento antes de comenzar
    time.sleep(2)

    # Habilitar interacciones en el chat
    agent.interactive_chat()
