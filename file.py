import csv
from scrapper import search_incruit

def save_to_csv(jobs):
    with open("download.csv", "w", encoding="utf-8-sig", newline="") as f:
        csv_writer = csv.writer(f)

        csv_writer.writerow(["No", "Co", "Title", "Loc", "MoreTnfo"])

        for i, job in enumerate(jobs):
            csv_writer.writerow([i+1, job["company"], job["title"], job["location"], job["link"]])