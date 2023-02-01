# import xml.etree.ElementTree as ET

# # import required module
# import os
# # assign directory
# directory = './forms'
 
# # iterate over files in
# # that directory

# with open('form_dictionary.txt', 'w') as f:
#     for filename in os.listdir(directory):
#         file = os.path.join(directory, filename)
#         tree = ET.parse(file)
#         root = tree.getroot()
#         elabels = root.findall("./Metadata/Field/ElementLabel")
#         for e in elabels:
#             f.write(e.text + "\n")

import xml.etree.ElementTree as ET
import os
from html.parser import HTMLParser
import regex as re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('english'))

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def extract_text(xml_file):
    # parse the xml file
    tree = ET.parse(xml_file)

    # get the root element
    root = tree.getroot()

    # Initialize an empty list to store the text
    text_list = []

    # Iterate over all elements in the XML tree
    for elem in root.iter():
        # If the element has text
        if elem.text:
            text = strip_tags(elem.text) #remove html tags
            words = word_tokenize(text)
            words = [word for word in words if word.lower() not in stop_words]
            text = elem.text.replace("\n", " ") #replace newlines with spaces
            text = re.sub(r'[^\w\s]', '', text) #remove special characters
            text = re.sub(r'\d+', '', text) #remove numbers
            text = " ".join(words)
            text_list.append(text)

    return text_list

def extract_text_from_folder(folder_path):
    # Initialize an empty list to store the text from all files
    all_text = []
    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        # check if the file is an XML file
        if filename.endswith('.xml'):
            # Construct the full file path
            file_path = os.path.join(folder_path, filename)
            # Extract the text from the file
            text = extract_text(file_path)
            # Append the text to the list
            all_text.extend(text)
    return all_text

folder_path = './forms'
text_data = extract_text_from_folder(folder_path)
with open('chatgpt_form_dictionary.txt', 'w') as f:
    f.write(str(text_data))