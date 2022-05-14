from project.pet_shop import PetShop
from unittest import TestCase, main


class TestPetShop(TestCase):
    def test_init(self):
        pet = PetShop('Mini')
        self.assertEqual('Mini', pet.name)
        self.assertEqual({}, pet.food)
        self.assertEqual([], pet.pets)

    def test_add_food(self):
        pet = PetShop('Mini')
        with self.assertRaises(ValueError) as ex:
            pet.add_food('Brid', 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))
        with self.assertRaises(ValueError) as ex:
            pet.add_food('Brid', -1)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))
        pet.add_food('Brid', 20)
        self.assertEqual({'Brid': 20}, pet.food)
        result = pet.add_food('Brid', 30)
        self.assertEqual({'Brid': 50}, pet.food)
        self.assertEqual(f"Successfully added 30.00 grams of Brid.", result)

    def test_add_pet(self):
        pet = PetShop('Mini')
        res = pet.add_pet('Ruby')
        self.assertEqual(['Ruby'], pet.pets)
        self.assertEqual(f"Successfully added Ruby.", res)
        with self.assertRaises(Exception) as ex:
            pet.add_pet('Ruby')
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_feed_pet(self):
        pet = PetShop('Mini')
        with self.assertRaises(Exception) as ex:
            pet.feed_pet('Brid', 'Ares')
        self.assertEqual("Please insert a valid pet name", str(ex.exception))
        pet.add_pet('Ares')
        res = pet.feed_pet('Brid', 'Ares')
        self.assertEqual("You do not have Brid", res)
        pet.add_food('Brid', 50)
        res = pet.feed_pet('Brid', 'Ares')
        self.assertEqual("Adding food...", res)
        self.assertEqual(1050.00, pet.food['Brid'])
        pet.add_food('As', 150)
        res = pet.feed_pet('As', 'Ares')
        self.assertEqual("Ares was successfully fed", res)
        self.assertEqual(50., pet.food['As'])

    def test_repr(self):
        pet = PetShop('Mini')
        pet.add_pet('Ruby')
        pet.add_pet('Ares')
        pet.add_pet('Charly')
        self.assertEqual(f'Shop Mini:\nPets: Ruby, Ares, Charly', pet.__repr__())


if __name__ == '__main__':
    main()
