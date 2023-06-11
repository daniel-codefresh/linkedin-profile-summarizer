from langchain.serpapi import SerpAPIWrapper


def get_linkedin_profile_url(text: str) -> str:
    """
    Given a person's name, return their LinkedIn profile URL.
    """
    search_engine = SerpAPIWrapper()
    res = search_engine.results(f"{text}")

    url = ""
    if "link" in res["organic_results"][0].keys():
        url = res["organic_results"][0]["link"]

    return url
