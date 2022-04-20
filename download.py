from pdf import pdf
import requests
from bs4 import BeautifulSoup
import os

def download_chapters(chapter_data, path, selected_chapters, title_name, cb) :
    print(title_name)
    # print(selected_chapters)
    link_list = []
    chapter_number = []
    if selected_chapters != 0:
        for choise in selected_chapters:
            for data in chapter_data:
                if data['chapter_link'].split('/')[4] == choise:
                    link_list.append(data['chapter_link'])
                    chapter_number.append(data['chapter_link'].split('/')[4])
            print(link_list)
    if selected_chapters == 0:
        for data in chapter_data:
            link_list.append(data['chapter_link'])
            chapter_number.append(data['chapter_link'].split('/')[4])
        # print(link_list)
        # for data in chapter_data:
        #     link_list.append(data['chapter_link'])

    
    j = 0
    for link in link_list:   
        print(link)
        sheet_page = requests.get('https://mangapoisk.ru' + link)
        soup_page= BeautifulSoup(sheet_page.text, "html.parser")
        chapter_path = path + '/' + title_name + '/Глава' + chapter_number[j]
        print(chapter_path)
        if os.path.isdir(chapter_path) == False:
            os.makedirs(chapter_path)
            # print(o)
        # print(os.path.isdir(chapter_path)
        if soup_page.find('img', class_="img-fluid page-image") != None:
            sheet_0 = soup_page.find('img', class_="img-fluid page-image")
            p = requests.get((soup_page.find('img', class_="img-fluid page-image")).get('src'))
            out = open(chapter_path + '/img0.jpg', "wb")
            out.write(p.content)
            out.close()
        if soup_page.find('img', class_="img-fluid page-image lazy lazy-preload") != None:
            sheet_list = soup_page.find_all('img', class_="img-fluid page-image lazy lazy-preload")
            i = 1
            for i_sheet in sheet_list:
                sheet = i_sheet.get('data-src')
                p = requests.get(sheet)
                out = open(chapter_path + '/img' + str(i) + '.jpg', "wb")
                out.write(p.content)
                out.close()
                i += 1
        if cb['PDF'] == 'on':
            pdf(cb['DEL'], chapter_path, i, chapter_number[j])
        j += 1
    return