import utils.utils as utils
import utils.departements as departements
import utils.taxons as taxons
#
import requests

BASE_URL="http://127.0.0.1:3030"
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
    return response.json()

if __name__ == "__main__":
    DATE_MIN = "2018-01-01T00:00:01Z"
    DATE_MAX = "2022-01-01T00:00:01Z"

    fetched_brochet = consume_api({
        "code_departement": departements.CODE_DEPARTEMENT_INDRE_ET_LOIRE,
        "date_operation_min": DATE_MIN,
        "date_operation_max": DATE_MAX,
        "nom_commun_taxon": taxons.TAXON_BROCHET,
    })
    data_brochet = fetched_brochet["data"]

    fetched_sandre = consume_api({
        "code_departement": departements.CODE_DEPARTEMENT_MAINE_ET_LOIRE,
        "date_operation_min": DATE_MIN,
        "date_operation_max": DATE_MAX,
        "nom_commun_taxon": taxons.TAXON_SANDRE,
    })
    data_sandre = fetched_sandre["data"]

    print("Nombre de Sandres pêchés dans le Maine et Loire entre 2018 et 2022: %s" % len(data_sandre))
    print("Nombre de Brochets pêchés dans l'Indre et Loire entre 2018 et 2022: %s" % len(data_brochet))