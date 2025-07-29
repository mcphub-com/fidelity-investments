import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/apidojo/api/fidelity-investments'

mcp = FastMCP('fidelity-investments')

@mcp.tool()
def v4_auto_complete(q: Annotated[str, Field(description='Symbol or company name')]) -> dict: 
    '''Get suggestions by term or phrase'''
    url = 'https://fidelity-investments.p.rapidapi.com/v4/auto-complete'
    headers = {'x-rapidapi-host': 'fidelity-investments.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def auto_complete(query: Annotated[str, Field(description='Symbol or company name')]) -> dict: 
    '''Auto suggestion by input name or quote. * This endpoint is deprecated'''
    url = 'https://fidelity-investments.p.rapidapi.com/auto-complete'
    headers = {'x-rapidapi-host': 'fidelity-investments.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v3_auto_complete(q: Annotated[str, Field(description='Symbol or company name')]) -> dict: 
    '''Auto suggestion by input name or quote'''
    url = 'https://fidelity-investments.p.rapidapi.com/v3/auto-complete'
    headers = {'x-rapidapi-host': 'fidelity-investments.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_auto_complete(q: Annotated[str, Field(description='Symbol or company name')]) -> dict: 
    '''Auto suggestion by input name or quote'''
    url = 'https://fidelity-investments.p.rapidapi.com/v2/auto-complete'
    headers = {'x-rapidapi-host': 'fidelity-investments.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'q': q,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def market_get_summary() -> dict: 
    '''Get recent market summary'''
    url = 'https://fidelity-investments.p.rapidapi.com/market/get-summary'
    headers = {'x-rapidapi-host': 'fidelity-investments.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def market_get_international() -> dict: 
    '''Get international markets information'''
    url = 'https://fidelity-investments.p.rapidapi.com/market/get-international'
    headers = {'x-rapidapi-host': 'fidelity-investments.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def market_get_orders() -> dict: 
    '''Get orders by Fidelity customers'''
    url = 'https://fidelity-investments.p.rapidapi.com/market/get-orders'
    headers = {'x-rapidapi-host': 'fidelity-investments.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def market_get_movers() -> dict: 
    '''Get market movers which are most actives, top gainers, top losers'''
    url = 'https://fidelity-investments.p.rapidapi.com/market/get-movers'
    headers = {'x-rapidapi-host': 'fidelity-investments.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def market_get_sectors() -> dict: 
    '''Get sectors performance'''
    url = 'https://fidelity-investments.p.rapidapi.com/market/get-sectors'
    headers = {'x-rapidapi-host': 'fidelity-investments.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def news_list_by_symbol(symbol: Annotated[str, Field(description='The value of symbol field returned in .../v4/auto-complete endpoint')],
                        endDate: Annotated[Union[str, None], Field(description="List news before this point of time. The date format must be yyyy-MM-dd'T'HH:mm:ss Ex : 2024-01-25T12:12:12")] = None,
                        count: Annotated[Union[int, float, None], Field(description='Limit number of items per response. Maximum is 50 Default: 21')] = None) -> dict: 
    '''Get news headlines by symbol'''
    url = 'https://fidelity-investments.p.rapidapi.com/news/list-by-symbol'
    headers = {'x-rapidapi-host': 'fidelity-investments.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'endDate': endDate,
        'count': count,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_get_details(storyId: Annotated[str, Field(description='The value of resId field returned in .../news/list-by-symbol endpoint')]) -> dict: 
    '''Get news content'''
    url = 'https://fidelity-investments.p.rapidapi.com/news/v2/get-details'
    headers = {'x-rapidapi-host': 'fidelity-investments.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'storyId': storyId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def news_list_top(symbol: Annotated[Union[str, None], Field(description='The symbol of quote, market, etc..., such as : IMRN. Only one is allowed at a time')] = None) -> dict: 
    '''List top news from all supported area'''
    url = 'https://fidelity-investments.p.rapidapi.com/news/list-top'
    headers = {'x-rapidapi-host': 'fidelity-investments.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def news_get_details(resId: Annotated[str, Field(description='The value of resId field returned in .../news/list-top endpoint, such as : 202003011902RTRSNEWSCOMBINED_KBN20O2GM-OUSBS_1')]) -> dict: 
    '''Get news details'''
    url = 'https://fidelity-investments.p.rapidapi.com/news/get-details'
    headers = {'x-rapidapi-host': 'fidelity-investments.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'resId': resId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def quotes_get_chart(symbol: Annotated[str, Field(description='Separated by comma for multiple symbols, support up to 3 symbols at a time')],
                     startDate: Annotated[str, Field(description='Date format must be strictly follow yyyy/MM/dd-HH:mm:ss')],
                     endDate: Annotated[str, Field(description='Date format must be strictly follow yyyy/MM/dd-HH:mm:ss')],
                     intraday: Annotated[Union[str, None], Field(description='Y or N')] = None,
                     granularity: Annotated[Union[int, float, None], Field(description='From 1 to 6, use with intraday to specify day or month Default: 1')] = None) -> dict: 
    '''Get information to draw chart'''
    url = 'https://fidelity-investments.p.rapidapi.com/quotes/get-chart'
    headers = {'x-rapidapi-host': 'fidelity-investments.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
        'startDate': startDate,
        'endDate': endDate,
        'intraday': intraday,
        'granularity': granularity,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def quotes_get_details(symbols: Annotated[str, Field(description='Separated by comma to query multiple symbols')]) -> dict: 
    '''Get quote information'''
    url = 'https://fidelity-investments.p.rapidapi.com/quotes/get-details'
    headers = {'x-rapidapi-host': 'fidelity-investments.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbols': symbols,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def quotes_get_mashup(symbol: Annotated[str, Field(description='Only one symbol is allowed')]) -> dict: 
    '''Get additional information for specific quote, market'''
    url = 'https://fidelity-investments.p.rapidapi.com/quotes/get-mashup'
    headers = {'x-rapidapi-host': 'fidelity-investments.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'symbol': symbol,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
