from data_sources import get_vendors
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import Counter

def fetch_all_vendors(limit=100):
    """
    Fetch all vendors.
    Returns a list of vendors.
    """
    max_workers = 50
    vendors = []
    first_page = get_vendors(limit=100, page=0)
    total_count = first_page.get('totalCount', 0)
    vendors = [item['name'] for item in first_page.get('items', [])]

    # If less than limit, return immediately
    if total_count <= limit:
        return vendors

    # Calculate total pages
    num_pages = (total_count + limit - 1) // limit
    # Fetch remaining pages in parallel
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(get_vendors, limit=limit, page=page)
            for page in range(1, num_pages)
        ]
        for future in as_completed(futures):
            vendors.extend([item['name'] for item in future.result().get('items', [])])

    return vendors

def audit_vendors_duplicates():
    """
    Audit vendors with duplicate names.
    Returns a dict with 'vendors' (list of vendors with duplicate names) and 'totalCount'.
    """
    all_vendors = fetch_all_vendors()
    counts = Counter(all_vendors)
    duplicates = {name: count for name, count in counts.items() if count > 1}
    
    return {
        "vendors": duplicates,
        "totalCount": len(duplicates)
    }