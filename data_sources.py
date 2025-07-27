import requests
from api_auth import get_auth_header, get_tenant_id

BASE_URL = "https://public-api.live.buildops.com"

def _get_headers():
    headers = get_auth_header()
    headers["tenantId"] = get_tenant_id()
    headers["Accept"] = "application/json"
    return headers

def get_customers(limit=100, page=0):
    return requests.get(
        f"{BASE_URL}/v1/customers",
        headers=_get_headers(),
        params={"limit": limit, "page": page}
    ).json()

def get_properties_list_by_customerID(customer_id):
    return requests.get(
        f"{BASE_URL}/v1/customers/{customer_id}/properties",
        headers=_get_headers()
    ).json()

def get_properties(limit=100, page=0):
    return requests.get(
        f"{BASE_URL}/v1/properties",
        headers=_get_headers(),
        params={"page_size": limit, "page": page, "include_addresses": "true"}
    ).json()

def get_asset_makes(limit=100, page=0):
    return requests.get(
        f"{BASE_URL}/v1/asset-makes",
        headers=_get_headers(),
        params={"pageSize": limit, "page": page}
    ).json()

def get_property_assets(limit=100, page=0):
    return requests.get(
        f"{BASE_URL}/v1/assets",
        headers=_get_headers(),
        params={"pageSize": limit, "page": page}
    ).json()

def get_vendors(limit=100, page=0):
    return requests.get(
        f"{BASE_URL}/v1/vendors",
        headers=_get_headers(),
        params={"page_size": limit, "page": page}
    ).json()