class InMemoryDB:
    def get(self, key: str):
        raise NotImplementedError

    def put(self, key: str, val: int):
        raise NotImplementedError

    def begin_transaction(self):
        raise NotImplementedError

    def commit(self):
        raise NotImplementedError

    def rollback(self):
        raise NotImplementedError


class InMemoryDBImpl(InMemoryDB):
    def __init__(self):
        self.mainDataStore = {}
        self.transactionDataStore = {}
        self.inTransaction = False

    def get(self, key: str):
        # only return committed info
        return self.mainDataStore.get(key, None)

    def put(self, key: str, val: int):
        # put can only be done during transaction
        if not self.inTransaction:
            raise Exception("No active transaction. Cannot call put().")
        self.transactionDataStore[key] = val

    def begin_transaction(self):
        if self.inTransaction:
            raise Exception("Transaction already in progress.")
        self.inTransaction = True
        self.transactionDataStore.clear()

    def commit(self):
        if not self.inTransaction:
            raise Exception("No active transaction to commit.")
        # commit
        for k, v in self.transactionDataStore.items():
            self.mainDataStore[k] = v
        # end
        self.inTransaction = False
        self.transactionDataStore.clear()

    def rollback(self):
        if not self.inTransaction:
            raise Exception("No active transaction to rollback.")
        # discard
        self.transactionDataStore.clear()
        self.inTransaction = False
