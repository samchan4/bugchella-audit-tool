from data_sources import get_customers, get_properties_list_by_customerID
from concurrent.futures import ThreadPoolExecutor, as_completed
from timeit import default_timer as timer

def fetch_all_customers(limit=100):
    # Fetch first page to get totalCount
    customers = []
    first_page = get_customers(limit=limit, page=0)
    total_count = first_page.get('totalCount', 0)
    customers = first_page.get('items', [])

    # If less than limit, return immediately
    if total_count <= limit:
        return customers

    # Calculate total pages
    num_pages = (total_count + limit - 1) // limit
    # Fetch remaining pages in parallel
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [
            executor.submit(get_customers, limit, page)
            for page in range(1, num_pages)
        ]
        for future in as_completed(futures):
            customers.extend(future.result().get('items', []))
    return customers

def audit_customers_with_properties():
    """
    Audit customers with properties.
    Returns a dict with 'customers' (list of (name, id) tuples) and 'totalCount'.
    prints elapsed time.
    """
    max_workers = 50
    customers_with_properties = []
    customers = fetch_all_customers()

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(get_properties_list_by_customerID, c['id']): c for c in customers
        }

        for future in as_completed(futures):
            customer = futures[future]
            try:
                property_list = future.result()
                if property_list['totalCount'] > 0:
                    customers_with_properties.append((customer['name'], customer['id']))
            except Exception as e:
                print(f"Error processing customer {customer['name']} (ID: {customer['id']}): {e}")

    return {
        "customers": customers_with_properties,
        "totalCount": len(customers_with_properties)
    }

def audit_customers_no_properties():
    """
    Audit customers without properties.
    Returns a dict with 'customers' (list of (name, id) tuples) and 'totalCount'.
    """
    max_workers = 50
    customers_without_properties = []
    customers = fetch_all_customers()

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(get_properties_list_by_customerID, c['id']): c for c in customers
        }

        for future in as_completed(futures):
            customer = futures[future]
            try:
                property_list = future.result()
                if property_list['totalCount'] == 0:
                    customers_without_properties.append((customer['name'], customer['id']))
            except Exception as e:
                print(f"Error processing customer {customer['name']} (ID: {customer['id']}): {e}")

    return {
        "customers": customers_without_properties,
        "totalCount": len(customers_without_properties)
    }