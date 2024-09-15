import unittest
from unittest.mock import patch, MagicMock

from project import driver_standings, race_result, get_year_input, get_round_input

class TestF1Functions(unittest.TestCase):

    @patch('requests.get')
    def test_driver_standings(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "MRData": {
                "StandingsTable": {
                    "StandingsLists": [{
                        "DriverStandings": [
                            {
                                "position": "1",
                                "Driver": {
                                    "givenName": "Lewis",
                                    "familyName": "Hamilton"
                                },
                                "points": "300"
                            },
                            {
                                "position": "2",
                                "Driver": {
                                    "givenName": "Max",
                                    "familyName": "Verstappen"
                                },
                                "points": "280"
                            }
                        ]
                    }]
                }
            }
        }
        mock_get.return_value = mock_response

        result = driver_standings(2024)
        expected = [
            {"Position": "1", "Driver Name": "Lewis Hamilton", "Total Points": "300"},
            {"Position": "2", "Driver Name": "Max Verstappen", "Total Points": "280"}
        ]
        self.assertEqual(result, expected)

    @patch('requests.get')
    def test_race_result(self, mock_get):
        # Sample response data
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "MRData": {
                "RaceTable": {
                    "Races": [
                        {
                            "raceName": "Australian Grand Prix",
                            "Results": [
                                {
                                    "position": "1",
                                    "Driver": {
                                        "givenName": "Charles",
                                        "familyName": "Leclerc"
                                    },
                                    "points": "25"
                                },
                                {
                                    "position": "2",
                                    "Driver": {
                                        "givenName": "Sergio",
                                        "familyName": "Perez"
                                    },
                                    "points": "18"
                                }
                            ]
                        }
                    ]
                }
            }
        }
        mock_get.return_value = mock_response

        result, circuit_name = race_result(2024, 1)
        expected_result = [
            {"Position": "1", "Driver Name": "Charles Leclerc", "Points": "25"},
            {"Position": "2", "Driver Name": "Sergio Perez", "Points": "18"}
        ]
        self.assertEqual(result, expected_result)
        self.assertEqual(circuit_name, "Australian Grand Prix")

    def test_get_year_input_valid(self):
        with patch('builtins.input', return_value='2024'):
            result = get_year_input("Enter the F1 season year (yyyy): ")
            self.assertEqual(result, 2024)

    def test_get_year_input_invalid(self):
        with patch('builtins.input', side_effect=['abcd', '2024']):
            result = get_year_input("Enter the F1 season year (yyyy): ")
            self.assertEqual(result, 2024)

    def test_get_round_input_valid(self):
        with patch('builtins.input', return_value='1'):
            result = get_round_input("Enter the round: ")
            self.assertEqual(result, 1)

    def test_get_round_input_invalid(self):
        with patch('builtins.input', side_effect=['-1', '1']):
            result = get_round_input("Enter the round: ")
            self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
