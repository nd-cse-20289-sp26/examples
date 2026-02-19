#!/usr/bin/env python3

import os
import re
import sys

import requests

# Functions

def usage(exit_status=0):
    print(f'''Usage: {os.path.basename(sys.argv[0])} [flags]
    -c      CITY    Which city to search
    -s      STATE   Which state to search (Indiana)''')
    sys.exit(exit_status)

def zipcodes(city: str, state: str) -> None:
    url   = f'https://www.zipcodestogo.com/{state}/'
    regex = r'/([^/]+)/[A-Z]{2}/([0-9]{5})/">'  # Review: regex

                                                # Discuss: popen
    #for line in os.popen(f'curl -sL {url}'):
    #   print(line)

    response = requests.get(url)                # Discuss: requests
    matches  = re.findall(regex, response.text) # Discuss: re.findall

    for current, zipcode in matches:
        if city is None or city == current:
            print(zipcode)

# Main execution

def main(arguments=sys.argv[1:]):
    state = 'Indiana'
    city  = None                                # Review: None

    while arguments:                            # Review: parsing arguments
        argument = arguments.pop(0)
        match argument:
            case '-c': city  = arguments.pop(0)
            case '-s': state = arguments.pop(0)
            case '-h': usage(0)
            case _   : usage(1)

    zipcodes(city, state)

if __name__ == '__main__':
    main()
