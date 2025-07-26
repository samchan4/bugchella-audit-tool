import click

@click.group()
def cli():
    """Bugchella Audit CLI Tool"""
    pass

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