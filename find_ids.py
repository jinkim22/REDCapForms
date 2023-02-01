from bs4 import BeautifulSoup

def get_usable_ids(pg_num):
    f = open("pg" + str(pg_num) + ".html", "r")
    # print(f)
    soup = BeautifulSoup(f, 'html.parser')
    mytrs = soup.find_all("tr", {"class": "search_row"})
    ids = []
    for txt in mytrs:
        in_id = False
        cur_id = ""
        s = str(txt)
        for i in range(20, len(s)):
            if s[i-18:i] == "showHideSearchRow(":
                in_id = True
            if s[i] == ")":
                in_id = False
                if cur_id != "":
                    ids += [cur_id]
                    break
            if in_id:
                cur_id += s[i]
    # find detail ids, which is the whole blob of info for each form
    usable_ids = []
    unusable_ids = []
    for form_id in ids:
        if "Terms of use:" not in str(soup.find(id="details" + str(form_id))):
            usable_ids += [form_id]
        else:
            unusable_ids += [form_id]
    return usable_ids, unusable_ids
        
def runner():
    ids = []
    unusables = []
    for i in range(1, 28):
        usable, unusable = get_usable_ids(i)
        ids += usable
        unusables += unusable
    with open('form_ids.txt', 'w') as f:
        f.write(", ".join(ids))

runner()