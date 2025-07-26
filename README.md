# Bugchella Audit CLI Tool

A Python CLI for auditing BuildOps data, including customers, properties, assets, and vendors.

## Features

- List customers without properties
- List properties with multiple addresses
- List asset makes and asset counts
- List vendors with duplicate names

## Setup

1. **Clone the repository**  
2. **Install dependencies**  
   ```sh
   pip install -r requirements.txt
   ```
3. **Configure API credentials**  
   Create a `.env` file in the root directory:
   ```
   CLIENT_ID="your_client_id"
   CLIENT_SECRET="your_client_secret"
   TENANT_ID="your_tenant_id"
   ```

## Usage

Run the CLI with:

```sh
python cli.py [COMMAND]
```

### Commands

- `customers_no_properties`  
  List customers without properties.

- `properties_many_addresses`  
  List properties with more than 2 addresses.

- `asset_make_counts`  
  List asset makes and number of assets for each make.

- `vendor_duplicate`  
  List vendors with duplicate names.

## File Structure

- [`cli.py`](cli.py): Main CLI entry point
- [`api_auth.py`](api_auth.py): API authentication
- [`data_sources.py`](data_sources.py): Data fetching functions
- [`audits/`](audits/): Audit logic for customers, properties, assets, vendors
