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
    jobs_s = []
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
            # Extract title and link
            title_link = li.find("a", class_="data_layer")
            if title_link:
                title = title_link.get_text().strip()
                link = "https://www.saramin.co.kr" + title_link.get("href")
            else:
                continue
            
            # Extract company and location from text
            text = li.get_text()
            
            # Company - look for company name patterns
            company = ""
            # Try to find company name in the text
            lines = [line.strip() for line in text.split('\n') if line.strip() and len(line) > 1]
            for line in lines:
                # Skip lines that are clearly not company names
                if any(skip in line for skip in ['스크랩', '입사지원', '오늘마감', '만원', '외', '수정일', '공고 모아보기', '기업정보', '관심기업']):
                    continue
                # Look for company-like patterns
                if ('(' in line and ')' in line) or len(line) > 3:
                    company = line
                    break
            
            # If still no company, try the last meaningful line
            if not company:
                for line in reversed(lines):
                    if len(line) > 2 and not any(char.isdigit() for char in line):
                        company = line
                        break
            
            # Location - look for common city names
            location = ""
            cities = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"]
            for city in cities:
                if city in text:
                    location = city
                    break
            
            job_data = {
                "company": company,
                "title": title,
                "location": location,
                "link": link
            }
            jobs_s.append(job_data)
    return jobs_s





# keyword = "파이썬"
# url = f"https://www.jobkorea.co.kr/Search?stext={keyword}&tabType=recruit&Page_No=1"
# response = requests.get(url)
# print(response.status_code)
# print(response.text)    
    
    
    
    
    




