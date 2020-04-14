# free_springer_books_downloader
Someone sent me a spreadsheet with free Springer book. I wrote a Python script to download them all!

The script it's called ```downloader.py```. It will open the spreadsheet file (already downloaded and called ```Free Springer Books - eBook list.csv```) and iterate each line requesting the books. You can access the original spreadsheet [here](https://docs.google.com/spreadsheets/d/1HzdumNltTj2SHmCv3SRdoub8SvpIEn75fa4Q23x0keU/htmlview). All the books will be stored in the same folder as the script. Quick and dirty.

Package requirements: ```pandas, requests```

To install the requirements, open a shell and run:

```pip3 install pandas requests```

Cheers.
