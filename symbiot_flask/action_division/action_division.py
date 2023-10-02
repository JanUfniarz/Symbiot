from injector import singleton

from action_division.action_service import ActionService
from action_division.ps_command_generator import PSCommandGenerator
from symbiot_division import SymbiotDivision


class ActionDivision(SymbiotDivision):
    def configure(self, binder):
        binder.bind(ActionService, scope=singleton)
        binder.bind(PSCommandGenerator, scope=singleton)
