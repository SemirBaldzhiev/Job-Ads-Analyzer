import unittest
from src.user.user import User

class TestUserClass(unittest.TestCase):

    def setUp(self):
        '''
        Set up any initial conditions or mock objects needed for tests
        '''
        self.test_user = User("John", "Doe", "johndoe", "john@example.com", "password123", "Python,SQL")
        self.test_user.save()

    def test_valid_credentials(self):
        '''
        Test valid login credentials
        '''
        self.assertTrue(User.valid_credentials("johndoe", "password123"))

    def test_invalid_credentials(self):
        '''
        Test invalid login credentials
        '''
        self.assertFalse(User.valid_credentials("johndoe", "wrongpassword"))

    def test_change_password_success(self):
        '''
        Test changing password with correct old password
        '''
        old_password = "password123"
        new_password = "newpassword456"
        self.assertTrue(self.test_user.change_password(old_password, new_password))

    def test_change_password_failure(self):
        '''
        Test changing password with incorrect old password
        '''
        old_password = "wrongpassword"
        new_password = "newpassword456"
        self.assertFalse(self.test_user.change_password(old_password, new_password))

if __name__ == '__main__':
    unittest.main()
