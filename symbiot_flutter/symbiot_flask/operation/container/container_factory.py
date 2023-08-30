from container import Container
from step_container import StepContainer
from script_container import ScriptContainer


class ContainerFactory:

    @staticmethod
    def from_entity(entity) -> Container:
        inputs = [Bridge(input_) for input_ in entity.inputs]
        outputs = None if entity.outputs is None else \
            [Bridge(output_) for output_ in entity]

        if entity.type_ == "step":
            return StepContainer(
                inputs,
                outputs=outputs,
                id_=entity.id,
                **entity.__dict__)
        elif entity.type_ == "script":
            return ScriptContainer(
                inputs,
                outputs=outputs,
                id_=entity.id,
                **entity.__dict__)


class Bridge:
    def __init__(self, formatted):
        self.level = 1

        def proper_type(t, d):
            match t:
                case "str": return d
                case "int": return int(d)
                case "bool": return bool(d)
                case "float": return float(d)
                case "list":
                    res = [proper_type(
                        *el.split(f"<@level{self.level}>"))
                                 for el in d.split("<@el>")]
                    self.level += 1
                    return res
                # TODO: add support for set and dict

        index, type_, data = formatted.split("<@bridge>")
        self.index = index
        self.data = proper_type(type_, data)
