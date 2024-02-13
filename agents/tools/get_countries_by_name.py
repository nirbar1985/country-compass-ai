from typing import Optional

import requests
from langchain.tools import tool
from pydantic.v1 import BaseModel, Field, conlist
from requests import PreparedRequest


def prepare_and_log_request(base_url: str, params: Optional[dict] = None) -> PreparedRequest:
    """Prepare the request and log the full URL."""
    req = PreparedRequest()
    req.prepare_url(base_url, params)
    print(f'\033[92mCalling API: {req.url}\033[0m')
    return req


# from pydantic import BaseModel, Field, conlist


class Params(BaseModel):
    fields: Optional[conlist(str, min_items=1, max_items=27)] = Field(
        default=None, description='Fields to filter the output of the request.', examples=[
            "name", "topLevelDomain", "alpha2Code", "alpha3Code", "currencies", "capital", "callingCodes", "altSpellings", "region",
            "subregion", "population", "latlng", "demonym", "area", "gini", "timezones", "borders", "nativeName", "numericCode",
            "languages", "flag", "regionalBlocs", "cioc"
        ])


class PathParams(BaseModel):
    name: str = Field(..., description='Name of the country')


class RequestModel(BaseModel):
    params: Optional[Params] = None
    path_params: PathParams


@tool(args_schema=RequestModel)
def get_countries_by_name(path_params: PathParams, params: Optional[Params] = None):
    """Useful for when you need to answer questions about countries. Input should be a fully formed question."""
    base_url = f'https://restcountries.com/v3.1/name/{path_params.name}'

    effective_params = {"fields": ",".join(params.fields)} if params and params.fields else None

    req = prepare_and_log_request(base_url, effective_params)

    # Make the request
    response = requests.get(req.url)

    # Raise an exception if the request was unsuccessful
    response.raise_for_status()

    return response.json()
