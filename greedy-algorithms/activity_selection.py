
activities = [
    ["A1", 0, 6],
    ["A2", 3, 4],
    ["A3", 1, 2],
    ["A4", 5, 8],
    ["A5", 5, 7],
    ["A6", 8, 9],
]


def print_max_activities(activities):
    activities.sort(key=lambda x: x[2])
    print(activities)


print_max_activities(activities)
