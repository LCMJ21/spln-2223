#!/usr/bin/env python3


import newspaper

url = "https://www.ojogo.pt/"

npp = newspaper.build(url)
raw_data=[]

for article in npp.articles[:10]:
    try:
        article.download()
        article.parse()
        article.nlp()
        raw_data.append((article.title,article.top_image,article.authors,article.url,article.summary))
    except:
        print("Erro ao fazer download do artigo")



# Generate the HTML code for each article
html = '<ul>'
for article in raw_data:
    html += '<li>'
    html += '<h1>' + str(article[0]) + '</h1>'
    html += '<img src="' + str(article[1]) + '" style="width:30%">'
    html += '<p>By ' + str(article[2]) + '</p>'
    html += '<a href="' + str(article[3]) + '">' + str(article[0]) + '</a>'
    html += '<p>' + str(article[4]) + '</p>'
    html += '</li>'
html += '</ul>'

# Get url name
url_name = url.split('//')[1].split('.')[1]
print(url_name)

with open(f'TPC6/html/{url_name}.html', 'w') as file:
    file.write(html)