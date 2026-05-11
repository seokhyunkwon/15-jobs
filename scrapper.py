import requests
from bs4 import BeautifulSoup

keyword="파이썬"
url = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}"
response = requests.get(url)
#print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
lis = soup.find_all("li", class_="c_col")
# print(len(lis))
# print(lis[0])

for li in lis:
    company = li.find("a", class_="cpname").text.strip()
    title = li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a").text.strip()
    location = li.find("div", class_="cl_md").find_all("span")[0].text.strip()
    history = li.find("div", class_="cl_md").find_all("span")[1].text.strip()
    edu = li.find("div", class_="cl_md").find_all("span")[2].text.strip()
    job_type = li.find("div", class_="cl_md").find_all("span")[3].text.strip()
    link = li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a")
    print(company,"||", title,"||", location,"||", history,"||", edu,"||", job_type,"||", link.get("href"))






