# FOFA Enumeration Script
Simple script to enumerate subdomains using the FOFA search engine, you can save it to a file or pipe to another tools.


# Usage
Replace the your_email@example.com and your_api_key placeholders in the script with your FOFA email and API key.

Run the script with the following command-line options:

    -d or --domain: Specify the domain you want to enumerate (required).
    -o or --output: Specify the output file where the results will be saved (optional).
    -p or --param: Specify an optional parameter to refine the FOFA query (optional).

To find documentation of other queries and filters that you can use with the -p flag visit: https://en.fofa.info/ and the see option "Query Description".

# Examples
List all subdomains from a target:
```
python3 fofa_subs.py -d microsoft.com
```
Running other tools together
```
python3 fofa_subs.py -d microsoft.com | httpx -status-code -title
```

