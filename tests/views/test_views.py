from unittest import TestCase
from app import app


class TestHome(TestCase):

    ## Home Test

    def test_home(self):
        with app.test_client() as c:
            resp = c.get('/')
            self.assertEqual(resp.status_code, 200)

    # Login page loads correctly

    def test_login_page_loads(self):
        with app.test_client() as c:
            response = c.get('/login', content_type='html/text')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(b'Please Log in' in response.data)

    # Signup page loads correctly

    def test_signup_page_loads(self):
        with app.test_client() as c:
            response = c.get('/signup', content_type='html/text')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(b'Sign Up' in response.data)

    # Manage DB page loads correctly

    def test_manage_db_page_loads(self):
        with app.test_client() as c:
            response = c.get('/manage_db', content_type='html/text')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(b'Add Template:' in response.data)

    # Ensure that title & default user shows on main page

    def test_title_shows_up(self):
        with app.test_client() as c:
            response = c.get('/')
            self.assertTrue(b'Machine Learning Question' in response.data)
            self.assertEqual(response.status_code, 200)

    # Ensure that dataset size shows on main page

    def test_dataset_size_shows_up(self):
        with app.test_client() as c:
            response = c.get('/')
            self.assertTrue(b'1599' in response.data)
            self.assertEqual(response.status_code, 200)

    # Ensure that classifier build page loads correctly

    def test_classifier_build_page_loads(self):
        with app.test_client() as c:
            response = c.get('/classifier_build')
            self.assertTrue(b'59%' in response.data)
            self.assertEqual(response.status_code, 200)

    # Ensure that classifier fit page loads correctly

    def test_classifier_fit_page_loads(self):
        with app.test_client() as c:
            response = c.get('/classifier_fit')
            self.assertTrue(b'69%' in response.data)
            self.assertEqual(response.status_code, 200)

    # Ensure that sommeliers page loads correctly

    def test_sommeliers_page_loads(self):
        with app.test_client() as c:
            response = c.get('/sommeliers')
            self.assertTrue(b'*(3-4 is poor quality, 5-6 average, 7-8 is the highest)' in response.data)
            self.assertEqual(response.status_code, 200)

    # Ensure that manage db page loads correctly

    def test_manage_db_page_loads(self):
        with app.test_client() as c:
            response = c.get('/manage_db')
            self.assertTrue(b'Add Template:' in response.data)
            self.assertEqual(response.status_code, 200)
