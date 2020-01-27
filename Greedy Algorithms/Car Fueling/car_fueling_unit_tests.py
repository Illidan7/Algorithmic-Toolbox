import unittest
from car_fueling import compute_min_number_of_refills


class CarFueling(unittest.TestCase):
    def test(self):
        for (d, m, n, stops, answer) in [
            (950, 400, 4, [200, 375, 550, 750], 2),
            (10, 3, 4, [1, 2, 5, 9], -1),
            (200, 250, 2, [100, 150], 0),
            (20, 25, 2, [10, 15], 0)
        ]:
            self.assertEqual(compute_min_number_of_refills(d, m, stops), answer)


if __name__ == '__main__':
    unittest.main()
