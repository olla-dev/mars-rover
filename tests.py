import unittest

from main import Plateau, Rover

plateau = Plateau(5, 5)

class TestRover(unittest.TestCase):
    def test_rover1(self):
        rover = Rover(1, 2, 'N', plateau.m, plateau.n)
        rover.command_sequence = 'L M L M L M L M M'.split(" ")
        rover.exec_command_sequence()
        self.assertEqual(rover.x, 1)
        self.assertEqual(rover.y, 3)
        self.assertEqual(rover.heading, 'N')
    def test_rover2(self):
        rover = Rover(3, 3, 'E', plateau.m, plateau.n)
        rover.command_sequence = 'M M R M M R M R R M'.split(" ")
        rover.exec_command_sequence()
        self.assertEqual(rover.x, 5)
        self.assertEqual(rover.y, 1)
        self.assertEqual(rover.heading, 'E')
if __name__ == '__main__':
    unittest.main()