# This code unzips all ROMs in a given fullset, then copies only those ROMs with the [!], (U), or (E) extension
# to the Retropie directory.
# If the option 'J' is selected, the user may also copy ROMs with the (J) extension.
# The point is to avoid copying bad or non-English ROMs to Retropie.

import os
from Tkinter import *
from Tkinter import ttk

root = Tk()
root.title = ("Choose a directory")

