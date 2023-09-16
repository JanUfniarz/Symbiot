from client_division.gpt.gpt_client import GPTClient
from operation_division.record.step_record import StepRecord
from tool_kit import ToolKit


class ClientBuilder:

    def __init__(self):
        self._client = None

    def new(self, client: GPTClient):
        self._client = client
        return self

    def build(self):
        print("client built\n===============\n" + str(self._client.__dict__))
        return self._client

    def add_step(self, step: StepRecord):
        self._null_check()

        messages = []
        for el in list(map(lambda entry: entry.split(
                "<@time>")[1],
                step.body.split("<@entry>")[1:])):
            messages.append(dict(
                role="user",
                content=el.split("<@res>")[0]))
            messages.append(dict(
                role="assistant",
                content=el.split("<@res>")[1]))
        self._client.messages = messages
        return self

    def add_access(self, tool_kit: ToolKit):
        self._null_check()
        self._client.functions = tool_kit.access
        self._client.function_call = tool_kit.forced \
            if tool_kit.forced == "auto" \
            or tool_kit.forced == "none" \
            else {"name": tool_kit.forced}
        self._client.tool_kit = tool_kit
        return self

    def set_params(self, model: str = None,
                   temperature: float = None,
                   n: int = None,
                   max_tokens: int = None):
        self._null_check()
        if model is not None:
            self._client.model = model
        if temperature:
            self._client.temperature = temperature
        if n is not None:
            self._client.n = n
        if max_tokens is not None:
            self._client.max_tokens = max_tokens

    def _null_check(self):
        if not self._client:
            raise Exception("No client, use new() first")

    # Idea: zrobić zapis klienta do bazy danych z relacją do stepu
