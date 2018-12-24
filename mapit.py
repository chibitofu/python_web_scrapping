#! python3
# mapIt.py - Launches a map in the browser using an addesss from the command line or clipboard.

import webbrowser, sys
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])

# TODO: GEt address from clipboard
