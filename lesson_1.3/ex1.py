#import requests as req
from bs4 import BeautifulSoup
import json
import tqdm
import time
data = {
    "data" : []
}

from requests_tor import RequestsTor
req = RequestsTor()

def soup_object(url, req):
    resp = req.get(url)
    soup = BeautifulSoup(resp.text, "lxml")

    return soup


def get_text_obj(obj):
    return obj.text if obj is not None else ""

for page in range(0,17):
    url = f"https://hh.ru/search/vacancy?clusters=true&enable_snippets=true&search_field=name&text=python+разработчик&page={page}&hhtmFrom=vacancy_search_list"
    soup = soup_object(url, req)
    tags = soup.find_all(attrs={"data-qa":"serp-item__title"})

    print(f"page {page} => {url}")

    for elem in tqdm.tqdm(tags):
        time.sleep(2)
        soup2 = soup_object(elem.attrs["href"], req)

        work_experiens = soup2.find("p", attrs={"class":"vacancy-description-list-item"})
        work_experiens = get_text_obj(work_experiens.find("span", attrs={"data-qa":"vacancy-experience"})) if work_experiens is not None else ""

        salary = get_text_obj(soup2.find(attrs={"data-qa":"vacancy-salary-compensation-type-net"}))

        region = get_text_obj(soup2.find(attrs={"data-qa":"vacancy-view-location"}))

        data['data'].append({'title': elem.text, 'work experiens': work_experiens, 'salary': salary, 'region': region})

        with open("hh.json", "w") as file:
            json.dump(data, file, ensure_ascii=False)