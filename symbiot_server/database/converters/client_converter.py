from objects.gpt_client import GPTClient
from client_division.gpt.gpt_client_entity import GPTClientEntity


class ClientConverter:
    @staticmethod
    def to_entity(client: GPTClient) -> GPTClientEntity:
        return GPTClientEntity(client)

    @staticmethod
    def from_entity(entity: GPTClientEntity) -> GPTClient:
        args = entity.__dict__.copy()

        args["init_messages"] = [dict(
            role="system",
            content=prompt
        ) for prompt in args.pop("system_prompts")]

        if "_sa_instance_state" in args:
            args.pop("_sa_instance_state")

        return GPTClient(**args)
