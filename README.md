# REDCapForms

For Research done in Fall 2022:

Task: Find word mappings for similar meaning words. Collect all text used in forms, then map them in Word2Vec, then see which words are similar to each other.

# Step 1: Collect all form id's that don't have special terms and conditions
find_ids.py
# Step 2: Download all forms in xml format
edited receiver.php, downlaod process described in final report
# Step 3: Extract text data and filter out non-English forms
cleanup.py
# Step 4: Manual cleaning
# Step 5: Perform word mapping
word_mapping.ipynb


# Resources
forms folder: contains all xml files of instruments. title of each file is <instrument id>xml.xml
pages folder: html downloaded from REDCap's search page. Because REDCap's search page is cretaed dynamically with javascript, this had to be manually scraped. If anyone else is trying to access all pages' html, this would save them some time

