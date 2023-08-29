from container import Container


class ContainerFactory:

    def __init__(self, dao):
        self.dao = dao

    def from_entity(self, entity) -> Container:


