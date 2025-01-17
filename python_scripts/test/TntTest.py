import unittest
from unittest.mock import MagicMock
import mcpi.block as block
import random
import time
from bots import TntBot


class TestTntBot(unittest.TestCase):
    def setUp(self):
        """Configuramos el entorno de pruebas (mocking)."""
        self.bot = TntBot()

        # Mockear la instancia de Minecraft y sus métodos
        self.bot.mc = MagicMock()
        self.bot.mc.setBlock = MagicMock()
        self.bot.mc.player.getTilePos = MagicMock(return_value=MagicMock(x=10, y=64, z=10))

    def test_place_tnt(self):
        """Probar que la colocación de TNT funciona correctamente."""
        self.bot.place_tnt(10, 64, 10)
        self.bot.mc.setBlock.assert_called_once_with(10, 64, 10, block.TNT.id, 1)

    def test_explode_tnt(self):
        """Probar que el encendido de TNT funciona correctamente."""
        self.bot.explode_tnt(10, 64, 10)
        self.bot.mc.setBlock.assert_called_once_with(10, 64, 10, block.FIRE.id)

    def test_random_tnt_placement(self):
        """Probar que se coloca TNT aleatoriamente cerca del jugador."""
        # Mockear random.randint para que siempre devuelva un valor fijo
        random.randint = MagicMock(return_value=5)

        # Ejecutamos la función random_tnt_placement
        self.bot.random_tnt_placement(radius=5)

        # Verificar que los métodos se llamaron correctamente con las coordenadas esperadas
        self.bot.mc.setBlock.assert_any_call(15, 64, 15, block.TNT.id, 1)  # 10 + 5 en ambas direcciones
        self.bot.mc.setBlock.assert_any_call(15, 64, 15, block.FIRE.id)

    def test_sleep(self):
        """Verificar que la función de espera no bloquea el hilo."""
        start_time = time.time()
        self.bot.random_tnt_placement(radius=5)
        elapsed_time = time.time() - start_time
        # Verificar que el tiempo de espera es alrededor de 2 segundos
        self.assertGreater(elapsed_time, 1.8)
        self.assertLess(elapsed_time, 2.2)


if __name__ == "__main__":
    unittest.main()