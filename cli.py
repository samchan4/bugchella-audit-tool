import click
import api_auth
from dotenv import load_dotenv
import os
from audits.customers import audit_customers_no_properties
from audits.properties import audit_properties_many_addresses
from audits.assets import audit_asset_makes_count
from audits.vendors import audit_vendors_duplicates

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
    click.echo(audit_customers_no_properties())

@cli.command()
def properties_many_addresses():
    """List properties with more than 2 addresses"""
    click.echo(audit_properties_many_addresses())

@cli.command()
def asset_make_counts():
    """List of asset make and number of assets for each make """
    click.echo(audit_asset_makes_count())

@cli.command()
def vendor_duplicate():
    """List vendors with duplicate names"""
    click.echo(audit_vendors_duplicates())

if __name__ == "__main__":
    if sys.version_info < (3, 9):
        print("Python 3.9 or newer is required.")
        sys.exit(1)
    cli()
    