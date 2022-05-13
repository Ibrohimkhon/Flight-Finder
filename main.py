from datetime import *
from datetime import timedelta
from notification_manager import NotificationManager
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

ORIGIN_CITY_IATA = "WAW"

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification = NotificationManager()


print(sheet_data)

for row in sheet_data:
    row["iataCode"] = flight_search.get_destination_code(row["city"])

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA ,
        destination['iataCode'] ,
        from_time=tomorrow ,
        to_time=six_month_from_today
    )

    if flight and flight.price < destination["lowestPrice"]:
        notification.send_sms(
            message=f"Low price alert! only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to "
                    f"{flight.destination_city} - {flight.destination_airport} from {flight.out_date} to {flight.return_date}"
        )
data_manager.update_destination_codes()
