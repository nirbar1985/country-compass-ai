from langchain.tools import tool
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper


@tool
def countries_image_generator(country: str):
    """Call this to get an image of a country"""
    res = DallEAPIWrapper(model="dall-e-3").run(f"You generate image of a country representing the most typical country's characteristics,\
        incorporating its flag. the country is {country}")

    answer_to_agent = (f"Use this format- Here is an image of {country}: [{country} Image]"
                       f"url= {res}")
    return answer_to_agent
