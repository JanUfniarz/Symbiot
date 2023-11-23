from typing import Any

import requests
from bs4 import BeautifulSoup

from requests import Response


def get_stack_overflow_thread(thread_url) -> dict:
    def votes(post) -> int:
        res = post.find_next('div', class_='js-vote-count')
        if res:
            return int(res.attrs.get("data-value", ""))
        return 0

    response: Response = requests.get(thread_url)
    if response.status_code != 200:
        raise Exception(f"HTTP ERROR:\n\tstatus_code: {response.status_code}")

    soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')

    elements: list[dict[str, Any]] = [dict(
        content=post.decode_contents(),
        votes=votes(post))
        for post in soup.find_all('div', class_='js-post-body')]

    temp = list(map(lambda el: el["votes"], elements))

    for it in range(1, len(elements)):
        elements[it]["votes"] = temp[it - 1]

    elements[0]["votes"] = int(soup.find('div', class_='js-vote-count').attrs.get("data-value", "N/A"))

    return dict(
        thread_title=soup.find('a', class_='question-hyperlink').text.strip(),
        question=elements[0],
        answers=elements[1:])


if __name__ == "__main__":
    url: str = "https://stackoverflow.com/questions/258028/script-debugging-not-working-vs-2008"
    thread: dict = get_stack_overflow_thread(url)
    print(thread)
