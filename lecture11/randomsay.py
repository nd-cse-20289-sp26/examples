#!/usr/bin/env python3

import os
import random                          # Discuss: random module
import sys

# Constants
                                        # Discuss: set data structure
FORBIDDEN = {'bong', 'sodomized', 'kiss', 'head-in', 'satanic', 'telebears'}

# Main Execution

def main():
    cow = []                            # Discuss: os.popen
    for index, line in enumerate(os.popen('cowsay -l')):
        if not index:                   # Discuss: enumerate
            continue

        for cow in line.split():        # Review: str.split
            if cow not in FORBIDDEN:    # Review: searching collection
                cow.append(cow)         # Review: list.append
    
    selected = random.choice(cow)
    os.system(f'cowsay -f {selected}')  # Variant: check exist status

if __name__ == '__main__':
    main()
