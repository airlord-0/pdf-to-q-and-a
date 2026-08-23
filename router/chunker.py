
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
import re


def text_splitter (document, chunk_size = 500, chunk_overlap = 10) :


    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ". ", " ", ""],
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )

    chunks = text_splitter.split_text(document)

    # Determine section titles for enhanced metadata
    section_patterns = [
        r'^#+\s+(.+)$',      # Markdown headers
        r'^.+\n[=\-]{2,}$',  # Underlined headers
        r'^[A-Z\s]+:$'       # ALL CAPS section titles
    ]

    documents =[]
    section = 'introduction'
    for i, chunk in enumerate (chunks) :
        chunk_lines= chunk.split('\n')
        for lines in chunk_lines :
            for pattern in section_patterns :
                match = re.match(pattern,lines,re.MULTILINE)
                if match : 
                    section = match.group(0)
                    break

    # lets give our documents some meta data as well 
        words= [re.findall(r'\bw+\b',chunk.lower())]
        stopwords=["for","the","a","is","are","was","were","been","has","have","had"] 
        useful_words = [w for w in words if w not in stopwords]
        semantic_density = (len(useful_words))/max(1,(len(words))) # prevent ZeroDivisionError

        doc = Document(page_content=chunk,
                         metadata = {
                            "chunk_id" : i,
                            "chunk_size" : len(chunks),
                            "chunk_type" : "semantic",
                            "semantic_density" : round(semantic_density,2),
                            "total_chunk_size" : len(words),
                            "section" : section
                         }
                        ) # debugged =, metadata is a dictionary we use : not = 

        documents.append(doc)
    return documents 



    

