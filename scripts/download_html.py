import asyncio
from typing import List
from urllib.parse import parse_qs, urlparse

import aiohttp


async def save_html(session: aiohttp.ClientSession, url: str) -> None:
    """
    URLからHTMLを取得し、ファイルに保存する。

    Parameters
    ----------
    session : aiohttp.ClientSession
        aiohttpのセッションオブジェクト。
    url : str
        HTMLを取得するURL。

    Returns
    -------
    None
    """
    async with session.get(url) as response:
        if response.status == 200:
            # urlのパラメータからlectureNoを抽出
            parsed_url = urlparse(url)
            query_params = parse_qs(parsed_url.query)
            lecture_no = query_params["lectureNo"][0]
            with open(f"data/html/{lecture_no}.html", "wb") as f:
                async for chunk in response.content.iter_chunked(1024):
                    f.write(chunk)
            print(f"{url} has been downloaded.")
        else:
            print(f"Failed to download {url}. Status: {response.status}")


async def check_urls(urls: List[str]) -> None:
    """複数のURLからHTMLを取得し、ファイルに保存する。

    Parameters
    ----------
    urls : List[str]
        HTMLを取得するURLのリスト。

    Returns
    -------
    None
    """
    async with aiohttp.ClientSession() as session:
        tasks = [save_html(session, url) for url in urls]
        await asyncio.gather(*tasks)


# メイン関数
async def main(urls: List[str]) -> None:
    """メイン関数。

    Parameters
    ----------
    urls : List[str]
        HTMLを取得するURLのリスト。

    Returns
    -------
    None
    """
    await check_urls(urls)


# URLリスト
with open("data/url_list.txt", "r") as f:
    urls = f.read().splitlines()
    # 学部のシラバスのURLのみを取得
    urls = [
        "https://www.k.kyoto-u.ac.jp/external/open_syllabus/" + url
        for url in urls
        if "la_syllabus" in url
    ]

if __name__ == "__main__":
    asyncio.run(main(urls))
