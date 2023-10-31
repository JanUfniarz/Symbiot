from injector import singleton

from symbiot_lib.components.symbiot_division import SymbiotDivision
from symbiot_server.control.ps_command_generator import PSCommandGenerator
from symbiot_server.control.services.action_service import ActionService


class ActionDivision(SymbiotDivision):
    def configure(self, binder):
        binder.bind(ActionService, scope=singleton)
        binder.bind(PSCommandGenerator, scope=singleton)
