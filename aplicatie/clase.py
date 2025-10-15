from datetime import datetime
from urllib.parse import urlparse, parse_qs
import locale
try:
    locale.setlocale(locale.LC_TIME, 'ro_RO.UTF-8')
except locale.Error:
    locale.setlocale(locale.LC_TIME, '')
class Accesare:
    _id_counter = 0 

    def __init__(self, ip_client, full_url):
        Accesare._id_counter += 1
        self.id = Accesare._id_counter
        self.ip_client = ip_client
        self._full_url = full_url
        self.timestamp = datetime.now()

    def lista_parametri(self):
        parsed_url = urlparse(self._full_url)
        query_params_dict = parse_qs(parsed_url.query)
        return [(key, value[0]) for key, value in query_params_dict.items()]

    def url(self):
        return self._full_url

    def data(self):
        return self.timestamp.strftime("%A, %d %B %Y, ora %H:%M:%S")

    def pagina(self):
        return urlparse(self._full_url).path