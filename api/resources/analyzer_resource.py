import json
import base64

from flask import request

from api.resources.base_resource import BaseResource
from api.domain.plate_analyzer import PlateAnalyzer


class AnalyzerResource(BaseResource):

    def post(self):
        # TODO add logic for encoding file from json without saving into server
        f = request.files['image']
        analyzer = PlateAnalyzer()
        return {'plate_number': str(analyzer.get_plate_number(f))}
