import base64
import subprocess
import json
import argparse

# Define command line arguments
parser = argparse.ArgumentParser(description="FOFA Enumeration Script")
parser.add_argument("-d", "--domain", required=True, help="Specify the domain")
parser.add_argument("-o", "--output", help="Specify the output file")
parser.add_argument("-p", "--param", help="Enter an optional parameter (leave blank for none)")
args = parser.parse_args()

# Hardcoded email and key
email = "your_email@example.com"
key = "your_api_key"

# Initialize page_number to 1
page_number = 1

# Format the input
input_string = 'domain="{}" && status_code=200'.format(args.domain)
if args.param:
    input_string += ' && ' + args.param

# Encode as base64
encoded_string = base64.b64encode(input_string.encode()).decode()

# Initialize results list to store all results
all_results = []

# Infinite loop to fetch results from multiple pages
while True:
    # Build the curl command with the encoded query and current page number
    curl_command = 'curl -s -X GET "https://fofa.info/api/v1/search/all?email={}&key={}&qbase64={}&fields=host&full=true&size=10000&page={}"'.format(email, key, encoded_string, page_number)

    # Execute the curl command and capture the output
    output = subprocess.check_output(curl_command, shell=True)

    # Parse the JSON response
    response = json.loads(output)

    # Check if there are results
    if "results" in response:
        results = response["results"]
        all_results.extend(results)
        # Increment the page number for the next iteration
        page_number += 1
    else:
        # No more results, exit the loop
        break

# Output results to the specified file or to the console
if args.output:
    with open(args.output, "w") as output_file:
        for result in all_results:
            output_file.write(str(result) + "\n")
else:
    for result in all_results:
        print(result)
