from api.analyzer_resource import AnalyzerResource


class URL:
    def __init__(self, api, url):
        self.api = api
        self.url = url


URLS = [
    URL(AnalyzerResource, '/analyzer')
]