class BaseRecord:
    def __init__(self, id=None, record_id=None, **kwargs):
        self.id = id
        self.record_id = record_id
        self.fields = kwargs
