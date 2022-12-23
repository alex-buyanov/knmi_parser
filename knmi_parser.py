import sys
from datetime import date, timedelta

import requests
from bs4 import BeautifulSoup


def get_averages(url):
    response = requests.get(url)
    assert response.status_code == 200, f"Error response: {response.status_code}"
    html = response.text

    soup = BeautifulSoup(html, features="html.parser")
    table = soup.find(attrs={"id": "lopendemaandTable"})  # This is the table with actual data

    result = []
    for row in table.find(name="tbody").find_all(name="tr"):
        cell = row.getText(separator="\t").split("\t")[1]  # split table row in cells and get cell with average temp
        day_average = float(cell.replace(',', '.'))  # days are formatted with comma instead of dot
        result.append(day_average)

    return result


def main() -> []:
    url_template = "https://weerstatistieken.nl/{}/{}/full"  # passing some non-existing month returns the whole year
    place, year = sys.argv[1], int(sys.argv[2])

    # Get averages and check that either 365 or 366 days were received
    year_averages = get_averages(url_template.format(place, year))
    assert 365 <= len(year_averages) <= 366

    # Append date to each value and output it into stdout
    year_start = date(year, 1, 1)
    for i in range(len(year_averages)):
        date_str = (year_start + timedelta(days=i)).strftime("%Y-%m-%d")
        print(date_str, '\t', year_averages[i])


if __name__ == '__main__':
    # test args: "de-bilt" 2022
    main()
