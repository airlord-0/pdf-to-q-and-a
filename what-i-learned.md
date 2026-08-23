# MY learning journey 

# day 2.   19th/july/2026
- I learned how to make a website reacive fies
` <input type="file"> ` 
- revised how we link html file with css 
`<link rel="stylesheet" href="file_name.css">`

- revised css 
- anything inside head isn't visible. script in the <body> has effects on the website

# day 3. 26th july 2026
- learned how do we install django pip install django
- we use django for backend purpose its a backend framework built for python 
- once its installed we go like python3 -m django --version to check its version
* how do we start projects in django ? 
- pyhton3 -m django startproject project_name 
- once starting the project is finished we get to see a folder named after the project inside our project folder 

# day 4 27th july 2026 
- learned how to create a veiw function using django.http response 
- basically we make a function with requests attribute and return httpresponse 
- we always end our routes with / 

# day 5 31st july 2026 learned Routing
- I got a basic idea how websites links have paths and how they work. 
- Start by creating a new application in django using the command python3 manage.py startapp "App_Name"
- once the app is created we create a function in views.py using HttpResponse we can requst and get responses 
- we create new urls file in application folder and map the views functions into urls file
- after mapping we go to the main urls file use include library and include the paths in the application/urls.py 
- with this procedure we be able to do things like website/router/greetings or /mywebsite
## I have successfully created a template then added my index.html into it, then added a function in views.py using render thing 
- the day was nice I take it as a win learned a little bit understood there's a lot to learn

## day 6 2nd august 2026 
- learned how we write comments in HTML we use 
    'html 
    <!-- that's how you do it -->
- learned how we make a functionig upload button in html 

## day 7 14th august 2026
- learned how you save files requested by html - save_file = request.FILES["uploaded_file"]
- Learned a new Library pymupdf. we use this library to extract text out of pdfs 
- Learned few syntax of pymupdf such as :
* doc = pymupdf.open ("file_name") 
out = open("output.txt", "wb") wb stands for write binary - it opens files and   writes binary in it 
- for page in doc : 
    text = page.get_text().encode("utf-8")
    out.write(text)
    out.write((12,)) # this tells editor to use new file
    out.close
# I feel like this project is teaching me lot 10x more than any college ever would

## day 8 18th august 2026 
- learned CHUNKING, splitting a big document into smaller units so that It could fit in strict context size window of embedding models and LLMs 
- Leaned how we split text using langchain's RecursiveCharacterTextSplitter and store these in langchain's Documents with calculated metadata 
- spent 5 hours on finding the best chunking method for me and learning the actual production grade code from [data_bricks](https://community.databricks.com/t5/technical-blog/the-ultimate-guide-to-chunking-strategies-for-rag-applications/ba-p/113089)

### my learning strategy : 20% consume 80% apply been super effective so far 