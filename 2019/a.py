def calc_uber_price(type_chosed, min, km):
  if type_chosed == 1:
    price_min = 10
    price_km = 80
    base_fare = 100
    minimum_fare = 250
  else:
    price_min = 15
    price_km = 120
    base_fare = 150
    minimum_fare = 350
  time_cost = min * price_min
  distance_cost = km * price_km

  total_price = time_cost + distance_cost + base_fare

  if total_price < minimum_fare:
    total_price = minimum_fare

  return total_price
type_chosed, min, km = map(int ,input().split())
print(f"Price: {calc_uber_price(type_chosed, min, km)}")