import wikipedia as wiki
import urllib.request as UR
from PIL import Image

wiki.set_user_agent("MyPythonApp/1.0 (contacts@example.com)")
wiki.set_lang("uk")

theme = input()
result = wiki.summary(theme, sentences=1)
wikiimages = wiki.page(theme).images

print(result)

req = UR.Request(wikiimages[0], headers={"User-Agent": "Mozilla/5.0"})
with UR.urlopen(req) as response, open(f"image.png", "wb") as file:
    file.write(response.read())
    img = Image.open("image.png")
    img.show()

for img in wikiimages:
    print(img)