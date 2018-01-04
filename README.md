Converts a transaction export from TopScore in to a format that can be imported by Quickbooks Online.


Download transactions from TopScore
-----------------------------------
1. Go to the admin menu of your site, and under "Commerce", select "Transactions"
2. Adjust the search as appropriate
3. Click on the "Export" link.  A file named "trans.zip" will be downloaded.
4. Unzip the file.  This will create a new directory called "trans"

Convert the downloaded file to a format QBO can handle
------------------------------------------------------
1. Run the ts_to_qb.py script from this repo, pointing to the __purchases.csv__ file in the trans directory.  You'll need to update the script to specify where you want the output to be saved.  (**Note**: Quickbooks can only import a limited number of transactions from a single file, so the output may be split between several files.)

Import the transactions into QBO
--------------------------------
1. In Quickbooks Online, go to the "Banking" section.
2. Select your TopScore account
3. Click the arrow next to "Update", and select "File upload"
4. Select the file that was output by the conversion script, and then follow the steps to map fields and import.
5. If necessary, repeat for the other files that were output by the conversion.