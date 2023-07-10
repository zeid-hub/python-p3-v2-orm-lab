from __init__ import CURSOR, CONN
from department import Department
from employee import Employee


class Review:

    def __init__(self, year, summary, employee, id=None):
        self.id = id
        self.year = year
        self.summary = summary
        self.employee = employee

    def __repr__(self):
        return (
            f"<Review {self.id}: {self.year}, {self.summary}, "
            + f"Employee: {self.employee.name} >"
        )

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY,
            year INT,
            summary TEXT,
            employee_id INTEGER,
            FOREIGN KEY (employee_id) REFERENCES employee(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Review class instances """
        sql = """
            DROP TABLE IF EXISTS reviews;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        pass

    def update(self):
        pass

    @classmethod
    def create(cls, year, summary, employee):
        pass

    def delete(self):
        pass

    @classmethod
    def new_from_db(cls, row):
        pass

    @classmethod
    def get_all(cls):
        pass

    @classmethod
    def find_by_id(cls, id):
        pass
