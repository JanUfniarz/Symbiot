from client_division.gpt.gpt_client import GPTClient
from operation_division.record.step_record import StepRecord


def to_client(step: StepRecord):
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
    return GPTClient(init_messages=messages)

    # Idea: zrobić zapis klienta do bazy danych z relacją do stepu
