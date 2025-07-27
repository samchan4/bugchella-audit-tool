# Bugchella Audit Tool - User Guide

## What is the Bugchella Audit Tool?

The Bugchella Audit Tool is a simple program that helps you examine and visualize your BuildOps data. It can show you information about customers, properties, assets, and vendors in an easy-to-understand format.

## Before You Begin

You'll need:
- A computer with the Bugchella Audit Tool files already downloaded
- Basic familiarity with opening programs on your computer
- Internet connection (for displaying maps)
- Your BuildOps API credentials (provided by your administrator)

## Setting Up Your Credentials

Before using the tool for the first time, you need to set up your access credentials:

1. Find the folder where the Bugchella Audit Tool is located
2. Look for a file named `.env.example`
3. Make a copy of this file and rename it to `.env` (just remove the ".example" part)
4. Open the `.env` file with a text editor (like Notepad or TextEdit)
5. Replace the placeholder text with your actual credentials:
   ```
   CLIENT_ID="your_client_id"
   CLIENT_SECRET="your_client_secret"
   TENANT_ID="your_tenant_id"
   ```
6. Save the file and close the text editor

**Note:** You only need to do this setup once. Your IT administrator should provide you with the correct credential values to use.

## Getting Started

### On Windows:
1. Open the "Command Prompt" by searching for it in the Start menu
2. Type `cd` followed by the location of the tool (your IT support can help with this)
3. Press Enter

### On Mac:
1. Open "Terminal" (press Cmd+Space and type "Terminal")
2. Type `cd ~/Documents/bugchella audit tool`
3. Press Enter

## Running the Tool

Once you've opened the command window and navigated to the right folder, you can run different commands:

### Find Customers Without Properties

**What it does:** Shows you which customers in your database don't have any properties assigned to them.

**How to use it:**
```
python cli.py customers-no-properties
```

### Find Properties With Multiple Addresses

**What it does:** Shows properties that have more than 2 addresses, which might indicate data issues.

**How to use it:**
```
python cli.py properties-many-addresses
```

### Count Assets by Make

**What it does:** Shows a list of asset makes and the number of assets you have from each make.

**How to use it:**
```
python cli.py asset-make-counts
```

### Find Duplicate Vendors

**What it does:** Identifies vendors that might be duplicates because they have the same name.

**How to use it:**
```
python cli.py vendor-duplicate
```

### View Properties on a Map

**What it does:** Creates a map showing all your properties in a specific state.

**How to use it:**
```
python cli.py show-map --state CA
```
(Replace "CA" with the two-letter code for the state you want to view)

**To view the map:**
1. After running the command, look for a message telling you the map is ready
2. Find the file named `properties_CA.html` in the same folder (where "CA" is the state you chose)
3. Double-click this file to open it in your web browser
4. The map will show all your properties in that state with markers you can click for more information

## Troubleshooting

### If nothing happens when you run a command:
- Make sure you typed the command exactly as shown
- Check that you're in the right folder
- Ask your IT support for help

### If you get an error message:
- Take a screenshot of the error
- Send it to your IT support team

### If the map doesn't show any properties:
- Check that you used the correct state code
- Verify that you have properties in that state
- Make sure you have an internet connection

## Need More Help?

Contact your system administrator or IT support team for assistance.
