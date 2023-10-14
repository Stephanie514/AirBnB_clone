import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModelAttributes(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        del self.base_model

    def test_id_type(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_ids_differ(self):
        new_model = BaseModel()
        self.assertNotEqual(new_model.id, self.base_model.id)

    def test_name_attribute(self):
        self.base_model.name = "John Doe"
        self.assertEqual(self.base_model.name, "John Doe")

class TestBaseModelDates(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        del self.base_model

    def test_created_updated_equal(self):
        self.assertEqual(self.base_model.created_at.year, self.base_model.updated_at.year)

    def test_save_updates_updated(self):
        old_updated = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated, self.base_model.updated_at)

class TestBaseModelRepresentation(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        del self.base_model

    def test_str_representation(self):
        expected_str = f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_str)

    def test_to_dict_type(self):
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)

    def test_to_dict_has_class_key(self):
        obj_dict = self.base_model.to_dict()
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

    def test_to_dict_date_types(self):
        obj_dict = self.base_model.to_dict()
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)

class TestBaseModelInstantiation(unittest.TestCase):
    def setUp(self):
        base_model_dict = {
            'id': 'test_id',
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
        }
        self.base_model = BaseModel(**base_model_dict)

    def tearDown(self):
        del self.base_model

    def test_id(self):
        self.assertEqual(self.base_model.id, 'test_id')

    def test_created_at_type(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_type(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

if __name__ == '__main__':
    unittest.main()
