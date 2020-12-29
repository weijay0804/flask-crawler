from flask import Flask, render_template

app = Flask(__name__)

prod_name = 'iphone'
prods = [
    {'title': 'Apple iPhone 12 Pro Max (128G)-石墨色(MGD73TA/A)', 'price': 37900, 'prod_img': 'https://c.ecimg.tw//items/DYAJDT1900AYT3S/000002_1608170468.jpg', 'prod_url': 'https://24h.pchome.com.tw/prod/DYAJDT-1900AYT3S', 'referer': 'pchome'},
    {'title': 'Apple iPhone 12 Pro Max (128G)-太平洋藍(MGDA3TA/A)', 'price': 37900, 'prod_img': 'https://c.ecimg.tw//items/DYAJDTA900AZDKF/000002_1604911106.jpg', 'prod_url': 'https://24h.pchome.com.tw/prod/DYAJDT-A900AZDKF', 'referer': 'pchome'},
    {'title': 'Apple iPhone 12 (128G)-藍色(MGJE3TA/A)', 'price': 27999, 'prod_img': 'https://c.ecimg.tw//items/DYAJ93A900AXPN8/000002_1603176717.jpg', 'prod_url': 'https://24h.pchome.com.tw/prod/DYAJ93-A900AXPN8', 'referer': 'pchome'},
    {'title': 'Apple iPhone 12 Pro Max (256G)-太平洋藍(MGDF3TA/A)', 'price': 41400, 'prod_img': 'https://c.ecimg.tw//items/DYAJDMA900AZDLR/000002_1604911239.jpg', 'prod_url': 'https://24h.pchome.com.tw/prod/DYAJDM-A900AZDLR', 'referer': 'pchome'},
    {'title': 'Apple iPhone 12 Pro Max (128G)-金色(MGD93TA/A)', 'price': 37900, 'prod_img': 'https://c.ecimg.tw//items/DYAJDT1900AYT3L/000002_1608170480.jpg', 'prod_url': 'https://24h.pchome.com.tw/prod/DYAJDT-1900AYT3L', 'referer': 'pchome'},
    {'title': 'Apple iPhone 12 Pro Max (128G)-金色(MGD93TA/A)', 'price': 37900, 'prod_img': 'https://c.ecimg.tw//items/DYAJDTA900AYWQ6/000002_1604383170.jpg', 'prod_url': 'https://24h.pchome.com.tw/prod/DYAJDT-A900AYWQ6', 'referer': 'pchome'},
    {'title': 'Apple iPhone 12 Pro Max (256G)-金色(MGDE3TA/A)', 'price': 41400, 'prod_img': 'https://c.ecimg.tw//items/DYAJDMA900AZDLM/000002_1604911197.jpg', 'prod_url': 'https://24h.pchome.com.tw/prod/DYAJDM-A900AZDLM', 'referer': 'pchome'},
    {'title': 'Apple iPhone 12 (128G)-黑色(MGJA3TA/A)', 'price': 27999, 'prod_img': 'https://c.ecimg.tw//items/DYAJ931900AY7WU/000002_1608263941.jpg', 'prod_url': 'https://24h.pchome.com.tw/prod/DYAJ93-1900AY7WU', 'referer': 'pchome'},
    {'title': 'Apple iPhone 12 (64G)-黑色(MGJ53TA/A)', 'price': 26488, 'prod_img': 'https://c.ecimg.tw//items/DYAJ2Y1900AY7VG/000002_1603770468.jpg', 'prod_url': 'https://24h.pchome.com.tw/prod/DYAJ2Y-1900AY7VG', 'referer': 'pchome'},
    {'title': 'Apple iPhone 12 mini (128G)-白色(MGE43TA/A)', 'price': 25500, 'prod_img': 'https://c.ecimg.tw//items/DYAJDNA900AZDO4/000002_1604911861.jpg', 'prod_url': 'https://24h.pchome.com.tw/prod/DYAJDN-A900AZDO4', 'referer': 'pchome'},
    {'title': 'Apple iPhone 12 Pro Max (256G)', 'price': 41400, 'prod_img': 'https://c.ecimg.tw//items/DYAJDMA900AZJI2/000002_1608859829.jpg', 'prod_url': 'https://24h.pchome.com.tw/prod/DYAJDM-A900AZJI2', 'referer': 'pchome'},
]

@app.route('/')
def index():
    return render_template('index.html',prod_name = prod_name, prods = prods)

if __name__ == '__main__':
    app.run(debug=True)