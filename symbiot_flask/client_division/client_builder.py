from injector import inject

from client_division.client_factory import ClientFactory
from client_division.gpt.gpt_client import GPTClient
from client_division.gpt.gpt_client_entity import GPTClientEntity
from operation_division.record.step_record import StepRecord
from tool_kits.nord_star_extractor import NordStarExtractor
from tool_kits.tool_kit import ToolKit


def client_required(method):
    def wrapper(self, *args, **kwargs):
        if not self._client:
            raise Exception("No client, "
                            "use new() or from_() first")
        return method(self, *args, **kwargs)

    return wrapper


class ClientBuilder:

    @inject
    def __init__(self, factory: ClientFactory):
        self._client = None
        self._factory = factory

    def from_(self, client: GPTClient):
        self._client = client
        return self

    # noinspection PyTypeChecker
    def new(self, type_: str, template: str = None):
        if type_ == "gpt":
            if template:
                self._client = self._factory.gpt(template)
                match template:

                    case "calibrator":
                        self.add_access(NordStarExtractor(self))

            else:
                self._client = GPTClient()
        return self

    @client_required
    def build(self) -> GPTClient:
        return self._client

    @client_required
    def entity_data(self,
                    entity: GPTClientEntity,
                    sys_prompts=True):
        params = entity.__dict__.copy()
        prompts = params.pop("system_prompts")
        self.set_params(**params)
        if sys_prompts:
            self._client.messages += list(map(lambda prompt: dict(
                role="system", content=prompt), prompts))
        return self

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
