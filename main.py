import csv
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# ---TASK 1---
years = []
schools = []

with open('1.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Пропускаємо перший рядок (заголовок)
    for row in reader:
        year, school = map(int, row)
        years.append(year)
        schools.append(school)

# Прогноз на наступні 10 років
future_years = np.arange(2025, 2035).reshape(-1, 1)
model = LinearRegression()
model.fit(np.array(years).reshape(-1, 1), schools)
future_schools = model.predict(future_years)

# Візуалізація прогнозу
plt.figure(figsize=(10, 6))
plt.plot(years, schools, marker='o', linestyle='-', label='Реальні дані')
plt.plot(future_years, future_schools, marker='x', linestyle='--', label='Прогноз')
plt.title('Прогноз зменшення кількості навчальних закладів')
plt.xlabel('Рік')
plt.ylabel('Кількість навчальних закладів')
years = np.concatenate((years, np.arange(2025, 2036)))
plt.xticks(years, rotation=45)  # Поділки для кожного року з поворотом на 45 градусів
plt.grid(True)
plt.legend()


# ---TASK 2---
salaries = []

with open('2.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Пропускаємо перший рядок (заголовок)
    for row in reader:
        salary = float(row[0])
        salaries.append(salary)

# Обчислення кількості співробітників у різних інтервалах зарплат
below_10k = np.sum(np.array(salaries) < 10000)
between_10k_15k = np.sum((np.array(salaries) >= 10000) & (np.array(salaries) <= 15000))
above_15k = np.sum(np.array(salaries) > 15000)

# Відображення результатів на графіку
labels = ['До 10 тис.', 'Від 10 до 15 тис.', 'Більше 15 тис.']
values = [below_10k, between_10k_15k, above_15k]
# Відображення гістограми
plt.figure(figsize=(10, 6))
plt.bar(labels, values, color='blue', alpha=0.7)
plt.title('Кількість співробітників за зарплатними інтервалами')
plt.xlabel('Зарплатний інтервал')
plt.ylabel('Кількість співробітників')
plt.grid(axis='y')


# ---TASK 3---
gas_types_read = []
prices_read = []
qualities_read = []

with open('3.csv', 'r') as file:
    next(file)  # Пропускаємо перший рядок (заголовок)
    for line in file:
        gas, price, quality = line.strip().split(',')
        gas_types_read.append(gas)
        prices_read.append(float(price))
        qualities_read.append(float(quality))

plt.figure(figsize=(10, 6))
plt.scatter(gas_types_read, prices_read, marker='o', label='Ціна (UAH)')
plt.scatter(gas_types_read, qualities_read, marker='s', label='Якість')
plt.title('Вартість та якість бензину різних сортів')
plt.xlabel('Сорт бензину')
plt.ylabel('Ціна (UAH) / Якість')
plt.grid(True)
plt.legend()


# ---TASK 4---
departments_read = []
new_staff_read = []
dismissed_staff_read = []

with open('4.csv', 'r') as file:
    next(file)  # Пропускаємо перший рядок (заголовок)
    for line in file:
        department, new, dismissed = line.strip().split(',')
        departments_read.append(department)
        new_staff_read.append(int(new))
        dismissed_staff_read.append(int(dismissed))

# Підрахунок різниці між новими та звільненими співробітниками
difference = np.array(new_staff_read) - np.array(dismissed_staff_read)

# Візуалізація графіка
plt.figure(figsize=(12, 6))
plt.bar(departments_read, difference, color='green', alpha=0.7)
plt.title('Різниця між новими та звільненими співробітниками')
plt.xlabel('Підрозділ')
plt.ylabel('Кількість співробітників')
plt.grid(axis='y')
plt.yticks(np.arange(min(difference), max(difference)+1, 1))



# ---TASK 5---
activities_read = []
hours_read = []

with open('5.csv', 'r') as file:
    next(file)  # Пропускаємо перший рядок (заголовок)
    for line in file:
        activity, hour = line.strip().split(',')
        activities_read.append(activity)
        hours_read.append(int(hour))

# Обчислення відсотків для кожної діяльності
total_hours = sum(hours_read)
percentages = [(hour / total_hours) * 100 for hour in hours_read]

# Візуалізація кругового графіка
plt.figure(figsize=(10, 8))
plt.pie(percentages, labels=activities_read, autopct='%1.1f%%', startangle=140, colors=['blue', 'green', 'red', 'purple', 'orange'])
plt.title('Розподіл робочого часу продавця')
plt.axis('equal')  # Забезпечення кругової форми


# ---TASK 6---
experience_years_read = []
bonus_size_read = []

with open('6.csv', 'r') as file:
    next(file)  # Пропускаємо перший рядок (заголовок)
    for line in file:
        exp, bonus = line.strip().split(',')
        experience_years_read.append(int(exp))
        bonus_size_read.append(int(bonus))

# Візуалізація графіка
plt.figure(figsize=(12, 6))
plt.scatter(experience_years_read, bonus_size_read, color='blue', marker='o')
plt.title('Залежність розміру надбавки до зарплати від трудового стажу')
plt.xlabel('Трудовий стаж, роки')
plt.ylabel('Розмір надбавки, грн')
plt.grid(True)
plt.xticks(experience_years_read)
plt.yticks(bonus_size_read)


# ---TASK 7---
employee_surnames = []
employee_ages = []

with open('7.csv', 'r', encoding='utf-8') as file:
    next(file)  # Пропускаємо перший рядок (заголовок)
    for line in file:
        surname, age = line.strip().split(',')
        employee_surnames.append(surname)
        employee_ages.append(int(age))

# Вікові групи
age_groups = ["18-24", "25-29", "30-35", "36-45", "46-60"]

# Обчислення відсотків для кожної вікової групи
total_employees = len(employee_ages)
percentages = []

for group in age_groups:
    start_age, end_age = map(int, group.split('-'))
    count = sum(1 for age in employee_ages if start_age <= age <= end_age)
    percentage = (count / total_employees) * 100
    percentages.append(percentage)

# Візуалізація кругової діаграми
plt.figure(figsize=(8, 8))
plt.pie(percentages, labels=age_groups, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0'])
plt.title('Відсоток звільнених/прийнятих співробітників за віковими групами')
plt.axis('equal')  # Забезпечення кругової форми діаграми



# ---TASK 8---
regions = []
birth_rates = []

with open('8.csv', 'r', encoding='utf-8') as file:
    next(file)  # Пропускаємо перший рядок (заголовок)
    for line in file:
        region, rate = line.strip().split(',')
        regions.append(region)
        birth_rates.append(int(rate))

# Візуалізація горизонтальної діаграми
plt.figure(figsize=(10, 6))
plt.barh(regions, birth_rates, color='green')
plt.title('Народжуваність за регіонами')
plt.xlabel('Народжуваність на 1000 осіб')
plt.ylabel('Регіон')

# Виведення текстової інформації біля стовпців
for i, rate in enumerate(birth_rates):
    plt.text(rate, i, str(rate), ha='left', va='center', color='black')


# ---TASK 9---
years = []
profits = []

with open('9.csv', 'r', encoding='utf-8') as file:
    next(file)  # Пропускаємо перший рядок (заголовок)
    for line in file:
        year, profit = line.strip().split(',')
        years.append(year)
        profits.append(int(profit))

# Візуалізація графіка
plt.figure(figsize=(10, 6))
plt.plot(years, profits, marker='o', color='red', linestyle='-')
plt.title('Зміна прибутковості акцій компанії')
plt.xlabel('Рік')
plt.ylabel('Прибутковість, долари')

# Виведення текстової інформації біля точок на графіку
for i, profit in enumerate(profits):
    plt.text(years[i], profit, str(profit), ha='center', va='bottom', color='black')

plt.grid(True)


# ---TASK 10---
activities = []
with open('10.csv', 'r', encoding='utf-8') as file:
    next(file)  # Пропускаємо перший рядок (заголовок)
    for line in file:
        fund, activity = line.strip().split(',')
        activities.append(activity)

# Обчислення часток фондів за діяльностями
fund_counts = Counter(activities)
funds = list(fund_counts.values())
activities = list(fund_counts.keys())

# Візуалізація кругової діаграми
plt.figure(figsize=(8, 8))
plt.pie(funds, labels=activities, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99', '#c2c2f0'])
plt.title('Розподіл фондів за діяльностями')
plt.axis('equal')  # Забезпечення кругової форми діаграми



# ---TASK 11---
incomes = []
salaries = []

with open('11.csv', 'r', encoding='utf-8') as file:
    next(file)  # Пропускаємо перший рядок (заголовок)
    for line in file:
        _, income, salary = line.strip().split(',')
        incomes.append(int(income))
        salaries.append(int(salary))

# Візуалізація точкової діаграми
plt.figure(figsize=(8, 6))
plt.scatter(incomes, salaries, color='blue', alpha=0.7)
plt.title('Зв\'язок між доходами та зарплатою')
plt.xlabel('Доходи, долари')
plt.ylabel('Зарплати, долари')
plt.grid(True)


# ---TASK 12---
students = []
grades = []

with open('12.csv', 'r', encoding='utf-8') as file:
    next(file)  # Пропускаємо перший рядок (заголовок)
    for line in file:
        student, grade = line.strip().split(',')
        students.append(student)
        grades.append(int(grade))

# Знаходження двох студентів з найкращою успішністю
top_students = sorted(zip(students, grades), key=lambda x: x[1], reverse=True)[:2]
top_student_names = [student[0] for student in top_students]
top_student_grades = [student[1] for student in top_students]

# Візуалізація стовпчикової діаграми
plt.figure(figsize=(10, 6))
bars = plt.bar(students, grades, color='skyblue')
plt.title('Успішність студентів')
plt.xlabel('Студент')
plt.ylabel('Середній бал')
plt.xticks(rotation=45)

# Підкреслення двох найкращих студентів
for i, bar in enumerate(bars):
    if students[i] in top_student_names:
        bar.set_color('green')

plt.tight_layout()
plt.show()