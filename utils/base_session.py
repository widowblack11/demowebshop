from requests import Session, Response


class BaseSession(Session):
    def __init__(self, url):
        super(BaseSession, self).__init__()
        self.url = url

    def request(self, metod, url, **kwargs) -> Response:
        return super().request(metod, self.url + url, **kwargs)

