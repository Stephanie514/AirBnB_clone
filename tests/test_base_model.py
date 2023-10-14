import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        del self.base_model

    def test_id_type(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_ids_differ(self):
        new_model = BaseModel()
        self.assertNotEqual(new_model.id, self.base_model.id)

    def test_created_at_type(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_type(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_updates_updated(self):
        old_updated = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(old_updated, self.base_model.updated_at)

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

    def test_instantiation_with_attributes(self):
        attributes = {
            'id': 'test_id',
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            'name': 'Test Name'
        }
        base_model = BaseModel(**attributes)
        self.assertEqual(base_model.id, 'test_id')
        self.assertEqual(base_model.name, 'Test Name')
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

if __name__ == '__main__':
    unittest.main()
