import httpx


async def get_page(url: str):
    """
    Retrieve the page HTML content the for given URL
    """
    async with httpx.AsyncClient() as client:
        return await client.get(url)


async def post_on_page(url: str, params: dict):
    """
    Some pages require POST parameters to be sent in order to be accessed.
    """
    async with httpx.AsyncClient() as client:
        return await client.post(url=url, params=params)
