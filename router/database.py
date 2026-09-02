from pinecone import Pinecone,ServerlessSpec
from dotenv import load_dotenv

load_dotenv ()

pc = Pinecone()

index=pc.Index("context")

def vectorbase_upsert (
    # : tells the python to expect assigned kind of parameters
    chunks : list[str], # parameter_name : parameter_type 
    embeddings : list,
    metadata_list : list[dict],
    doc_id : int,
    batch_size : int =100
    ) :

    vectors_to_upsert=[]

    for i, (chunk,emb,meta) in enumerate  (zip(chunks,embeddings,metadata_list)) :
         # vectors come in many types, google api packs vectos in embeddingContents obeject
        if (hasattr(emb,"values")) :                    # this one gets executed 
            vector_values = list(emb.values)            # remove the object, store only values
        elif (hasattr(emb,"tolist")):                   # future Proof
            vector_values = emb.tolist() 
        else :                                          # future proof
            vector_values = list(emb)

        # metadata concatenation 
        full_metadata = {
            **meta,                                     # **meta gives the existing dictionary
            "text" : chunk,                             # until now chunk and metadata were seperate, put chunk in metadata itself 
            "doc_id" : doc_id                           # argumet doc_id given by django in views.py
        }

       # prepare records for pinecone ,                 # 1 record stores : 1. Record id                  
        vectors_to_upsert.append({                                        # 2. Embedding
                "id" : f"{doc_id}_chunk_{i}",                             # 3. metadata that includes my units as well 
                "values" : vector_values,
                "metadata" : full_metadata
            })
    # now I have the records stored in vectors_to_upset 
    # its time to push these records batch by batch 
        
    for i in range (0,len(vectors_to_upsert),batch_size) : 
        batch = vectors_to_upsert[ i: i+batch_size] # where batch_size is 100 so the loop is from 1-101,101th excluded
        index.upsert(vectors=batch) # upsert(), has a parameter vectors, provided by pinecone pdk
                                    # there are other functions -> index.delete(),querry(),fetch etc 

    print("successfully upserted records")

        
       
    
    


        
        
    

        
                          
