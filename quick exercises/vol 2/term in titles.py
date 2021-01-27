miserable_flicks = ['Shame', 'Charlie Says', 'Martyrs', 'Sylvia', 'Ghost Story']
fun_flicks = ['John Wick 3', 'The Raid', 'Once Upon A Time In Hollywood', 'Amadeus']
dumb_flicks = ['Mortal Engines', 'Transformers', 'Number 23', 'Batman V Superman']

def search(term, titles): 
    found = list(filter(lambda title: term in title.lower(), titles))
    if len(found) == 0:
        return '\'{}\' was not found'.format(term)
    return found
    
print(search('mustard', miserable_flicks))
print(search('once', fun_flicks))
print(search('a', dumb_flicks))
