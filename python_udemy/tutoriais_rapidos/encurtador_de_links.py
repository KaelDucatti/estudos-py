import pyshorteners


url = input("Digite a URL: \n")
s = pyshorteners.Shortener()
short_url = s.tinyurl.short(url)
print(short_url)
