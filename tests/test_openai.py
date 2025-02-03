import unittest
from openai_integration import get_openai_response

class TestOpenAIIntegration(unittest.TestCase):

    def test_get_openai_response(self):
        prompt = "Qual será minha função?"
        response = get_openai_response(prompt)
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)

if __name__ == '__main__':
    unittest.main()