import scrapy
import re
from unicodedata import normalize

# Ce fichier est un "Spider" pour "Scrapy", qui permet de scanner le site de l'assemblée narionale
# afin de récupérer la liste des élus, leurs informations et leur photo
# 
# - Usage :
#   scrapy runspider deputes-scrapy.py -o deputes.json

_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.:]+')

def slugify(text, delim=u'-'):
    """Generates an slightly worse ASCII-only slug."""
    result = []
    for word in _punct_re.split(text.lower()):
        word = normalize('NFKD', word).encode('ascii', 'ignore')
        if word:
            result.append(word)
    return unicode(delim.join(result))

def extractCss(response, selector) :
    res = response.css(selector).extract_first()
    if res is None :
        return None 
    else :
        return res.strip()

def extractXPath(response, selector) :
    res = response.xpath(selector).extract_first()
    if res is None :
        return None 
    else :
        return res.strip()

class BlogSpider(scrapy.Spider):
    
    name = 'blogspider'
    start_urls = ['http://www2.assemblee-nationale.fr/deputes/liste/alphabetique']
    # start_urls =  ["http://www2.assemblee-nationale.fr/deputes/fiche/OMC_PA605922"]
    

    def parse(self, response):
        for url in response.css('a::attr("href")').re('.*/deputes/fiche/.*'):
            yield scrapy.Request(response.urljoin(url), self.parse_depute)


    def parse_depute(self, response) :
        res = {}
        
        nom = response.css("h1::text").extract_first().strip()
        
        if nom.startswith("Mme") :
            res['genre'] = "F"
        else :
            res['genre'] = "M"

    
        nom = re.sub("^M\w*\s*", "", nom)
        res['nom'] = nom
        res['id'] = slugify(nom)
        res['departement'] = extractCss(response, "span.nom-departement::text")
        res['parti'] = extractXPath(response, '//dt[contains(text(),"Rattachement")]/following-sibling::dd[1]/ul/li/text()')
        res['groupe'] = extractCss(response, "#deputes-illustration span a::text")
        res["emails"] = map(lambda href : href.replace("mailto:", "").strip(), set(response.css("a::attr('href')").re('.*mailto.*')))
        res["site"] = extractXPath(response, '//dd[contains(text(), "Site internet")]/a/text()')

        # Launch downloadof image
        img_url = response.urljoin(extractCss(response, "div.deputes-image img::attr('src')"))
        yield scrapy.Request(img_url, self.parse_img, meta = {'id' : res['id']})

        yield res
    
    def parse_img(self, response):
        id = response.meta['id']
        filename = 'img/' + id + '.jpg'
        with open(filename, 'wb') as f:
            f.write(response.body)

    def parse_titles(self, response):
        for post_title in response.css('div.entries > ul > li a::text').extract():
            yield {'title': post_title}


