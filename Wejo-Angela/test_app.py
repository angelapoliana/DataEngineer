import unittest
from unittest.mock import Mock

import csvparser


class TestMethods(unittest.TestCase):
    
    def test_read_row(self):
        with open('./data/vehicle_events.csv') as file:
            atual = csvparser.read_row(file)
            
           
        assert_value = ['VehicleD', 'Driver Side Window', 'Down']
        self.assertEqual(atual, assert_value)
        
    def test_parse_row(self):
        row = csvparser.parse_row('"VehicleD","Driver Side Window","Down"')
        atual = f'{row[0]} - {row[1]} - {row[2]}'
        assert_value = "VehicleD - Driver Side Window - Down"
        self.assertEqual(atual, assert_value)
        
if __name__ == "__main__":
    unittest.main()
