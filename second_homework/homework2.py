import csv
import sys


def read_data(file_name: str) -> list[dict[str, str]]:
    """Чтение CSV"""
    with open(file_name, 'r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file, delimiter=';')
        employees = list(reader)
    return employees


def print_hierarchy(employees: list[dict[str, str]]) -> None:
    """Иерархия команд"""
    hierarchy = {}

    for employee in employees:
        department = employee['Департамент']
        team = employee['Отдел']
        if department not in hierarchy:
            hierarchy[department] = set()
        hierarchy[department].add(team)

    departments = sorted(hierarchy)
    for department in departments:
        print(department)
        teams = sorted(hierarchy[department])
        for team in teams:
            print(f'  {team}')


def get_summary(employees: list[dict[str, str]]) -> dict:
    """Расчет сводки по департаментам"""
    summary = {}

    for employee in employees:
        department = employee['Департамент']
        salary = int(employee['Оклад'])

        if department not in summary:
            summary[department] = []
        summary[department].append(salary)

    return summary


def print_summary(employees: list[dict[str, str]]) -> None:
    """Вывод сводки по департаментам"""
    summary = get_summary(employees)

    departments = sorted(summary)
    for department in departments:
        salaries = summary[department]
        employee_count = len(salaries)
        min_salary = min(salaries)
        max_salary = max(salaries)
        average_salary = sum(salaries) / len(salaries)

        print(department)
        print(f'  Сотрудников: {employee_count}')
        print(f'  Минимальная зарплата: {min_salary}')
        print(f'  Максимальная зарплата: {max_salary}')
        print(f'  Средняя зарплата: {average_salary:.2f}')


def save_summary(employees: list[dict[str, str]], file_name: str) -> None:
    """Запись сводки в CSV"""
    summary = get_summary(employees)
    fieldnames = ['Департамент', 'Сотрудников', 'Минимальная зарплата', 'Максимальная зарплата', 'Средняя зарплата']

    with open(file_name, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        departments = sorted(summary)
        for department in departments:
            salaries = summary[department]
            employee_count = len(salaries)
            min_salary = min(salaries)
            max_salary = max(salaries)
            average_salary = sum(salaries) / len(salaries)

            department_data = {
                'Департамент': department,
                'Сотрудников': employee_count,
                'Минимальная зарплата': min_salary,
                'Максимальная зарплата': max_salary,
                'Средняя зарплата': f'{average_salary:.2f}',
            }
            writer.writerow(department_data)

    print(f'Отчёт сохранён в {file_name}')


def main(report_number: int) -> None:
    employees = read_data('Corp_Summary.csv')

    if report_number == 1:
        print_hierarchy(employees)
    elif report_number == 2:
        print_summary(employees)
    else:
        save_summary(employees, 'department_summary.csv')


if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in ('1', '2', '3'):
        raise SystemExit('Укажите номер отчёта: 1, 2 или 3')
    main(int(sys.argv[1]))
