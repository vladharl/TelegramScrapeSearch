import shutil
import tkinter as tk
from tkinter import filedialog
import re
from pathlib import Path
from bs4 import BeautifulSoup


# Prompt user for HTML file path
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
if not file_path:
    print("No file selected")
    exit()

# Open and read the HTML file
with open(file_path, "r") as file:
    contents = file.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(contents, "html.parser")

# Create a directory for the results
results_dir = Path("Results")
results_dir.mkdir(exist_ok=True)

# Prompt user for search term
val = input("Enter search term: ")

# Search for matching videos and copy them to the results directory
searchtexts = soup.find_all('div', class_='text')
found = False
for searchtext in searchtexts:
    stext = searchtext.text.strip()
    if re.search(val, stext, re.IGNORECASE):
        vidlink = searchtext.parent
        vlink = vidlink.a['href']
        dest_file = results_dir / Path(vlink).name
        shutil.copy(vlink, dest_file)
        found = True

if not found:
    print(f"No matching videos found for '{val}'")
else:
    print(f"{len(searchtexts)} videos searched, {found} videos copied to {results_dir}")
