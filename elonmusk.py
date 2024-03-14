import yaml
import requests


class ScraperElon:
    def __init__(self, quantity: int):
        """Initializing the configuration and how many posts you need to get"""

        with open('config_twitter/cfg.yaml', encoding='utf8') as f_:
            data_ = yaml.load(f_, Loader=yaml.FullLoader)

        self.headers = data_.get('headers')
        self.params = data_.get('params')
        self.url = data_.get('url')
        self.quantity = quantity + 1

    def __writing_txt(self, data: str):
        """Method for writing data to csv"""
        with open('result_elon.txt', 'a', encoding='utf8') as f:
            f.write(data + '\n\n')

    def get_posts(self):
        """Post parsing"""

        response = requests.get(self.url, headers=self.headers, params=self.params)

        if response.status_code == 200:
            posts = response.json().get('data').get('user').get('result').get('timeline_v2').get('timeline') \
                .get('instructions')[1].get('entries')

            for p in range(0, self.quantity):
                self.__writing_txt(posts[p].get('content').get('itemContent').get('tweet_results').get('result') \
                                   .get('legacy').get('full_text'))

        else:
            print(f'Status code {response}')


if __name__ == '__main__':
    run = ScraperElon(10)
    run.get_posts()
