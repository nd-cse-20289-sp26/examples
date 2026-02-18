#!/usr/bin/env python3

import concurrent.futures
import os
import re
import sys

import requests

# Functions

def wget(url):
    p = os.path.basename(url)           # Review: os.path.basename

    print('Downloading {} to {}'.format(url, p))
    r = requests.get(url)
    with open(p, 'wb') as fs:           # Review: Writing to a file, with statement
        fs.write(r.content)

    return p

def flatten(sequence):
    for iterable in sequence:
        yield from iterable

# Main Execution

def main():
    # Download images from Flickr
    # https://www.flickr.com/photos/indianafirst/albums/72177720332075049/
    # https://www.flickr.com/photos/indianafirst/albums/72177720332075049/page2
    # https://www.flickr.com/photos/indianafirst/albums/72177720332075049/page3
    pages  = (requests.get(argument) for argument in sys.argv[1:])
    assets = flatten(
        re.findall(r'src="//(.*jpg)"', page.text) for page in pages
    )
    urls   = ('https://' + asset for asset in assets)

    # Sequential
    list(map(wget, urls))               # Discuss: Why list?

    # Parallel                          # Discuss: concurrent.futures
    '''
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(wget, urls)        # Discuss: Timing
    '''

if __name__ == '__main__':
    main()
