import requests


class Feedbacks:
    def parse_feedbacks(self, articles: list):
        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'dnt': '1',
            'origin': 'https://www.wildberries.ru',
            'referer': 'https://www.wildberries.ru/catalog/0/search.aspx?search={query}&xsearch=true',
            'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/92.0.4515.159 Safari/537.36',
        }
        feedbacks_data = []
        for i in articles:
            # Получаем информацию о товаре
            url = f'https://card.wb.ru/cards/detail?spp=34&' \
                  f'regions=80,64,83,4,38,33,70,82,69,68,86,75,30,40,48,1,22,66,31,71' \
                  f'&pricemarginCoeff=1.0&reg=1&appType=1&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=12,3,18,15,21' \
                  f'&sppFixGeo=4&dest=-1029256,-102269,-2162196,-1257484&nm={i}'
            data = requests.get(url, headers=headers).json()
            # Проверяем, есть ли отзывы
            if data['data']['products'][0]['feedbacks'] > 0:
                imt_id = data['data']['products'][0]['root']

                for cnt in range(1, 5):
                    url = f'https://feedbacks{cnt}.wb.ru/feedbacks/v1/{imt_id}'
                    res = requests.get(url).json()
                    if res['feedbacks']:
                        feedbacks_data.extend(res['feedbacks'][:3])
                        break
        return feedbacks_data


def main():
    articles = [125408065, 125408065]

    c = Feedbacks()
    print(c.parse_feedbacks(articles))


if __name__ == '__main__':
    main()
