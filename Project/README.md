# Formula 1 Data Analysis

#### Video Demo : [Formula 1 Data Analysis](https://www.youtube.com/watch?v=c8ICJ21_vXQ)

**F1 Data Analysis** is a command-line tool designed to provide insights into Formula 1 racing through data retrieval and analysis using **Ergast API** and **fastf1 library**. It offers functionalities to view driver standings and race results for a specified season and round,and also visualization of data such as Position changes during a race. allowing users to easily access and interpret F1 data.

## Features

- **Driver Standings**: Retrieve and display the standings of drivers for a specific F1 season, including their positions, names, and total points.
- **Race Results**: Fetch and display the results of a specific race, including driver positions, names, and points, along with the circuit name.
- **Visualization of Data**: Fetch and display the results and position changes during a specific race.
- **Interactive CLI**: User-friendly command-line interface that guides users through selecting functions and entering necessary parameters.
- **Error Handling**: The project includes basic error handling for invalid user inputs and API response errors.

## Requirements

- Python 3.6 or higher
- All the libraries mentioned in the [requirements.txt](https://github.com/Vageesha-S-R/CS50P/blob/main/Project/requirements.txt)
- [project.py](https://github.com/Vageesha-S-R/CS50P/blob/main/Project/project.py) Contains the main functionality of the program, inculding functions for fetching and displaying the data
- [test_project.py](https://github.com/Vageesha-S-R/CS50P/blob/main/Project/test_project.py) Contains `pytest` tests for the functions in `project.py` , uses `unittest` testing framework


## Installation

1. **Install the required libraries:**

    ```bash
    pip install requests
    ```

## Usage

Run the script to start the application:

```bash
python project.py
