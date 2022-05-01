from unittest import TestCase, main

from test.project import Hero


class TestHero(TestCase):
    def test_initialisation(self):
        player = Hero('Az', 20, 100.0, 50.0)
        self.assertEqual('Az', player.username)
        self.assertEqual(20, player.level)
        self.assertEqual(100.0, player.health)
        self.assertEqual(50.0, player.damage)

    def test_battle_raises_same_player_error(self):
        player = Hero('Az', 20, 100.0, 50.0)
        player_2 = Hero('Az', 20, 100.0, 50.0)
        with self.assertRaises(Exception) as ex:
            player.battle(player_2)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_raises_player_low_health_error(self):
        player = Hero('Az', 20, 0.0, 50.0)
        enemy_player = Hero('Someone', 20, 20.0, 50.0)
        with self.assertRaises(Exception) as ex:
            player.battle(enemy_player)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_raises_enemy_low_health_error(self):
        player = Hero('Az', 20, 100.0, 50.0)
        enemy_player = Hero('Someone', 20, 0.0, 50.0)

        with self.assertRaises(Exception) as ex:
            player.battle(enemy_player)
        self.assertEqual(f"You cannot fight {enemy_player.username}. He needs to rest", str(ex.exception))

    def test_battle_correct_data_win(self):
        player = Hero('Az', 1, 100.0, 50.0)
        enemy_player = Hero('Someone', 1, 50.0, 50.0)
        result = player.battle(enemy_player)
        self.assertEqual(55.0, player.health)
        self.assertEqual(2, player.level)
        self.assertEqual(55.0, player.damage)
        self.assertEqual(0.0, enemy_player.health)
        self.assertEqual(1, enemy_player.level)
        self.assertEqual(50.0, enemy_player.damage)
        self.assertEqual("You win", result)

    def test_battle_correct_data_draw(self):
        player = Hero('Az', 1, 50.0, 50.0)
        enemy_player = Hero('Someone', 1, 50.0, 50.0)
        result = player.battle(enemy_player)
        self.assertEqual(0.0, player.health)
        self.assertEqual(1, player.level)
        self.assertEqual(50.0, player.damage)
        self.assertEqual(0.0, enemy_player.health)
        self.assertEqual(1, enemy_player.level)
        self.assertEqual(50.0, enemy_player.damage)
        self.assertEqual("Draw", result)

    def test_battle_correct_data_lose(self):
        player = Hero('Az', 1, 50.0, 50.0)
        enemy_player = Hero('Someone', 1, 100.0, 50.0)
        result = player.battle(enemy_player)
        self.assertEqual(0.0, player.health)
        self.assertEqual(1, player.level)
        self.assertEqual(50, player.damage)
        self.assertEqual(55.0, enemy_player.health)
        self.assertEqual(2, enemy_player.level)
        self.assertEqual(55.0, enemy_player.damage)
        self.assertEqual("You lose", result)

    def test_str(self):
        player = Hero('Az', 1, 50.0, 50.0)
        result = str(player)
        self.assertEqual(f"Hero Az: 1 lvl\nHealth: 50.0\nDamage: 50.0\n", result)


if __name__ == '__main__':
    main()
