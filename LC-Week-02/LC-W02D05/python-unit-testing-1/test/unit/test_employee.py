from unittest import TestCase, expectedFailure
from src.employee import Employee

class TestEmployee(TestCase):
    @classmethod
    def setUpClass(cls):
        print("In setUpClass()...")
        cls.default_company = "General Assembly"
        cls.test_company = "The company of the Basil"

    @classmethod
    def tearDownClass(cls):
        print("In tearDownClass()...")

    def setUp(self):
        print("setUp has run")
        self.emp_1 = Employee("qusai", "othman")
        self.emp_2 = Employee("saeed", "jabeeti", self.test_company)

    def tearDown(self):
        print("Tear down has finished cleaning up")

    @expectedFailure
    def test_email(self):
        print("email")
        self.assertEqual(self.emp_1.email, "qusai.othman@email.com")

    def test_fullname(self):
        print("fullname")
        self.assertEqual(self.emp_1.fullname, "Qusai Othman")

    def test_default_company(self):
        print("default company")
        self.assertEqual(self.emp_1.company, "General Assembly")

    def test_custom_company(self):
        print("custom company")
        self.assertEqual(self.emp_2.company, self.test_company)

    
