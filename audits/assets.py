from data_sources import get_asset_makes, get_property_assets
from concurrent.futures import ThreadPoolExecutor, as_completed
from timeit import default_timer as timer
from collections import Counter

def fetch_all_asset_makes(limit=100):
    """
    Fetch all asset makes.
    Returns a list of asset makes.
    """
    max_workers = 50
    asset_makes = []
    first_page = get_asset_makes(limit=100, page=0)
    total_count = first_page.get('totalCount', 0)
    asset_makes = [item['name'] for item in first_page.get('items', [])]

    # If less than limit, return immediately
    if total_count <= limit:
        return asset_makes

    # Calculate total pages
    num_pages = (total_count + limit - 1) // limit
    # Fetch remaining pages in parallel
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(get_asset_makes, page_size=limit, page=page)
            for page in range(1, num_pages)
        ]
        for future in as_completed(futures):
            asset_makes.extend([item['name'] for item in future.result().get('items', [])])

    return asset_makes

def fetch_all_property_assets(limit=100):
    """
    Fetch all property assets.
    Returns a list of property assets.
    """
    max_workers = 50
    property_assets_make = []
    first_page = get_property_assets(limit=100, page=0)
    total_count = first_page.get('totalCount', 0)
    property_assets_make = [item['make'] for item in first_page.get('items', [])]

    # If less than limit, return immediately
    if total_count <= limit:
        return dict(Counter(property_assets_make))

    # Calculate total pages
    num_pages = (total_count + limit - 1) // limit
    # Fetch remaining pages in parallel
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(get_property_assets, limit=limit, page=page)
            for page in range(1, num_pages)
        ]
        for future in as_completed(futures):
            property_assets_make.extend([item['make'] for item in future.result().get('items', [])])

    return dict(Counter(property_assets_make))

def audit_asset_makes_count():
    """
    Audit asset makes.
    Returns a dict with 'asset_makes' (list of names) and 'totalCount'.
    """
    asset_makes_count = fetch_all_property_assets()
    return {
        "asset_makes_count": asset_makes_count,
        "totalCount": len(asset_makes_count)
    }