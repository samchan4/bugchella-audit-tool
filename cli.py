import click
import api_auth
from dotenv import load_dotenv
import os
from audits.customers import audit_customers_no_properties
from audits.properties import audit_properties_many_addresses, show_properties_on_map
from audits.assets import audit_asset_makes_count
from audits.vendors import audit_vendors_duplicates
import csv
import sys

@click.group()
def cli():
    """Bugchella Audit CLI Tool"""
    load_dotenv()  # Loads from .env file in current dir
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    tenant_id = os.getenv("TENANT_ID")
    api_auth.authorize(client_id, client_secret, tenant_id)

@cli.command()
def customers_no_properties():
    """List customers without properties"""
    result = audit_customers_no_properties()
    
    click.echo("Customers with no properties:")
    click.echo("----------------------------")
    
    for customer_name, customer_id in result.get("customers", []):
        click.echo(f"Customer ID: {customer_id} - {customer_name}")
    
    click.echo(f"\nTotal: {result.get('totalCount', 0)} customers found with no properties")

@cli.command()
def properties_many_addresses():
    """List properties with more than 2 addresses"""
    result = audit_properties_many_addresses()
    
    click.echo("Properties with more than 2 addresses:")
    click.echo("------------------------------------")
    
    for property_name, property_id in result.get("properties", []):
        click.echo(f"Property ID: {property_id} - {property_name}")
    
    click.echo(f"\nTotal: {result.get('totalCount', 0)} properties found with multiple addresses")

@cli.command()
def asset_make_counts():
    """List of asset make and number of assets for each make """
    result = audit_asset_makes_count()
    click.echo("Asset counts by manufacturer:")
    click.echo("---------------------------")
    
    total_assets = 0
    for make, count in result.get("asset_makes_count", {}).items():
        click.echo(f"{make}: {count} assets")
        total_assets += count
    
    click.echo(f"\nTotal: {total_assets} assets across {len(result.get('asset_makes_count', {}))} manufacturers")

@cli.command()
def vendor_duplicate():
    """List vendors with duplicate names"""
    result = audit_vendors_duplicates()
    click.echo("Possible duplicate vendors:")
    click.echo("-------------------------")
    
    for vendor_name, count in result.get("vendors", {}).items():
        click.echo(f"\"{vendor_name}\" appears {count} times")

    click.echo(f"\nTotal: {result.get('totalCount', 0)} potential duplicate vendor entries found")

@cli.command()
@click.option('--state', required=True, help='State code to filter properties (e.g., CA, NY)')
def show_map(state):
    """Show properties on a map filtered by state"""
    show_properties_on_map(state)
    click.echo(f"Map for state '{state}' saved as properties_{state}.html")

if __name__ == "__main__":
    if sys.version_info < (3, 9):
        print("Python 3.9 or newer is required.")
        sys.exit(1)
    cli()
