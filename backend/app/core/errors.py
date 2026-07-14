class MarketplaceError(Exception):
    def __init__(self, message: str, code: str = 'UNKNOWN_ERROR'):
        self.message = message
        self.code = code
        super().__init__(message)


class NotFoundError(MarketplaceError):
    pass


class TransactionError(MarketplaceError):
    pass
