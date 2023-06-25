from selenium import webdriver
import csv
from bs4 import BeautifulSoup


def my_url(keyword):
    temp = "https://www.amazon.com/s?k={}&ref=nb_sb_noss_1"
    keyword = keyword.replace(" ", "+")
    url = temp.format(keyword)
    url += "&page{}"
    return url


def extract_records(obj):
    atag = obj.h2.a
    description = obj.h2.a.text.strip()
    url = "https://www.amazon.com/" + atag.get("href")

    try:
        parent = obj.find("span", "a-price")
        price = parent.find("span", "a-offscreen").text
    except AttributeError:
        return None

    try:
        rate = obj.find("span", "a-icon-alt").text
        count_review = obj.find("span", {"class": "a-size-base", "dir": "auto"}).text
    except AttributeError:
        rate = ""
        count_review = ""

    image = obj.find("img", {"class": "s-image"}).get("src")
    result = (description, price, rate, count_review, url, image)
    return result


def main(keyword):
    driver = webdriver.Chrome()
    records = []
    url = my_url(keyword)

    for page in range(1, 3):
        driver.get(url.format(page))
        soup = BeautifulSoup(driver.page_source, "html.parser")
        soup_results = soup.find_all("div", {"data-component-type": "s-search-result"})

        for item in soup_results:
            record = extract_records(item)
            if record:
                records.append(record)

    with open("results.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["Description", "Price", "Rate", "Review Counts", "URL", "Image"]
        )
        writer.writerows(records)

    driver.quit()


main("school bag")
