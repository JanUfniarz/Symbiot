from operation.container.container_entity import db
from operation.container.container_converter import ContainerConverter
db = db

converter = ContainerConverter()


class Operation(db.Model):
    __tablename__ = 'operations'
    id = db.Column(
        db.Integer,
        primary_key=True,)
    wish = db.Column(db.Text)
    nord_star = db.Column(db.Text)
    leaf_summary_status = db.Column(db.Text, nullable=True)
    status = db.Column(db.String)
    name = db.Column(db.String)
    body = db.Column(db.Text)
    _containers = db.relationship(
        "ContainerEntity", backref="operations", lazy=True)

    def __init__(self, name, wish, containers, body, ):

        self.name = name
        self._containers = containers
        self.wish = wish
        self.nord_star = wish
        self.status = "CREATION_STARTED"
        self.body = body

    @property
    def containers(self):
        containers = [converter.from_entity(entity)
                      for entity in self._containers]

        for container in containers:
            if isinstance(container.previous, int):
                for it in containers:
                    if container.previous == it.id_:
                        container.previous = it.id_

        return containers

    def add_container(self, new):
        self._containers.append(converter.to_entity(new))

    def to_dict(self):
        res = self.__dict__.copy()
        res.pop("_sa_instance_state")
        res["containers"] = list(map(
            lambda c: c.to_dict(),
            self.containers))
        return res
