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

    def add(self, entity):
        self._db.session.add(entity)


