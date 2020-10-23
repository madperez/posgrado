from scholarly import scholarly
import anvil.server

anvil.server.connect("WTILNCT6433IFN3C6UHKGVAU-BBOZIA6PRHGNNBOK")

@anvil.server.callable
def busca_publicaciones(lista):
  listapub=[]
  for row in lista:
     print(row)
     search_query = scholarly.search_author(row)
     author = next(search_query).fill()
    # for pub in author.publications:
     for pub in range(len(author.publications)):
        print(pub)
        try:
            cdata=author.publications[pub].fill()
            print(cdata)
            listapub.append({'investigador':row,'year':cdata.bib['year'],'title':cdata.bib['title'], 'author':cdata.bib['author'], 'journal':cdata.bib['journal']})
        except:
            pass
     #print(next(scholarly.search_author(row)))
  print(listapub)
  return listapub

anvil.server.wait_forever()


# Retrieve the author's data, fill-in, and print
#print(author)

# Print the titles of the author's publications
#print([pub.bib['title'] for pub in author.publications])

# Take a closer look at the first publication
#pub = author.publications[0].fill()
#print(pub)

# Which papers cited that publication?
#print([citation.bib['title'] for citation in pub.citedby])
