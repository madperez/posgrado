from scholarly import scholarly
#import anvil.server

#anvil.server.connect("WTILNCT6433IFN3C6UHKGVAU-BBOZIA6PRHGNNBOK")

#@anvil.server.callable
def busca_publicaciones(lista):
  listapub=[]
  for row in lista:
     print(row)
     search_query = scholarly.search_author(row)

     author = scholarly.fill(next(search_query))
     for index in range(len(author['publications'])):

         pub=scholarly.fill(author['publications'][index])
         print(pub['bib'])
         try:
             listapub.append({'investigador': row, 'year': pub['bib']['pub_year'], 'title': pub['bib']['title'],'author': pub['bib']['author'], 'journal': pub['bib']['journal']})
         except:
             pass
  print(listapub)
  return listapub

#anvil.server.wait_forever()
busca_publicaciones(['MADAIN PEREZ PATRICIO','Abiel Aguilar-González','Steven A Cholewiak'])

# Retrieve the author's data, fill-in, and print
#print(author)

# Print the titles of the author's publications
#print([pub.bib['title'] for pub in author.publications])

# Take a closer look at the first publication
#pub = author.publications[0].fill()
#print(pub)

# Which papers cited that publication?
#print([citation.bib['title'] for citation in pub.citedby])
# Retrieve the author's data, fill-in, and print
search_query = scholarly.search_author('Steven A Cholewiak')
author = scholarly.fill(next(search_query))
print(author)

# Print the titles of the author's publications
print([pub['bib']['title'] for pub in author['publications']])

# Take a closer look at the first publication
pub = scholarly.fill(author['publications'][0])
print(pub)

# Which papers cited that publication?
print([citation['bib']['title'] for citation in scholarly.citedby(pub)])