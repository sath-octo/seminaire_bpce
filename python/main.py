import utils.utils as utils
import utils.departements as departements
import utils.taxons as taxons
#
import requests
import os

BASE_URL = os.environ.get('API_URL')
API_VERSION="v1"

def consume_api(options):
    url = "%s/%s/observations" % (BASE_URL, API_VERSION)

    isFirst = True
    for option in options:
        if isFirst:
            url += "?"
            isFirst = False
        else:
            url += "&"
        url += "%s=%s" % (option, options[option])

    response = requests.get(url)
    return response.json()["data"]

if __name__ == "__main__":
    DATE_MIN = "2018-01-01T00:00:01Z"
    DATE_MAX = "2022-01-01T00:00:01Z"

    data = consume_api({
        "code_departement": departements.CODE_DEPARTEMENT_BAS_RHIN,
        "date_operation_min": DATE_MIN,
        "date_operation_max": DATE_MAX,
        "nom_commun_taxon": taxons.TAXON_PERCHE
    })

    print("Nombre de Perches pêchés dans l'Indre et Loire entre 2018 et 2022: %s" % len(data))