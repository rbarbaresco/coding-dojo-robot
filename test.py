import unittest
import robot


class RobotTest(unittest.TestCase):

    def test_deveria_receber_uma_lista_de_comandos(self):
        robot.execute("SEi pa")

    def test_deveria_receber_uma_lista_de_comandos_quando_tiver_dois(self):
        robot.execute("SEi pa", "Outro comando")

    def test_deveria_retornar_not_placed_yet_quando_nao_tiver_sido_colocado(self):
        self.assertEqual("I'm not placed yet", robot.execute("SEi pa", "Outro comando"))

    def test_deveria_retornar_0_0_NORTH(self):
        self.assertEqual("0 0 NORTH", robot.execute("PLACE 0 0 NORTH"))

    def test_deveria_retornar_0_1_NORTH(self):
        self.assertEqual("0 1 NORTH", robot.execute("PLACE 0 0 NORTH", "MOVE"))

    def test_deveria_retornar_0_0_WEST(self):
        self.assertEqual("0 0 WEST", robot.execute("PLACE 0 0 NORTH", "LEFT"))

    def test_deveria_retornar_0_0_EAST(self):
        self.assertEqual("0 0 EAST", robot.execute("PLACE 0 0 NORTH", "RIGHT"))

    def test_deveria_retornar_0_0_NORTH_(self):
        self.assertEqual("0 0 NORTH", robot.execute("PLACE 0 0 WEST", "RIGHT"))

    def test_deveria_retornar_0_0_SOUTH(self):
        self.assertEqual("0 0 SOUTH", robot.execute("PLACE 0 0 EAST", "RIGHT"))

    def test_deveria_retornar_0_0_SOUTH_passando_LEFT(self):
        self.assertEqual("0 0 SOUTH", robot.execute("PLACE 0 0 WEST", "LEFT"))

    def test_deveria_retornar_0_0_EAST_passando_LEFT(self):
        self.assertEqual("0 0 EAST", robot.execute("PLACE 0 0 SOUTH", "LEFT"))

    def test_deveria_retornar_0_0_NORTH_passando_LEFT(self):
        self.assertEqual("0 0 NORTH", robot.execute("PLACE 0 0 EAST", "LEFT"))

    def test_deveria_retornar_0_0_NORTH_com_place_no_meio(self):
        self.assertEqual("0 0 NORTH", robot.execute("PLACE 0 0 NORTH", "MOVE", "PLACE 0 0 NORTH"))

    def test_deveria_retornar_0_0_NORTH_comecando_de_0_1_SOUTH(self):
        self.assertEqual("0 0 SOUTH", robot.execute("PLACE 0 1 SOUTH", "MOVE"))

    def test_deveria_retornar_1_0_EAST_comecando_de_0_0_EAST(self):
        self.assertEqual("1 0 EAST", robot.execute("PLACE 0 0 EAST", "MOVE"))

    def test_deveria_retornar_1_0_WEST_comecando_de_2_0_WEST(self):
        self.assertEqual("1 0 WEST", robot.execute("PLACE 2 0 WEST", "MOVE"))

    def test_deveria_retornar_0_1_NORTH_com_place_no_meio_e_move(self):
        self.assertEqual("0 1 NORTH", robot.execute("PLACE 0 0 NORTH", "MOVE", "PLACE 0 0 NORTH", "MOVE"))

    def test_PLACE_nao_aceitando_negativo(self):
        saldjlaksdj
