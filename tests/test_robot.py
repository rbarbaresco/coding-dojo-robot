# -*- coding: utf-8 -*-
import unittest

import robot
from unittest.mock import MagicMock


class RobotTest(unittest.TestCase):

    def setUp(self):
        self.robot = robot.Robot(MagicMock())

    def test_deveria_receber_uma_lista_de_comandos(self):
        self.robot.execute("SEi pa")

    def test_deveria_receber_uma_lista_de_comandos_quando_tiver_dois(self):
        self.robot.execute("SEi pa", "Outro comando")

    def test_deveria_retornar_not_placed_yet_quando_nao_tiver_sido_colocado(self):
        self.assertEqual("I'm not placed yet", self.robot.execute("SEi pa", "Outro comando"))

    def test_deveria_retornar_0_0_NORTH(self):
        self.assertEqual("0 0 NORTH", self.robot.execute("PLACE 0 0 NORTH"))

    def test_deveria_retornar_0_1_NORTH(self):
        self.assertEqual("0 1 NORTH", self.robot.execute("PLACE 0 0 NORTH", "MOVE"))

    def test_deveria_retornar_0_0_WEST(self):
        self.assertEqual("0 0 WEST", self.robot.execute("PLACE 0 0 NORTH", "LEFT"))

    def test_deveria_retornar_0_0_EAST(self):
        self.assertEqual("0 0 EAST", self.robot.execute("PLACE 0 0 NORTH", "RIGHT"))

    def test_deveria_retornar_0_0_NORTH_(self):
        self.assertEqual("0 0 NORTH", self.robot.execute("PLACE 0 0 WEST", "RIGHT"))

    def test_deveria_retornar_0_0_SOUTH(self):
        self.assertEqual("0 0 SOUTH", self.robot.execute("PLACE 0 0 EAST", "RIGHT"))

    def test_deveria_retornar_0_0_SOUTH_passando_LEFT(self):
        self.assertEqual("0 0 SOUTH", self.robot.execute("PLACE 0 0 WEST", "LEFT"))

    def test_deveria_retornar_0_0_EAST_passando_LEFT(self):
        self.assertEqual("0 0 EAST", self.robot.execute("PLACE 0 0 SOUTH", "LEFT"))

    def test_deveria_retornar_0_0_NORTH_passando_LEFT(self):
        self.assertEqual("0 0 NORTH", self.robot.execute("PLACE 0 0 EAST", "LEFT"))

    def test_deveria_retornar_0_0_NORTH_com_place_no_meio(self):
        self.assertEqual("0 0 NORTH", self.robot.execute("PLACE 0 0 NORTH", "MOVE", "PLACE 0 0 NORTH"))

    def test_deveria_retornar_0_0_NORTH_comecando_de_0_1_SOUTH(self):
        self.assertEqual("0 0 SOUTH", self.robot.execute("PLACE 0 1 SOUTH", "MOVE"))

    def test_deveria_retornar_1_0_EAST_comecando_de_0_0_EAST(self):
        self.assertEqual("1 0 EAST", self.robot.execute("PLACE 0 0 EAST", "MOVE"))

    def test_deveria_retornar_1_0_WEST_comecando_de_2_0_WEST(self):
        self.assertEqual("1 0 WEST", self.robot.execute("PLACE 2 0 WEST", "MOVE"))

    def test_deveria_retornar_0_1_NORTH_com_place_no_meio_e_move(self):
        self.assertEqual("0 1 NORTH", self.robot.execute("PLACE 0 0 NORTH", "MOVE", "PLACE 0 0 NORTH", "MOVE"))

    def test_deveria_retornar_0_3_NORTH_com_3_moves(self):
        self.assertEqual("0 3 NORTH", self.robot.execute("PLACE 0 0 NORTH", "MOVE", "MOVE", "MOVE"))

    def test_deveria_retornar_0_3_EAST_com_3_moves_e_1_right(self):
        self.assertEqual("0 3 EAST", self.robot.execute("PLACE 0 0 NORTH", "MOVE", "MOVE", "MOVE", "RIGHT"))

    def test_deveria_retornar_2_1_SOUTH_com_2_moves_e_1_right_move_right(self):
        self.assertEqual("1 2 SOUTH", self.robot.execute("PLACE 0 0 NORTH", "MOVE", "MOVE", "RIGHT", "MOVE", "RIGHT"))

    def test_deveria_retornar_2_2_SOUTH_com_2_moves_e_1_right_move_move_right(self):
        self.assertEqual("2 2 SOUTH", self.robot.execute("PLACE 0 0 NORTH", "MOVE", "MOVE", "RIGHT", "MOVE", "MOVE", "RIGHT"))

    def test_deveria_retornar_0_0_WEST_depois_de_alguns_comandos(self):
        self.assertEqual("0 0 WEST", self.robot.execute("PLACE 0 2 EAST", "RIGHT", "MOVE", "MOVE", "RIGHT"))

    def test_deveria_continuar_em_0_0_WEST(self):
        self.assertEqual("0 0 WEST", self.robot.execute("PLACE 0 0 WEST", "MOVE"))

    def test_deveria_continuar_em_4_4_EAST(self):
        self.assertEqual("4 4 EAST", self.robot.execute("PLACE 4 4 EAST", "MOVE"))

    # def test_PLACE_nao_aceitando_negativo(self):
    #     saldjlaksdj

