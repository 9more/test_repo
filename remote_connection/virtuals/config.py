CLIENTS = {
    "1": "BETFRED",
    "2": "CORAL",
    "3": "LADBROKES",
}

CLIENT_CATEGORIES = {
    "BETFRED": {
        1: "CARS",
        2: "SPEEDWAY",
        3: "CYCLING",
        4: "TENNIS",
        7: "DOGS",
        8: "HD FOOTBALL",
        9: "BINGO",
        13: "DARTS",
        14: "DASH HORSES",
        18: "HORSES v2",
        19: "HD DASH DOGS",
    },
    "CORAL": {
        1: "Horses (Victor Park)",
        2: "Dogs (BARKING HALL)",
        3: "Motor Racing (SILVER CIRCUIT)",
        5: "Sprints (SURREY DOWNS)",
        6: "Jumps (WORKINGFORD)",
        7: "Dogs 2 (HOUND HILL)",
    },
    "LADBROKES": {
        1: "Horses Flats",
        2: "Rush Dogs",
        3: "Motor-Racing",
        6: "Horses Jumps",
    },
}


for key, value in CLIENT_CATEGORIES[CLIENTS["3"]].items():
    print(f"Type {key} for {value}")
