# Program to find media and copy to "Results" folder if matching prompted keyword
# Must be placed in same root folder as /video_files

# Importing library

from bs4 import BeautifulSoup
import re
import tkinter as tk
from tkinter import filedialog
import shutil
import os


# Opening and reading the html file

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
file = open(file_path, "r")
contents = file.read()

soup = BeautifulSoup(contents, "lxml")

if not os.path.exists('Results/'):
	os.makedirs('Results/')

val = input("Enter search term: ")

searchtexts = soup.find_all('div', class_='text')
for searchtext in searchtexts:
	stext = searchtext.text
	if val in stext:
		vidlink = searchtext.parent
		vlink = vidlink.a['href']
		shutil.copy(vlink, r'Results/')