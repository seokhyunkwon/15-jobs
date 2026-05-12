import keyword

import requests
from bs4 import BeautifulSoup

# keyword="파이썬"
# url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}"
# response = requests.get(url)
#print(response.text)

# soup = BeautifulSoup(response.text, "html.parser")
# lis = soup.find_all("li", class_="c_col")
# print(len(lis))
# print(lis[0])

def search_incruit(keyword, pages):

    jobs = []
    for i in range(pages):
        page = i * 30
        # keyword="파이썬"

        url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno={page}"
        # print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        lis = soup.find_all("li", class_="c_col")
    
        for li in lis:
            company = li.find("a", class_="cpname").text.strip()
            title = li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a").text.strip()
            location = li.find("div", class_="cl_md").find_all("span")[0].text.strip()
            history = li.find("div", class_="cl_md").find_all("span")[1].text.strip()
            edu = li.find("div", class_="cl_md").find_all("span")[2].text.strip()
            job_type = li.find("div", class_="cl_md").find_all("span")[3].text.strip()
            link = li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a").get("href")
            # print(company,"||", title,"||", location,"||", history,"||", edu,"||", job_type,"||", link)

            job_data = {
                "company": company,
                "title": title,
                "location": location,
                "history": history,
                "edu": edu,
                "job_type": job_type,
                "link": link
                }
            jobs.append(job_data)

    return jobs


def search_saramin(keyword, pages):
    jobs = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    for i in range(pages):
        page = i + 1
        url = f"https://www.saramin.co.kr/zf_user/search/recruit?searchword={keyword}&recruitPage={page}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        lis = soup.find_all("div", class_="item_recruit")

        for li in lis:
            company = li.find("strong", class_="corp_name").text.strip()
            title_link = li.select_one("h2.job_tit > a")
            title = title_link.get_text(strip=True) if title_link else ""
            link = "https://www.saramin.co.kr" + title_link.get("href") if title_link else ""
            location = " ".join([a.get_text(strip=True) for a in li.select("div.job_condition span a")])

            job_data = {
                "company": company,
                "title": title,
                "location": location,
                "link": link
            }
            jobs.append(job_data)
    return jobs





# keyword = "파이썬"
# url = f"https://www.jobkorea.co.kr/Search?stext={keyword}&tabType=recruit&Page_No=1"
# response = requests.get(url)
# print(response.status_code)
# print(response.text)    




