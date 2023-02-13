#! /bin/bash
set -e

source ./sources/taxons.sh
source ./sources/departements.sh

API_VERSION="v1"
URL="$API_URL/$API_VERSION/observations"

function _fetch_data() {
    local URL="$1"
    local DATA=$(curl -s "$URL" -H 'accept: application/json' | jq '.data')
    if [ $? -ne 0 ]; then
        echo "Error fetching API"
        exit 1
    fi

    echo "$DATA"
}

function _get_nb_taxon()
{
    local CODE_DEPARTEMENT="$1"
    local NOM_TAXON="$2"
    local DATE_MIN="$3"
    local DATE_MAX="$4"

    local TO_FETCH="$URL?code_departement=$CODE_DEPARTEMENT&nom_commun_taxon=$NOM_TAXON&date_operation_min=$DATE_MIN&date_operation_max=$DATE_MAX"
    
    DATA=$(_fetch_data "$TO_FETCH")

    DATA_LENGTH=$(echo "$DATA" | jq '. | length')

    echo "$DATA_LENGTH"
}


function main()
{
    local DATE_MIN="2018-01-01T00:00:01Z"
    local DATE_MAX="2022-01-01T00:00:01Z"

    _get_nb_taxon "$CODE_DEPARTEMENT_BAS_RHIN" "$NOM_TAXON_BATOFLE" "$DATE_MIN" "$DATE_MAX"
    # FIXME
}

main

