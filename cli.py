import click
import api_auth
from dotenv import load_dotenv
import os


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
    click.echo("Listing customers without properties...")

@cli.command()
def properties_many_addresses():
    """List properties with more than 2 addresses"""
    click.echo("Listing properties with many addresses...")

@cli.command()
def asset_make_counts():
    """List of asset make and number of assets for each make """
    click.echo("Listing asset make counts...")

@cli.command()
def vendor_duplicate():
    """List vendors with duplicate names"""
    click.echo("Listing vendors with duplicate names...")

if __name__ == "__main__":
    cli()