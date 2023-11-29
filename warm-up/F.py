max_count_in_lift = int(input())
count_of_floors = int(input())
office = [1] + [int(input()) for _ in range(count_of_floors)]
# print(office)

time = 0
now_count_in_lift = 0
highest_completed_floor = 0

# Находим самый высокий этаж, на котором есть люди
for floor_now in range(count_of_floors, -1, -1):
    if office[floor_now] != 0:
        highest_completed_floor = floor_now
        break

# Пока на нулевом этаже есть люди
while office[0] != 0:
    # Поднимаемся на самый высокий этаж с людьми
    for floor_now in range(highest_completed_floor, -1, -1):
        if office[floor_now] != 0:
            time += floor_now
            break

    if office[highest_completed_floor] > max_count_in_lift:
        if office[highest_completed_floor] // max_count_in_lift > 1:
            time += highest_completed_floor * (office[highest_completed_floor] // max_count_in_lift) * 2
            office[highest_completed_floor] %= max_count_in_lift
            if office[highest_completed_floor] == 0:
                time -= 2

    # Собираем людей с этажей, пока в лифте есть место
    for floor_now in range(highest_completed_floor, -1, -1):
        if now_count_in_lift + office[floor_now] < max_count_in_lift:
            now_count_in_lift += office[floor_now]
            office[floor_now] = 0
        else:
            office[floor_now] -= max_count_in_lift - now_count_in_lift
            now_count_in_lift = max_count_in_lift
            break

    time += highest_completed_floor
    now_count_in_lift = 0

    for floor_now in range(highest_completed_floor, -1, -1):
        if office[floor_now] != 0:
            highest_completed_floor = floor_now
            break

print(time)
