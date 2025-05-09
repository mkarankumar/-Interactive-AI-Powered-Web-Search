from googlesearch import search

#To collect the links of the search
def googlesearch(query, num_results=10):
    searched_links = []
    for result in search(query, num_results=num_results):
        searched_links.append(result)
    return searched_links 

if __name__ == "__main__":  
    query = input("Enter the query: ")
    d = googlesearch(query, num_results=10)
    print(d)  # Print the result
