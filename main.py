# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
# import lxml
# import urllib
import os
from pdf import pdf
from download import download_chapters


def get_chapter_data(name, headers):
    chapter_page = []
    i = 0
    soup = []
    while True:
        chapter_page.append(requests.get('https://mangapoisk.ru/manga/' + name + '/chaptersList?infinite=1&page=' + str(i+1), headers = headers))
        soup.append(BeautifulSoup(chapter_page[i].text, "html.parser"))
        if soup[i].find('span', class_="chapter-title") == None: break
        i += 1
        print(i)
    chapter_data=[]
    soup.reverse()
    x = 0
    for soup_list in soup:
        chapters_list = soup_list.find_all('a', class_="")
        chapters_list.reverse()
        for chapter in chapters_list:
            chapter_data.append({'chapter_name': chapter.get('href').split('/')[4], 'chapter_link': chapter.get('href')})
        x += 1
        
    return(chapter_data)

def main(url, path, flag, cb):
        name = url.split('/')[4]
        print(cb)
        ua = UserAgent()
        headers={'UserAgent': ua.random}
        main_page = requests.get(url, headers = headers)
        main_soup = BeautifulSoup(main_page.text, "html.parser")
        title_name = main_soup.find('span', class_="post-name").text.strip()
        # print(title_name)

        chapter_data = get_chapter_data(name, headers)
        if flag == 'get_list':
            return chapter_data, title_name
        if flag == 'get_all':
            download_chapters(chapter_data, path, 0, title_name, cb)


if __name__ == '__main__':
    main()
