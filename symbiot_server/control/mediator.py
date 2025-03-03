from injector import Injector


class Mediator:
    def __init__(self, injector: Injector):

        services = {}
        # noinspection PyProtectedMember
        for cls in injector.binder._bindings:
            if hasattr(cls, "division_name"):
                services[getattr(cls, "division_name")] = cls

        # noinspection PyTypeChecker
        self._services = {name: injector.get(service) for name, service in services.items()}

        for service in self._services.values():
            service.set_mediator(self)

    def __call__(self, name: str):
        return self._services[name]
