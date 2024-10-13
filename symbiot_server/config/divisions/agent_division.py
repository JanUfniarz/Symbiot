from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from injector import singleton

# noinspection PyPackages
from symbiot_lib.components.symbiot_division import SymbiotDivision
from symbiot_server.control.agent_builder import AgentBuilder
from symbiot_server.control.agent_factory import AgentFactory
from symbiot_server.control.services.agent_service import AgentService
from symbiot_server.endpoints.agent_endpoint import AgentEndpoint


class AgentDivision(SymbiotDivision):

    def configure(self, binder):
        binder.bind(AgentService, scope=singleton)
        binder.bind(AgentBuilder, scope=singleton)
        binder.bind(AgentFactory, scope=singleton)
        binder.bind(AgentEndpoint, scope=singleton)
        binder.bind(SQLAlchemy, to=self.db)
        binder.bind(Flask, to=self.app)
