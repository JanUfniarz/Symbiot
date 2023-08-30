from container import Container


class ContainerFactory:

    def __init__(self, dao):
        self.dao = dao

    def from_entity(self, entity) -> Container:
        previous = self.dao.get_container_by_id(entity.previous)
