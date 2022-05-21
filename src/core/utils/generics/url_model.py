"""Just a Url Model that only returns the internal url"""


class Url:
    def __init__(self):
        self._URL: str

    def get_url(self):
        return self._URL
