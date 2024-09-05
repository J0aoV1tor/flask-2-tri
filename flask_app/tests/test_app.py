import unittest
from app import create_app, db

class UserModelCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()

    def test_user_creation(self):
        from app.models import User
        user = User(name='Test User', email='test@example.com', password='password')
        db.session.add(user)
        db.session.commit()
        self.assertEqual(User.query.count(), 1)
