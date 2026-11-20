import sqlite3
import pandas as pd


# STEP 1A
# Import SQL Library and Pandas
# sqlite3 and pandas are imported above.


# STEP 1B
# Connect to the database.
conn = sqlite3.connect("data.sqlite")


# STEP 2
# Select employee number and last name for all employees.
df_first_five = pd.read_sql(
    """
    SELECT employeeNumber, lastName
    FROM employees;
    """,
    conn,
)


# STEP 3
# Select the same columns in reverse order.
df_five_reverse = pd.read_sql(
    """
    SELECT lastName, employeeNumber
    FROM employees;
    """,
    conn,
)


# STEP 4
# Alias employeeNumber as ID.
df_alias = pd.read_sql(
    """
    SELECT lastName, employeeNumber AS ID
    FROM employees;
    """,
    conn,
)


# STEP 5
# Categorize executive job titles using CASE.
df_executive = pd.read_sql(
    """
    SELECT
        employeeNumber,
        lastName,
        jobTitle,
        CASE
            WHEN jobTitle = 'President'
                OR jobTitle = 'VP Sales'
                OR jobTitle = 'VP Marketing'
            THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees;
    """,
    conn,
)


# STEP 6
# Return the length of each employee's last name.
df_name_length = pd.read_sql(
    """
    SELECT LENGTH(lastName) AS name_length
    FROM employees;
    """,
    conn,
)


# STEP 7
# Return the first two characters of each employee's job title.
df_short_title = pd.read_sql(
    """
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees;
    """,
    conn,
)


# STEP 8
# Calculate the sum of each rounded order total.
sum_total_price = pd.read_sql(
    """
    SELECT SUM(ROUND(priceEach * quantityOrdered)) AS total_price
    FROM orderDetails;
    """,
    conn,
)["total_price"]


# STEP 9
# Break each order date into day, month, and year columns.
df_day_month_year = pd.read_sql(
    """
    SELECT
        orderDate,
        STRFTIME('%d', orderDate) AS day,
        STRFTIME('%m', orderDate) AS month,
        STRFTIME('%Y', orderDate) AS year
    FROM orders;
    """,
    conn,
)


# Close the database connection after all queries have completed.
conn.close()