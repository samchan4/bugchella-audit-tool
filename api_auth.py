import requests

_API_URL = "https://public-api.live.buildops.com/v1/auth/token"
_access_token = None
_token_type = None
_expires_in = None
_tenant_id = None

def authorize(client_id, client_secret, tenant_id):
    """
    Authorize with BuildOps API and store access token and tenant id.
    """
    global _access_token, _token_type, _expires_in, _tenant_id
    payload = {
        "clientId": client_id,
        "clientSecret": client_secret
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(_API_URL, json=payload, headers=headers)
    response.raise_for_status()
    data = response.json()
    _access_token = data.get("access_token")
    _token_type = data.get("token_type")
    _expires_in = data.get("expires_in")
    _tenant_id = tenant_id
    if not _access_token or not _token_type:
        raise Exception("Authorization failed: missing token.")

def get_auth_header():
    """
    Return the authorization header for future requests.
    """
    if not _access_token or not _token_type:
        raise Exception("Not authorized. Call authorize() first.")
    return {"Authorization": f"{_token_type} {_access_token}"}

def get_tenant_id():
    """
    Return the tenant id for future requests.
    """
    if not _tenant_id:
        raise Exception("Tenant ID not set. Call authorize() first.")
    return _tenant_id
