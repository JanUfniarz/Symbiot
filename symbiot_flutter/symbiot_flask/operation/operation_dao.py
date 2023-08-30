class OperationDAO:

    _db = None

    def __init__(self, db=None):
        if db is not None:
            self._db = db
        elif self._db is None:
            raise Exception('db not provided')

    @property
    def db(self):
        print("database distributed")
        return self._db

    def add_operation(self, operation):
        if self._db is None:
            raise Exception('db not provided to add')
        print("dao, add: " + operation.name)
        self._db.session.add(operation)
        self._db.session.commit()

    def get_container_by_id(self, id_):
        self._db.session.query().all()
