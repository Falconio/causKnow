import requests
from requests.auth import HTTPBasicAuth
from requests_toolbelt import MultipartEncoder
import os
from falconio.settings import MEDIA_ROOT

url = 'http://localhost:3030/falconds/data?graph=default'

class FusekiRdfLoader:
    def __init__(self, rdffilename):
        rdfFile = open(os.path.join(MEDIA_ROOT, rdffilename), 'rb')
        rdfHttpData = MultipartEncoder(
            fields={'field0': (rdffilename, rdfFile, 'text/turtle')}
            )
        self.httpRequest = requests.post(url, data=rdfHttpData, auth=HTTPBasicAuth('admin', 'password'),
                          headers={'Content-Type': rdfHttpData.content_type})
    def httpResponse(self):
        response = self.httpRequest.status_code
        if response != 200:
            return "Failed ERROR <%s>" %(str(response))
        else:
            return 200

         
        
