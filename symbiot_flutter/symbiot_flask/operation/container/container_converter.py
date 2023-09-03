from .step_container import StepContainer
from .script_container import ScriptContainer
from .container_entity import ContainerEntity


def type_to_string(container):
    if type(container) is ContainerEntity:
        return "entity"
    elif type(container) is StepContainer:
        return "step"
    elif type(container) is ScriptContainer:
        return "script"
    else:
        raise ValueError("Unsupported container type")


def from_entity(entity):
    inputs = [Bridge(input_) for input_ in entity.inputs]
    outputs = None if entity.outputs is None else \
        [Bridge(output_) for output_ in entity.outputs]
    args = entity.__dict__
    args.pop("inputs")
    args.pop("outputs")
    if entity.type_ == "step":
        return StepContainer(
            inputs,
            outputs=outputs,
            id_=entity.id,
            **args)
    elif entity.type_ == "script":
        return ScriptContainer(
            inputs,
            outputs=outputs,
            id_=entity.id,
            **args)


def to_entity(container) -> ContainerEntity:
    type_ = type_to_string(container)

    if type_ == "entity":
        return container

    return ContainerEntity(
        type_,
        inputs=[bridge.format() for bridge in container.inputs],
        outputs=[bridge.format() for bridge in container.outputs],
        **container.__dict__
    )


class Bridge:
    def __init__(self, formatted):
        def proper_type(t, d):
            match t:
                case "str": return d
                case "int": return int(d)
                case "bool": return bool(d)
                case "float": return float(d)
                case "list":
                    res = [proper_type(
                        *el.split(f"<@level{self.level}>"))
                        for el in d.split(f"<@el{self.level}>")]
                    self.level += 1
                    return res
                # TODO: add support for set and dict

        self.level = 1
        index, type_, data = formatted.split("<@bridge>")
        self.index = index
        self.data = proper_type(type_, data)

    def format(self):
        """
        1<b>list<b>
          str<l1>dupa<el1>
          int<l1>1

        2<b>list<b>
          list<l1>
              str<l2>pyra<el2>
              int<l2>3<el1>
          list<l1>
              str<l2>dupa<el2>
              int<l2>52
        """
        def data_format(d):
            if isinstance(d, (str, int, bool, float)):
                return str(d)
            elif isinstance(d, list):
                res = f"<@el{self.level}>".join(
                    [f"{str(type(x))}<level{self.level}>{data_format(x)}"
                     for x in d])
                self.level += 1
                return res
            # TODO: add support for set and dict
            raise NotImplementedError("Not implemented data type")

        self.level = 1
        return "<@bridge>".join([
            self.index,
            str(type(self.data)),
            data_format(self.data)])
