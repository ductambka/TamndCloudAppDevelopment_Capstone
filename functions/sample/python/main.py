#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
from cloudant.client import Cloudant
from cloudant.error import CloudantException
import requests


def main(dict):
    databaseName = "dealerships"

    try:
        client = Cloudant.iam(
            account_name=dict["COUCH_USERNAME"],
            api_key=dict["IAM_API_KEY"],
            connect=True,
        )
        print("Databases: {0}".format(client.all_dbs()))
    except CloudantException as ce:
        print("unable to connect")
        print(f"ce = {ce}")
        return {"error": ce}
    except (requests.exceptions.RequestException, ConnectionResetError) as err:
        print("connection error")
        print(f"err = {err}")
        return {"error": err}

    return {"dbs": client.all_dbs()}

main({
    "COUCH_USERNAME": "38fb3533-a6dc-4394-b6c0-3670c49aa5cd-bluemix",
    "IAM_API_KEY": "lSNvExsaUhf9pa4mJ4PwCsOCd6WyR4O6iN3mmP6UIt3Y",
    "COUCH_URL": "https://38fb3533-a6dc-4394-b6c0-3670c49aa5cd-bluemix.cloudantnosqldb.appdomain.cloud/",
})