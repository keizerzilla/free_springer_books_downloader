import requests
import pandas as pd

spreadsheet = "Free Springer Books - eBook list.csv"
base_dl_url = "https://link.springer.com/content/pdf/"
df = pd.read_csv(spreadsheet)

for index, row in df.iterrows():
    doi_url = row["DOI URL"]
    split = doi_url.split("/")
    doi1 = split[-1]
    doi2 = split[-2]
    dl_url = base_dl_url + doi2 + "/" + doi1 + ".pdf"
    filename = row["Book Title"] + ".pdf"
    print("Downloading \"{}\"...".format(row["Book Title"]))
    response = requests.get(dl_url)
    with open(filename, "wb") as dump:
        dump.write(response.content)
    print("Done!")
