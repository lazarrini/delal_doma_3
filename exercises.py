import models


async def get_cheapest_room():
    query = "SELECT name, MIN(minimal_price) FROM Hotels"
    result = await models.Hotels.raw(query)
    return result

get_cheapest_room()