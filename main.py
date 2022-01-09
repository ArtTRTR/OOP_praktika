from typing import List

class Trip:
    def __init__(self, distance: float, comment: str = "Просто поездка") -> None:
        self.distance = distance
        self.comment = comment


class Transport:
    def __init__(self, fuel: int, trips: List[Trip]) -> None:
        self.fuel = fuel
        self.trips = trips

    def add_trips(self, trip: Trip) -> None:
        """Добавить поездку"""

        self.trips.append(trip)

    def sum_trip_distance(self) -> float:
        """Рассчитать всю пройденную дистанцию данного вида транспорта"""

        return sum ([trip.distance for trip in self.trips])

    def calc_reachable_deistance(self):
        """Рассчитывает оставшийся путь транспортного средства с учетом совершенных поездок"""
        raise NotImplementedError("Для базоваого класса нет реализации этого метода")


class Car(Transport):
    FUEL_CONSUMPTION_CAR = 0.12 #л/км
    def calc_reachable_distance(self) -> str:
        result = (self.fuel - self.sum_trip_distance() * self.FUEL_CONSUMPTION_CAR) // self.FUEL_CONSUMPTION_CAR
        return f'Машине осталось ехать {result} км.'


class Airplane(Transport):
    FUEL_CONSUMPTION_AIRPLANE = 200

    def calc_reachable_distance(self):
        result = (self.fuel - self.sum_trip_distance() * self.FUEL_CONSUMPTION_AIRPLANE) // self.FUEL_CONSUMPTION_AIRPLANE
        return f'Самолету осталось лететь {result}'


audi = Car(70, [
    Trip(200, "Калуга-Москва"),
    Trip(50, "В лес")
    ])

print(audi.calc_reachable_distance())
