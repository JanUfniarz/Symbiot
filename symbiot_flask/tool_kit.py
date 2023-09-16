import json


class ToolKit:
    def __init__(self,
                 forced: str = "auto",
                 excluded: list = None,
                 component=None):
        self._forced = forced
        self.excluded = excluded if excluded is not None else []
        self.component = component

    @property
    def forced(self):
        if self.component is not None \
            and self.component.forced != "auto" \
                and self.component.forced != "none":
            return self.component.forced
        return self._forced

    # noinspection PyUnresolvedReferences
    @forced.setter
    def forced(self, value):
        if hasattr(self, value):
            method = getattr(self, value)
            if callable(method) and getattr(method, 'accessible', False):
                self._forced = value
                return
        raise ValueError(f"there is no available method {value}")

    @property
    def auto_call(self) -> bool:
        return self._forced == "auto"

    # noinspection PyUnresolvedReferences
    @auto_call.setter
    def auto_call(self, value: bool):
        if value:
            self._forced = "auto"
        else:
            if self._forced == "auto":
                self._forced = "none"
            else:
                print("auto_call already off")

    @staticmethod
    def tool_function(description, parameters=None):
        # parameters are (type, name, description, required, enum)
        def decorator(func):
            def param_format(param: dict) -> dict:
                copy = param.copy()
                res = {}
                if "required" not in copy:
                    res["required"] = True
                else:
                    res["required"] = copy.pop("required")
                res["name"] = copy.pop("name")
                res["value"] = copy
                return res

            params = list(map(
                lambda x: param_format(x), parameters)) \
                if parameters else []

            func.accessible = True
            func.__doc__ = description
            # noinspection PyTypeChecker
            func.parameters = json.dumps(dict(
                type="object",
                properties={
                    param["name"]: param["value"] for param in params
                }, required=[param["name"] for param in params
                             if param["required"]]))
            return func
        return decorator

    @property
    def access(self):
        access = [dict(
            name=name,
            description=method.__doc__,
            parameters=json.loads(getattr(method, 'parameters', '{}')))
            for name, method in self.__class__.__dict__.items()
            if callable(method)
            and getattr(method, 'accessible', False)
            and name not in self.excluded]
        if self.component is not None:
            component_access = self.component.access
            match self.component.forced:
                case "auto": return component_access + access
                case "none": return access
                case _: return component_access
        return access

    def execute(self, call):
        name = call["name"]
        args = json.loads(call["arguments"])
        if hasattr(self, name) \
                and callable(getattr(self, name)):
            method = getattr(self, name)
            return method(**args)
        elif self.component is not None:
            return self.component.execute(call)
        else:
            raise Exception("Unknown function")
