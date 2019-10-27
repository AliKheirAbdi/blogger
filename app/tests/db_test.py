import unittest
from app import db
from app.models import User, Post

class DbUserPost(unittest.TestCase):
    '''
        Test Class to test db
      '''

    def setUp(self):
        '''
         Set up method runs pre test
        '''
        self.test_user = User(username="demo", email="demo@demo.com", password='testing' )
        db.session.add(self.test_user)
        db.session.commit()

    def tearDown(self):
        self.user = User.query.filter_by(username= "ali").first()
        db.session.remove(self.user)
        db.session.commit()

    def test_save_user_to_db(self):
        user = User.query.filter_by(username='ali').first()
        self.assertEqual('ali', user.username)



if __name__ == "__main__":
    unittest.main()