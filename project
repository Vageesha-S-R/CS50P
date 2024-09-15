import requests
from tabulate import tabulate
import sys

def main():
    functions = [{"functions": "Driver Standings", "code": "a"}, {"functions": "Race Result", "code": "b"}]
    print(tabulate(functions, headers="keys", tablefmt="fancy_grid"))
    code = input("Select any function by typing its code: ").strip().lower()
    if code == "a":
        year = get_year_input("Enter the F1 season year (yyyy): ")
        standings = driver_standings(year)
        print_table(standings)
    elif code == "b":
        year = get_year_input("Enter the F1 season year (yyyy): ")
        round_num = get_round_input("Enter the round: ")
        result, circuit_name = race_result(year,round_num)
        print(f"------Race Name: {circuit_name} ------")
        print_table(result)
    else:
        print("Invalid code. Please select a valid function.")

def driver_standings(year):
    response = requests.get(f"https://ergast.com/api/f1/{year}/driverStandings.json")
    if response.status_code != 200:
        sys.exit(f"Failed to retrieve data: HTTP {response.status_code}")

    data = response.json()
    standings = data["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]
    records = []
    for s in standings:
        driver = s["Driver"]
        records.append({"Position": s["position"],"Driver Name": f"{driver['givenName']} {driver['familyName']}","Total Points": s["points"]})
    return records

def race_result(year,round_num):
    response = requests.get(f"https://ergast.com/api/f1/{year}/{round_num}/results.json")
    if response.status_code != 200:
        sys.exit(f"Failed to retrieve data: HTTP {response.status_code}")

    data = response.json()
    results = data["MRData"]["RaceTable"]["Races"]
    if not results:
        sys.exit("No results found for the selected round.")
    circuit_name = results[0]["raceName"]
    records = []
    for s in results[0]["Results"]:
        driver = s["Driver"]
        records.append({"Position": s["position"],"Driver Name": f"{driver['givenName']} {driver['familyName']}","Points": s["points"]})

    return records, circuit_name

def get_year_input(prompt):
    while True:
        try:
            year = int(input(prompt))
            if year < 1950:
                print("Year must be 1950 or later.")
            else:
                return year
        except ValueError:
            print("Invalid input. Please enter a valid year.")

def get_round_input(prompt):
    while True:
        try:
            round_num = int(input(prompt))
            if round_num < 1:
                print("Round number must be 1 or greater.")
            else:
                return round_num
        except ValueError:
            print("Invalid input. Please enter a valid round number.")

def print_table(s):
    print(tabulate(s, headers="keys", tablefmt="fancy_grid"))

if __name__ == "__main__":
    main()
