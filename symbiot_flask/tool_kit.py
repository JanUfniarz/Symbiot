import json


class ToolKit:

    @staticmethod
    def tool_function(description, parameters):
        # parameters are (type, name, description, required)
        def decorator(func):
            func.purview = True
            func.__doc__ = description
            func.parameters = json.dumps(dict(
                type="object",
                properties={
                    param[1]: dict(
                        type=param[0],
                        description=param[2]
                    ) for param in parameters
                }, required=[param[1] for param in parameters
                             if param[2]]))
            return func
        return decorator

    @classmethod
    def get_access(
            cls, excluded: list = None,
            to_specific: list = None):
        def include(name):
            if excluded:
                return name not in excluded
            if to_specific:
                return name in to_specific
            return name

        if excluded and to_specific:
            raise Exception("Incompatible parameters")
        excluded = [] if not excluded else excluded
        to_specific = [] if not to_specific else to_specific

        return json.dumps([dict(
            name=name,
            description=method.__doc__,
            parameters=json.loads(
                getattr(method, 'parameters', '{}')))
            for name, method in cls.__dict__.items()
            if callable(method)
            and getattr(method, 'purview', True)
            and include(name)],
            indent=4)
