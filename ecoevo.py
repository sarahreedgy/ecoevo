#!/usr/bn/env/python
import glob
import re

from bs4 import BeautifulSoup

all_html = glob.glob("seminars/*.html")
print len(all_html)

def is_ecoevopub(element):
	strongs = element.find_all("strong")
	for strong in strongs:
		if re.search("EcoEvoPub", str(strong)):
			return strong
def extract_date(element):
	date = element.find("h4")
	if (date):
		return date.string
def get_summary_text(element):
    header = element.find("h4", text="Summary")
    if header and header.string == "Summary":
            return header.find_next("p")
for html_file in all_html:
	with open(html_file, "r") as rfile:
		soup = BeautifulSoup(rfile)
		section_div = soup.find("div", class_="section")
		if is_ecoevopub(section_div):
			eep_date = extract_date(section_div)
			print "Found an EcoEvoPub on", eep_date
			summary_text = get_summary_text(section_div)
			for line in summary_text.strings:
				search_name = re.search(r" ([A-Z-]+) ([A-Z-]+)", line)
				if search_name:
					print search_name.group(0)

