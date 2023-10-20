import openai

from tool_kits.tool_kit import ToolKit


class GPTClient:
    def __init__(
            self,
            name: str = None,
            model: str = "gpt-3.5-turbo",
            functions=None,
            function_call: str = "auto",
            temperature: float = 1,
            n: int = 1,
            max_tokens: int = 3000,
            init_messages: list = None,
            tool_kit: ToolKit = None,
            id_: str = None
    ):
        self.name = name
        self.model = model
        self.functions = functions
        self.function_call = function_call
        self.temperature = temperature
        self.n = n
        self.max_tokens = max_tokens
        self.messages = [] \
            if not init_messages else init_messages
        self.tool_kit = tool_kit
        self.id = id_

    @staticmethod
    def set_api_key(api_key):
        openai.api_key = api_key

    def chat(self,
             message: str,
             role="user",
             full_response=False):
        result = None
        self.messages.append(dict(role=role, content=message))
        response = openai.ChatCompletion.create(**self._to_dict())
        self.messages.append(dict(role="assistant", content=response))
        if "function_call" in response["choices"][0]["message"]:
            output = self.tool_kit.execute(
                response["choices"][0]["message"]["function_call"])
            if output:
                self.messages.append(
                    dict(role="function", content=output))
                result = output
        else:
            result = response["choices"][0]["message"]["content"]
        return response if full_response else result

    def _to_dict(self) -> dict:
        res = self.__dict__.copy()
        if not self.functions:
            del res["functions"]
            del res["function_call"]
        del res["tool_kit"]
        del res["id"]
        del res["name"]
        return res
