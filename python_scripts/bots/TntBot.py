import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random
from Python_scripts.bots.PrimerBot import MinecraftAgent

class TntBot(MinecraftAgent):
    def __init__(self):
        super().__init__()  # Llama al constructor de la clase base

    def place_tnt(self, x, y, z):
        """Coloca un bloque de TNT en las coordenadas especificadas."""
        self.mc.setBlock(x, y, z, block.TNT.id, 1)  # Coloca TNT activable

    def explode_tnt(self, x, y, z):
        """Coloca fuego para activar el TNT y esperar la explosión."""
        self.mc.setBlock(x, y, z, block.FIRE.id)  # Coloca fuego para activar el TNT

    def random_tnt_placement(self, radius=5):
        """Coloca TNT aleatoriamente cerca del jugador y lo explota."""
        # Obtén la posición del jugador
        pos = self.mc.player.getTilePos()
        player_x, player_y, player_z = pos.x, pos.y, pos.z

        # Genera coordenadas aleatorias dentro de un radio alrededor del jugador
        tnt_x = player_x + random.randint(-radius, radius)
        tnt_y = player_y
        tnt_z = player_z + random.randint(-radius, radius)

        # Coloca TNT y luego lo explota
        print(f"Colocando TNT en: ({tnt_x}, {tnt_y}, {tnt_z})")
        self.place_tnt(tnt_x, tnt_y, tnt_z)
        time.sleep(2)  # Espera 2 segundos antes de explotar el TNT
        self.explode_tnt(tnt_x, tnt_y, tnt_z)

if __name__ == "__main__":
    # Crear una instancia del bot
    tnt_bot = TntBot()

    # Bucle principal para colocar TNT continuamente
    try:
        while True:
            tnt_bot.random_tnt_placement(radius=10)  # Cambia el radio si deseas mayor alcance
            time.sleep(5)  # Espera 5 segundos antes de colocar otro TNT
    except KeyboardInterrupt:
        print("Bot detenido manualmente.")