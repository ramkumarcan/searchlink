page = 'ram this is the link k="www.google.com" lets find it if you can'
start_link = page.find("k=")
start_quote = page.find('"',start_link)
end_quote = page.find('"',start_quote +1)
url = page[start_quote +1: end_quote]
print url
raw_input("Press<enter>")
