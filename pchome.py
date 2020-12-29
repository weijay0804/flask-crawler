import requests
import json
import time
import openpyxl

'''爬取pchome商品資訊'''

keyword = input('輸入關鍵字: ')

pages = 3

header = {'cookie': 'ECC=GoogleBot',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

def pchome(keyword,data_list = []):
    '''取得產品清單'''
    for page in range(1,pages):
        url = f'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={keyword}%2012&page={page}&sort=sale/dc'
        response = requests.get(url,headers = header)
        try:
            prods = response.json()['prods']
            for prod in prods:
                prod_id = prod['Id']
                prod_img_id = prod['picS']
                prod_img = f'https://c.ecimg.tw/{prod_img_id}'
                prod_url = f'https://24h.pchome.com.tw/prod/{prod_id}'
                data_list.append({
                    'title':prod['name'],
                    'price':prod['price'],
                    'prod_img':prod_img,
                    'prod_url':prod_url,
                    'referer':'pchome',
                })
        except:
            return f'找不到與 "{keyword}" 有關的商品'
            break
    
    return data_list

pchomes = pchome(keyword)

with open('pchome.txt','w', encoding='utf-8') as f:
    for p in pchomes:
        f.write(str(p) +',' + '\n')



    





