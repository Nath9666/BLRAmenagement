import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.bricklink.com/catalogColors.asp'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'Accept-Language': 'fr-FR,fr;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Referer': 'https://search.brave.com/',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Sec-GPC': '1'
}

cookies = {
    'blCartBuyerID': '-249847159',
    'blckMID': '194f12cae7900000-3b2d0d26e207e08a',
    'BLNEWSESSIONID': 'V107419D4582EE72210A672CF614FFBC1FDEF7564A7E26BD4A182CEFC654647D619D324151F0D848B7142F6A70BD9724FD8',
    'ASPSESSIONIDAQDSBATR': 'HNFMGDCCPAEHFNEFCHPBBCEI',
    'blckSessionStarted': '1',
    'AWSALB': 'zU7T/wPxijsCPqpB3KEyyyJPn8hlaptHFp4xhhPgh73qOInP46T1a4yQDOZiro09Epj/AmX0uXH2kTUBaO9i6rsZcCRzJswyI86jt2D2k/YnsexW2wNGb4YVSUiz',
    'AWSALBCORS': 'zU7T/wPxijsCPqpB3KEyyyJPn8hlaptHFp4xhhPgh73qOInP46T1a4yQDOZiro09Epj/AmX0uXH2kTUBaO9i6rsZcCRzJswyI86jt2D2k/YnsexW2wNGb4YVSUiz',
    'aws-waf-token': '85127e5a-7165-4781-8138-0155c34dc1f1:EQoAfNlyIcliAQAA:cT3T8HKCeNyI0WeaDHvC+jL12VCZ2OyrvgDjR9IrKnx2fTTZ+cyQO6xVco4FjW3+n/Lcd+nOGGP0YBGZ4xWM3mjq/4SCSUjxwmkmRrtPadTqQ426twVuObUpN4Y0pWXYZQJ2qk8pDc1vtHVyHOSsTcGSTIXPYEjA8TVy2l4w+tEmkVsYQz3eowYz2V+Z4UKJ61q+2Xm8Qw3eCT4EB1hosnzxGbMOiihEFvG8kHaxajkx77e/z05X8jHS3Mwdemw1N2BkwL9HLLA='
}

response = requests.get(url, headers=headers, cookies=cookies)
if response.status_code == 200:
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.find_all('table', {'border': '0', 'cellpadding': '1', 'cellspacing': '0', 'width': '100%'})
    data = []

    inni = 0

    for table in tables:

        if inni == 0:
            type = "Solid"
        elif inni == 1:
            type = "Transparent"
        elif inni == 2:
            type = "Pearl Colors"
        elif inni == 3:
            type = "Satin Colors"
        elif inni == 4:
            type = "Metallic Colors"
        elif inni == 5:
            type = "Milky Colors"
        elif inni == 6:
            type = "Glitter Colors"
        elif inni == 7:
            type = "Speckle Colors"
        elif inni == 8:
            type = "Modulex Colors"

        inni += 1


        if table:
            rows = table.find_all('tr')[1:]  # Skip the header row
            for row in rows:
                cols = row.find_all('td')
                if len(cols) >= 9:
                    id = cols[0].text.strip()
                    name = cols[3].text.strip()
                    parts = cols[4].text.strip()
                    in_sets = cols[5].text.strip()
                    wanted = cols[6].text.strip()
                    for_sale = cols[7].text.strip()
                    color_timeline = cols[8].text.strip()
                    bgcolor = cols[1].get('bgcolor', '')

                    data.append({
                        id: {
                            "name": name,
                            "bgColor": bgcolor,
                            "type": type,
                            "Parts": parts,
                            "In Sets": in_sets,
                            "Wanted": wanted,
                            "For Sale": for_sale,
                            "Color Timeline": color_timeline
                        }
                    })

    # Sort data by ID
    data_sorted = sorted(data, key=lambda x: int(list(x.keys())[0]))  # Sort by ID

    # Write to JSON file
    with open('../material_brinklinks.json', 'w') as json_file:
        json.dump(data_sorted, json_file, indent=2)

    print('Table data has been saved')
else:
    print('Failed to retrieve the URL:', response.status_code)