import json
from selenium import webdriver
import yaml
import requests
from fake_useragent import UserAgent


class ScraperElon:
    URL = "https://api.twitter.com/graphql/eS7LO5Jy3xgmd3dbL044EA/UserTweets"
    URL_ID = "https://api.twitter.com/graphql/k5XapwcSikNsEsILW5FvgA/UserByScreenName"
    TOKEN = "AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA"

    def __init__(self, username: str, quantity: int, proxy: str = None):
        """Initializing the configuration and how many posts you need to get"""


        self.username = username
        self.quantity = quantity + 1
        self.proxy = {'http': proxy, 'https': proxy} if proxy else None
        self.headers = self.__get_headers()
        self.params = self.__collecting_parameters()

    def __get_headers(self):
        """Method for getting headers"""
        useragent = UserAgent()
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")

        driver = webdriver.Chrome(options=options)

        driver.get("https://twitter.com/")

        cookies = {}
        for cookie in driver.get_cookies():
            cookies[cookie['name']] = cookie['value']
        headers = {
            'authority': 'api.twitter.com',
            'accept': '*/*',
            'accept-language': 'ru,en;q=0.9',
            'authorization': f'Bearer {self.TOKEN}',
            'content-type': 'application/json',
            'origin': 'https://twitter.com',
            'referer': 'https://twitter.com/',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "YaBrowser";v="24.1", "Yowser";v="2.5"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': f'{useragent.random}',
            'x-client-transaction-id': '6uK+6nC7ghVIkBnUvJOWZicz4lQbudUjPUXplkZ6ExbyjDyNdMlvddWRNtubXD7rA3zVSetIyBmC8VASqIeNwgEBMmuK6w',
            'x-guest-token': cookies.get('gt'),
            'x-twitter-active-user': 'yes',
            'x-twitter-client-language': 'ru',
        }
        return headers

    def __collecting_parameters(self):
        """Method for collecting parameters"""
        parm = {
            "userId": self.__get_id_user(),
            "count": 20,
            "includePromotedContent": True,
            "withQuickPromoteEligibilityTweetFields": True,
            "withVoice": True,
            "withV2Timeline": True
        }

        params = {
            'variables': json.dumps(parm),
            'features': '{"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_timeline_navigation_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"c9s_tweet_anatomy_moderator_badge_enabled":true,"tweetypie_unmention_optimization_enabled":true,"responsive_web_edit_tweet_api_enabled":true,"graphql_is_translatable_rweb_tweet_is_translatable_enabled":true,"view_counts_everywhere_api_enabled":true,"longform_notetweets_consumption_enabled":true,"responsive_web_twitter_article_tweet_consumption_enabled":true,"tweet_awards_web_tipping_enabled":false,"freedom_of_speech_not_reach_fetch_enabled":true,"standardized_nudges_misinfo":true,"tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled":true,"rweb_video_timestamps_enabled":true,"longform_notetweets_rich_text_read_enabled":true,"longform_notetweets_inline_media_enabled":true,"responsive_web_enhance_cards_enabled":false}',
        }

        return params

    def __get_id_user(self):
        """The method of obtaining the user ID"""
        variables = {"screen_name": self.username, "withSafetyModeUserFields": True}
        params = {
            'variables': json.dumps(variables),
            'features': '{"hidden_profile_likes_enabled":true,"hidden_profile_subscriptions_enabled":true,"responsive_web_graphql_exclude_directive_enabled":true,"verified_phone_label_enabled":false,"subscriptions_verification_info_is_identity_verified_enabled":true,"subscriptions_verification_info_verified_since_enabled":true,"highlights_tweets_tab_ui_enabled":true,"responsive_web_twitter_article_notes_tab_enabled":true,"creator_subscriptions_tweet_preview_api_enabled":true,"responsive_web_graphql_skip_user_profile_image_extensions_enabled":false,"responsive_web_graphql_timeline_navigation_enabled":true}',
            'fieldToggles': '{"withAuxiliaryUserLabels":false}',
        }
        response = requests.get(
            url=self.URL_ID,
            params=params,
            headers=self.headers,
            proxies=self.proxy
        ).json().get('data').get('user').get('result').get('rest_id')

        return response

    def __writing_txt(self, data: str):
        """Method for writing data to csv"""
        with open(f'result_{self.username}.txt', 'a', encoding='utf8') as f:
            f.write(data + '\n\n')

    def get_posts(self):
        """Post parsing"""

        response = requests.get(self.URL, headers=self.headers, params=self.params, proxies=self.proxy)

        if response.status_code == 200:
            posts = response.json().get('data').get('user').get('result').get('timeline_v2').get('timeline') \
                .get('instructions')[1].get('entries')

            for p in range(0, self.quantity):
                self.__writing_txt(posts[p].get('content').get('itemContent').get('tweet_results').get('result') \
                                   .get('legacy').get('full_text'))

        else:
            print(f'Status code {response}')


if __name__ == '__main__':
    run = ScraperElon(username='elonmusk', quantity=10)
    run.get_posts()
