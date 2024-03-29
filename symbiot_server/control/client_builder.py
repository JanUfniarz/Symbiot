import copy

from injector import inject

from symbiot_lib.objects.gpt_client import GPTClient
from symbiot_lib.objects.step_record import StepRecord
from symbiot_lib.tool_kits.nord_star_extractor import NordStarExtractor
from symbiot_lib.tool_kits.tool_kit import ToolKit
from symbiot_server.control.client_factory import ClientFactory


def client_required(method):
    def wrapper(self, *args, **kwargs):
        if not self._client:
            raise Exception("No client, "
                            "use new() or existing() first")
        return method(self, *args, **kwargs)

    return wrapper


class ClientBuilder:

    @inject
    def __init__(self, factory: ClientFactory):
        self._client = None
        self._factory = factory

    def existing(self, client: GPTClient):
        self._client = client
        return self

    # noinspection PyTypeChecker
    def new(self, type_: str, template: str = None):
        if type_ == "gpt":
            if template:
                self._client = self._factory.gpt(template)
                match template:

                    case "calibrator":
                        client_copy = copy.copy(self._client)
                        extractor = NordStarExtractor(self)
                        self._client = client_copy
                        self.add_access(extractor)

            else:
                self._client = GPTClient()
        return self

    @client_required
    def get(self) -> GPTClient:
        return self._client

    @client_required
    def add_step(self, step: StepRecord):
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
        self._client.messages += messages
        return self

    @client_required
    def add_access(self, tool_kit: ToolKit):
        self._client.functions = tool_kit.access
        self._client.function_call = tool_kit.forced \
            if tool_kit.forced == "auto" \
            or tool_kit.forced == "none" \
            else {"name": tool_kit.forced}
        self._client.tool_kit = tool_kit
        return self

    @client_required
    def set_params(self, model: str = None,
                   temperature: float = None,
                   n: int = None,
                   max_tokens: int = None):
        if model is not None:
            self._client.model = model
        if temperature:
            self._client.temperature = temperature
        if n is not None:
            self._client.n = n
        if max_tokens is not None:
            self._client.max_tokens = max_tokens
        return self

    @client_required
    def add_sys_prompt(self, prompt: str):
        self._client.messages.append(dict(
            role="system",
            content=prompt))
        return self
