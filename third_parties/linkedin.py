# import json

import requests
import os

api_key = os.getenv("PROXYCURL_API_KEY")


def scrape_linkedin_profile(url):
    """Scrapes a linkedin profile and returns a dictionary of the profile"""

    # with open("daniel_soifer_linkedin_profile.json", "r") as f:
    #     linkedin_profile = json.load(f)

    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dic = {"Authorization": "Bearer " + api_key}
    params = {
        "url": url,
    }
    response = requests.get(api_endpoint, params=params, headers=header_dic)

    linkedin_profile = response.json()

    return clean_linkedin_profile(linkedin_profile)


def clean_linkedin_profile(linkedin_profile):
    """Cleans a linkedin profile dictionary"""
    linkedin_profile_without_empty_fields = clean_dict_from_empty_value_fields(
        linkedin_profile
    )
    if linkedin_profile_without_empty_fields.get("people_also_viewed"):
        del linkedin_profile_without_empty_fields["people_also_viewed"]
    if linkedin_profile_without_empty_fields.get("certifications"):
        del linkedin_profile_without_empty_fields["certifications"]

    if linkedin_profile_without_empty_fields.get("groups"):
        for group in linkedin_profile_without_empty_fields["groups"]:
            del group["profile_pic_url"]

    return linkedin_profile_without_empty_fields


def clean_dict_from_empty_value_fields(dic):
    return {key: value for key, value in dic.items() if value}
