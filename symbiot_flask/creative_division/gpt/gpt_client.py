import openai


class GPTClient:
    def __init__(self, model="gpt-3.5-turbo",
                 functions=None, function_call="auto",
                 temperature=0.1, n=1, max_tokens=3000):
        self.model = model
        self.functions = functions
        self.function_call = function_call
        self.temperature = temperature
        self.n = n
        self.max_tokens = max_tokens
        self.messages = []

    @staticmethod
    def set_api_key(api_key):
        openai.api_key = api_key

    def chat(self, message: str, role="system"):
        self.messages.append({"role": role, "message": message})
        return openai.ChatCompletion(**self.__dict__.copy())
