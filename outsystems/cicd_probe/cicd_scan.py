# Custom Modules
from outsystems.cicd_probe.cicd_base import build_probe_endpoint, send_probe_get_request
from outsystems.vars.cicd_vars import SCAN_BDD_TESTS_ENDPOINT, PROBE_SCAN_SUCCESS_CODE
from outsystems.vars.file_vars import PROBE_APPLICATION_SCAN_FILE, PROBE_FOLDER
from outsystems.file_helpers.file import store_data

# Scan existing BDD test endpoints (i.e. WebScreens) in the target environment.
def scan_bdd_test_endpoint(env_url :str, application_name :str):
  # Builds the endpoint for CICD Probe and params
  endpoint = build_probe_endpoint(env_url)
  params = {"ApplicationName": application_name}
  # Sends the request
  response = send_probe_get_request(endpoint, SCAN_BDD_TESTS_ENDPOINT, params)
  status_code = response["http_status"]
  if status_code == PROBE_SCAN_SUCCESS_CODE:
    # Stores the result
    filename = "{}\\{}{}".format(PROBE_FOLDER, application_name, PROBE_APPLICATION_SCAN_FILE)
    store_data(filename, response["response"])
    return response["response"]
  else:
    raise NotImplementedError("There was an error. Response from server: {}".format(response))