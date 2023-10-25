class Operation:
    def __init__(self, id_: str, wish: str, nord_star: str,
                 leaf_summary_status: str, status: str,
                 name: str, body: str, records: list):
        self.records = records
        self.body = body
        self.name = name
        self.status = status
        self.leaf_summary_status = leaf_summary_status
        self.nord_star = nord_star
        self.wish = wish
        self.id = id_

    @staticmethod
    def from_json(json):
        # TODO: implement
        return Operation()

    def to_dict(self):
        res = self.__dict__.copy()
        if "_records" in res:
            res.pop("_records")
        res["records"] = list(map(
            lambda r: r.to_dict(),
            self.records))
        return res
