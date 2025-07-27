from data_sources import get_properties
from concurrent.futures import ThreadPoolExecutor, as_completed
from timeit import default_timer as timer
from functools import cache
import folium

@cache
def fetch_all_properties(limit=100):
    """
    Fetch all properties across all customers.
    Returns a list of properties.
    """
    max_workers = 50
    properties = []
    first_page = get_properties(limit=100, page=0)
    total_count = first_page.get('totalCount', 0)
    properties = first_page.get('items', [])
    # If less than limit, return immediately
    if total_count <= limit:
        return properties

    # Calculate total pages
    num_pages = (total_count + limit - 1) // limit
    # Fetch remaining pages in parallel
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(get_properties, limit=limit, page=page)
            for page in range(1, num_pages)
        ]
        for future in as_completed(futures):
            properties.extend(future.result().get('items', []))

    return properties

def audit_properties_many_addresses():
    """
    Audit properties with multiple addresses.
    Returns a dict with 'properties' (list of (name, id) tuples) and 'totalCount'.
    """
    properties_with_multiple_addresses = []
    properties = fetch_all_properties()
    for p in properties:
        if 'addresses' in p and len(p['addresses']) > 2:
            properties_with_multiple_addresses.append((p['companyName'], p['id']))
    
    return {
        "properties": properties_with_multiple_addresses,
        "totalCount": len(properties_with_multiple_addresses)
    }

def show_properties_on_map(state):
    """
    Filter properties by state and display them on a map.
    """
    properties = fetch_all_properties()
    # Filter properties by state
    filtered = []
    for p in properties:
        for addr in p.get('addresses', []):
            if addr.get('state') == state and addr.get('latitude') and addr.get('longitude'):
                filtered.append({
                    "name": p.get('companyName'),
                    "lat": addr['latitude'],
                    "lon": addr['longitude'],
                    "address": addr.get('street', '') + ', ' + addr.get('city', '') + ', ' + addr.get('state', '')
                })

    # Center map on first property or default location
    if filtered:
        center = [filtered[0]['lat'], filtered[0]['lon']]
    else:
        center = [37.0902, -95.7129]  # Default: USA center

    m = folium.Map(location=center, zoom_start=7)
    for prop in filtered:
        folium.Marker(
            location=[prop['lat'], prop['lon']],
            popup=f"{prop['name']}<br>{prop['address']}"
        ).add_to(m)

    # Save to HTML file
    m.save(f"properties_{state}.html")
    print(f"Map saved to properties_{state}.html")