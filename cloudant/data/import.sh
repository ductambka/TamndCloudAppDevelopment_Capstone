npm install -g couchimport

export IAM_API_KEY="lSNvExsaUhf9pa4mJ4PwCsOCd6WyR4O6iN3mmP6UIt3Y"
# Windows: set IAM_API_KEY="lSNvExsaUhf9pa4mJ4PwCsOCd6WyR4O6iN3mmP6UIt3Y"
export COUCH_URL="https://38fb3533-a6dc-4394-b6c0-3670c49aa5cd-bluemix.cloudantnosqldb.appdomain.cloud/"
# Windows: set COUCH_URL="https://38fb3533-a6dc-4394-b6c0-3670c49aa5cd-bluemix.cloudantnosqldb.appdomain.cloud/"

cat ./dealerships.json | couchimport --type "json" --jsonpath "dealerships.*" --database dealerships
# Windows: get-content .\dealerships.json | couchimport --type "json" --jsonpath "dealerships.*" --database dealerships
cat ./reviews.json | couchimport --type "json" --jsonpath "reviews.*" --database reviews
# Windows Powershell: get-content .\reviews.json | couchimport --type "json" --jsonpath "reviews.*" --database reviews