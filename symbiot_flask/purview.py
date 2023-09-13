import json


class Purview:

    @staticmethod
    def purview_function(description, parameters):
        # parameters are (type, name, description, required)
        def decorator(func):
            func.purview = True
            func.__doc__ = description
            func.parameters = json.dumps({
                "type": "object",
                "properties": {
                    param[1]: {
                        "type": param[0],
                        "description": param[2],
                    } for param in parameters
                },
                "required": [param[1] for param in parameters if param[2]]
            })
            return func
        return decorator

    @classmethod
    def get_functions(cls):
        return json.dumps([{
            "name": name,
            "description": method.__doc__,
            "parameters": json.loads(
                getattr(method, 'parameters', '{}'))
        } for name, method in cls.__dict__.items()
            if callable(method)
            and getattr(method, 'purview', True)],
            indent=4)
