import unittest
from unittest.mock import MagicMock
from time import sleep
from bots import OracleBotLlista

class TestOracleBot(unittest.TestCase):

    def setUp(self):
        """Configurar las instancias y mocks necesarios."""
        # Crear una instancia del bot
        self.bot = OracleBotLlista(name="TestOracleBot")

        # Mock para la conexión de Minecraft (mc)
        self.bot.mc = MagicMock()

        # Mock para el evento de chat
        self.bot.mc.events.pollChatPosts = MagicMock(return_value=[])

    def test_match_question_found(self):
        """Verificar que match_question devuelve la respuesta correcta."""
        question = "How to build"
        expected_answer = "To build in Minecraft, gather resources, select a flat area, and start placing blocks creatively!"
        
        # Llamar al método
        answer = self.bot.match_question(question)

        # Verificar que la respuesta es la correcta
        self.assertEqual(answer, expected_answer)

    def test_match_question_default(self):
        """Verificar que match_question devuelve una respuesta predeterminada cuando no hay coincidencias."""
        question = "What is the weather?"
        
        # Llamar al método
        answer = self.bot.match_question(question)

        # Verificar que la respuesta sea una de las predeterminadas
        self.assertIn(answer, self.bot.default_responses)

    def test_answer_question(self):
        """Verificar que answer_question llama a post_message con la respuesta correcta."""
        question = "Diamonds"
        expected_answer = "Diamonds are usually found between layers 5 and 12. Mine carefully with an iron or better pickaxe."
        
        # Hacer un mock de post_message para verificar que se llame correctamente
        self.bot.post_message = MagicMock()

        # Llamar al método
        self.bot.answer_question(question)

        # Verificar que post_message se haya llamado con la respuesta correcta
        self.bot.post_message.assert_called_with(f"Q: {question} | A: {expected_answer}")

    def test_listen_for_questions(self):
        """Verificar que listen_for_questions maneja los eventos de chat correctamente."""
        # Simulamos un evento de chat
        chat_event = MagicMock()
        chat_event.message = "Diamonds"
        self.bot.mc.events.pollChatPosts = MagicMock(return_value=[chat_event])

        # Hacer un mock de post_message para verificar que se llama correctamente
        self.bot.post_message = MagicMock()

        # Llamar al método (solo una iteración para evitar bucles infinitos)
        self.bot.listen_for_questions()

        # Verificar que post_message se haya llamado correctamente
        self.bot.post_message.assert_called_with("Q: Diamonds | A: Diamonds are usually found between layers 5 and 12. Mine carefully with an iron or better pickaxe.")

if __name__ == "__main__":
    unittest.main()