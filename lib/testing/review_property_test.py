from employee import Employee
from department import Department
from review import Review
import pytest


class TestReviewProperties:
    '''Class Review in review.py'''

    @pytest.fixture(autouse=True)
    def reset_db(self):
        '''drop and recreate tables prior to each test.'''
        Review.drop_table()
        Employee.drop_table()
        Department.drop_table()
        Department.create_table()
        Employee.create_table()
        Review.create_table()

    def test_review_valid(self):
        '''validates name, job title, department id are valid'''
        # should not raise exception
        employee = Employee.create("Lee", "Manager", Department.create(
            "Payroll", "Building A, 5th Floor"))
        review = Review.create(
            2023, "Excellent work ethic! Outstanding programming skills!", employee)

    def test_year_is_int(self):
        '''validates year property is assigned int'''
        with pytest.raises(ValueError):
            employee = Employee.create("Lee", "Manager", Department.create(
                "Payroll", "Building A, 5th Floor"))
            review = Review.create(
                "this century", "Excellent work ethic! Outstanding programming skills!", employee)

    def test_year_value(self):
        '''validates year property length >= 2000'''
        with pytest.raises(ValueError):
            employee = Employee.create("Lee", "Manager", Department.create(
                "Payroll", "Building A, 5th Floor"))
            review = Review.create(
                1999, "Excellent work ethic! Outstanding programming skills!", employee)

    def test_summary_string_length(self):
        '''validates summary property length > 0'''
        with pytest.raises(ValueError):
            employee = Employee.create("Lee", "Manager", Department.create(
                "Payroll", "Building A, 5th Floor"))
            review = Review.create(2023, "", employee)

    def test_employee_property_type_assignment(self):
        with pytest.raises(ValueError):
            employee = Employee.create("Lee", "Manager", Department.create(
                "Payroll", "Building A, 5th Floor"))
            review = Review.create(
                2023, "Excellent work ethic! Outstanding programming skills!", employee)
            review.employee = 7  # Must be Employee object

    def test_employee_fk_property_assignment(self):
        with pytest.raises(ValueError):
            department = Department.create("Payroll", "Building A, 5th Floor")
            employee = Employee.create("Lee", "Manager", department)
            review = Review.create(
                2023, "Excellent work ethic! Outstanding programming skills!", employee)
            review.employee = Employee("Kai", "Web Developer", Department(
                "HR", "Building C"))  # Department not in db
