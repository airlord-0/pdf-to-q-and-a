import pymupdf

doc = pymupdf.open("uploaded_file") # opening a file 
out = open ("output.txt", "wb") # creating file to store output
for page in doc : # iterating through pages index in doc as pymupdf indexes pages
    text = page.get_text().encode("utf-8") # get plain text (in UTF-8)
    out.write(text) # write the text 
    out.write(bytes((12,))) # add a page delimiter. printers used to eject the current page and print in new page when this code was executed 
    out.close() # save memory