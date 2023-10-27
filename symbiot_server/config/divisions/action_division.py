from injector import singleton

from symbiot_server.config.divisions.server_division import ServerDivision
from symbiot_server.control.ps_command_generator import PSCommandGenerator
from symbiot_server.control.services.action_service import ActionService


class ActionDivision(ServerDivision):
    def configure(self, binder):
        binder.bind(ActionService, scope=singleton)
        binder.bind(PSCommandGenerator, scope=singleton)
