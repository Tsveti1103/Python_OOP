class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class WorkerTests(TestCase):
    def test_worker_is_initialized_correct(self):
        worker = Worker('Test', 100, 10)
        self.assertEqual('Test', worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy)
        self.assertEqual(0, worker.money)

    def test_rest(self):
        worker = Worker('Test', 100, 10)
        self.assertEqual(10, worker.energy)
        worker.rest()
        self.assertEqual(11, worker.energy)

    def test_worker_tries_to_work_with_negative_energy_error_raised(self):
        worker = Worker('Test', 100, -1)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_tries_to_work_with_energy_equal_to_zero_error_raised(self):
        worker = Worker('Test', 100, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_money_is_increased_after_work(self):
        worker = Worker('Test', 100, 10)
        worker.work()
        self.assertEqual(100, worker.money)
        worker.work()
        self.assertEqual(200, worker.money)

    def test_energy_is_decreased_after_work(self):
        worker = Worker('Test', 100, 10)
        worker.work()
        self.assertEqual(worker.energy, 9)
        worker.work()
        self.assertEqual(worker.energy, 8)

    def test_get_info(self):
        worker = Worker('Test', 100, 10)
        self.assertEqual("Test has saved 0 money.", worker.get_info())
        worker.work()
        self.assertEqual("Test has saved 100 money.", worker.get_info())


if __name__ == '__main__':
    main()
