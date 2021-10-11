# This is a sample Python script.
#My api key

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
   # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
   # print_hi('PyCharm')


#
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import requests
import pprint
#import json


def get_score(url, strategy):
    url_2_check = f"https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&key=AIzaSyAcebqSe3Mnp0EiPLsVm8NEfLvuyJi8lG8&category=PERFORMANCE&strategy={strategy}"
    # r = requests.get(url_2_check)
    # print(r.json())
    print(url_2_check)
    r = requests.get(url_2_check).json()
    return r['loadingExperience']['metrics']


def get_score_by_url(name, url, strategy='DESKTOP'):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # url_2_check = "https://developers.google.com/speed/docs/insights/v5/reference/pagespeedapi/runpagespeed?apix_params=%7B%22url%22%3A%22https%3A%2F%2Fwww.mtsbank.ru%22%2C%22category%22%3A%5B%22PERFORMANCE%22%5D%2C%22strategy%22%3A%22DESKTOP%22%7D"
    if strategy == 'ALL':
        desktop_result = get_score(url, 'DESKTOP')
        mobile_result = get_score(url, 'MOBILE')
        return {
            'desktop': desktop_result,
            'mobile': mobile_result
        }
    else:
        return get_score(url, strategy)


    # Press the green button in the gutter to run the script.


if __name__ == '__main__':
    DEFAULT_CHECK_URL = 'https://www.mtsbank.ru'
    DEFAULT_STRATEGY = 'DESKTOP'

    user_url = input("Enter url to check ") or DEFAULT_CHECK_URL
    user_strategy = input("Enter strategy ALL/DESKTOP/MOBILE ") or DEFAULT_STRATEGY

    print(f'Using {user_strategy} for {user_url}')

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(get_score_by_url('PyCharm', user_url, user_strategy))

    # print("desktop by default")
    # print(get_score_by_url('PyCharm', user_url))
    #
    # print("mobile")
    # print(get_score_by_url('PyCharm',user_url, 'MOBILE'))
    #
    # print("all")
    # print(get_score_by_url('PyCharm', user_url, 'ALL'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

