from api.base_resource import BaseResource


class AnalyzerResource(BaseResource):

    def post(self):
        return {'hello': 'guys'}
