class GoogleLibException(Exception):
    """Base exception for Google library errors."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message