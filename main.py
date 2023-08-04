from tortoise import Tortoise, run_async
from models import Hotels, Rooms, Clients


async def create_tables():
    await Tortoise.init(
        db_url='sqlite://hotels.db',
        modules={'models': ['__main__']},
    )
    await Tortoise.generate_schemas()


async def create_data():
    hotel1 = await Hotels.create(name="Ronda", description="This is a hotel for the whole family right in the city center.", stars=3, minimal_price=2100)
    hotel2 = await Hotels.create(name="France", description="You will immerse yourself in the incredibly beautiful atmosphere of France", stars=5, minimal_price=10000)
    hotel3 = await Hotels.create(name="Mikasa", description="The hotel is built in oriental style and conveys the pure beauty of Asia", stars=4, minimal_price=7500)


    room11 = await Rooms.create(hotel=hotel1, count_of_persons=2, price=5500)
    room12 = await Rooms.create(hotel=hotel1, count_of_persons=1, price=2100)
    room13 = await Rooms.create(hotel=hotel1, count_of_persons=3, price=7800)

    room21 = await Rooms.create(hotel=hotel2, count_of_persons=2, price=15700)
    room22 = await Rooms.create(hotel=hotel2, count_of_persons=1, price=10000)
    room23 = await Rooms.create(hotel=hotel2, count_of_persons=4, price=24300)

    room31 = await Rooms.create(hotel=hotel3, count_of_persons=2, price=12000)
    room32 = await Rooms.create(hotel=hotel3, count_of_persons=1, price=7500)
    room33 = await Rooms.create(hotel=hotel3, count_of_persons=3, price=15600)


    await Clients.create(room=room11, full_name="Shawn Cook", phone_number=7955955, date_start='2022-01-01', date_end='2022-01-03')
    await Clients.create(room=room12, full_name="Eric May", phone_number=4387489, date_start='2022-02-07', date_end='2022-02-08')
    await Clients.create(room=room13, full_name="Fernando Sanchez", phone_number=5305108, date_start='2022-03-05', date_end='2022-03-11')

    await Clients.create(room=room21, full_name="Joshua Garcia", phone_number=9459903, date_start='2022-03-01', date_end='2022-02-01')
    await Clients.create(room=room22, full_name="Brian Wright", phone_number=3217013, date_start='2022-09-21', date_end='2022-09-03')
    await Clients.create(room=room23, full_name="Donald Tucker", phone_number=1315790, date_start='2022-01-01', date_end='2022-01-12')

    await Clients.create(room=room31, full_name="Lee Schwartz", phone_number=2184174, date_start='2022-01-08',date_end='2022-01-15')
    await Clients.create(room=room32, full_name="Christopher Larson", phone_number=2901946, date_start='2022-04-11', date_end='2022-04-07')
    await Clients.create(room=room33, full_name="Larry Jones", phone_number=7718953, date_start='2022-05-02', date_end='2022-05-07')


async def main():
    await create_tables()
    await create_data()

async def get_cheapest_room():
    query = "SELECT name, MIN(minimal_price) FROM Hotels"
    result = await Hotels.raw(query)
    return result

run_async(main())
get_cheapest_room()