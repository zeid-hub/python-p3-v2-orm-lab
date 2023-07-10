# ORM Lab

## Learning Goals

- Map a Python class to a database table.
- Persist a one-to-many relationship.
- Define property methods to manage attributes.

---

## Instructions

This is a **test-driven lab**. Run `pipenv install` to create your virtual
environment and `pipenv shell` to enter the virtual environment. Then run
`pytest -x` to run your tests. Use these instructions and `pytest`'s error
messages to complete your work in the `lib/` folder.

![orm lab erd](https://curriculum-content.s3.amazonaws.com/6676/python-p3-v2-orm/orm_lab_erd.png)

This lab involves enhancing the company data model from the ORM lessons. You
will implement a class named `Review` that encapsulates a annual performance
review for an employee. There is a one-to-many relationship between `Employee`
and `Review`.

- An employee may have many reviews.
- A review is for one employee.
- A review includes an attribute for the `year` as well as a `summary` of the
  employee's performance.

The `Department` and `Employee` classes contain the completed solutions from the
ORM lessons. You will add functionality for the new `Review` class in this lab.

### **Environment**

Our environment is going to be generated in `lib/__init__.py` (rather than
`lib/config.py`) using a series of imports and instantiations. Here we will
generate a `sqlite3.Connection` object, `CONN`, and a `sqlite3.Cursor` object,
`CURSOR` to be used throughout the lab.

### Implementing `Review`

The `Review` class contains the following methods already implemented for you:

- `__init__` initializes attributes for the review `year`, `summary`, and
  associated `employee`. It also initializes the `id` attribute to a default
  value of `None`.
- `__repr__` returns a formatted string containing the attribute values.
- `create_table` creates a "reviews" database table.
- `drop_table` drops the "reviews" database table.

Edit the `Review` class to add the following ORM methods (you will add property
methods in a subsequent step):

### `save()`

Create an instance method `save()` that saves a `Review` object to your
database. Keep in mind the `employee` attribute references an `Employee` object,
while the database table foreign key column stores the employee id as an
integer.

### `create()`

This is a class method that should:

- Create a new `Review` class instance using the parameter values.
- Save the new `Review` class instance to the "reviews" table.
- Return the new `Review` class instance.

Think about how you can re-use the `save()` method to help with this one.

### `update()`

This instance method should update the `year`, `summary` and `employee_id`
columns for a "reviews" table row based on the `id` of the current object.

### `delete()`

This instance method should delete a "reviews" table row based on the `id` of
the current object.

### `new_from_db()`

This class method should initialize a new instance of `Review` using values from
a "review" table row passed as a list into the method. Since the table row
stores the employee id as an integer, you need to use the `find_by_id` method to
get an instance of `Employee` to associate with the new `Review` class instance
that you create. Make sure you also set the `id` of the new `Review` instance.
Finally, the method should return the newly created `Review` instance.

### `get_all()`

This class method should return a list of `Review` instances for every record in
the "reviews" table.

### `find_by_id()`

This class method takes in an `id` as a parameter, and should return a single
`Review` class instance for the corresponding row in the "reviews" table with
that same id, or `None` is no such row exists in the table.

You can test your methods by running the tests in the
"lib/testing/review_orm_test.py" file:

```bash
pytest lib/testing/review_orm_test.py
```

You can also experiment using the `lib/debug.py` file:

```bash
ipdb> Review.get_all()
[<Review 1: 2023, Efficient worker, Employee: Lee >, <Review 2: 2022, Good work ethic, Employee: Lee >, <Review 3: 2023, Excellent communication skills, Employee: Sasha >]
ipdb>
```

### `Review` Properties

Let's add property methods to set rules for the `Review` attributes as follows:

- `year` should be an integer that is greater or equal to 2000.
- `summary` should be a non-empty string.
- `employee` should reference an `Employee` class instance that has been
  persisted into the "employees" table.

You can test your methods by running the tests in the
"lib/testing/review_property_test.py" file:

```bash
pytest lib/testing/review_property_test.py
```

### Update `Employee` to get a list of associated `Review` instances

Update the `Employee` class with a new method `reviews()` ßfor getting
associated `Review` instances that have been persisted to the database.

### `reviews()`

This instance method should query the "reviews" table to get all rows where the
foreign key column matches the id of the current `Employee` class instance. The
method should return a list of `Review` objects for each matching table row.

NOTE: To avoid issues with circular imports, embed import the `Review` class
within the `reviews()` method rather than at the module level.

You can test your methods by running the tests in the
"lib/testing/employee_orm_test.py" file:

```bash
pytest lib/testing/employee_orm_test.py
```

### Submit your completed lab

Check to make sure all tests pass:

```bash
pytest -x
```

Once all of your tests are passing, commit and push your work using `git` to
submit.

---
