# Company, Branch, and Employee Management API

This project is a RESTful API built with Django REST Framework (DRF) that allows for comprehensive management of companies, branches, and employees. It provides robust CRUD operations to facilitate the handling of organizational data.

## Features

- **Company Management**: Register, list, update, delete, and restore companies.
- **Branch Management**: Register, list, update, delete, and restore branches.
- **Employee Management**: Register, list, update, delete, and restore employees.
- **Filtering and Search**: Filter employees by creation date and search functionality.

## API Endpoints

### Companies

- `POST /companies/company-register/`: Register a new company.
- `GET /companies/company-list/`: Retrieve a list of all companies.
- `GET /companies/{comp_code}/details/`: Retrieve details of a specific company.
- `PUT /companies/company-update/`: Update an existing company.
- `DELETE /companies/{comp_code}/delete/`: Delete a specific company.
- `GET /companies/company-deleted-list/`: Retrieve a list of deleted companies.
- `POST /companies/company-restore/`: Restore a deleted company.

### Branches

- `POST /branches/branch-register/`: Register a new branch.
- `GET /branches/branch-list/`: Retrieve a list of all branches.
- `GET /branches/{branch_code}/details/`: Retrieve details of a specific branch.
- `PUT /branches/branch-update/`: Update an existing branch.
- `DELETE /branches/{branch_code}/delete/`: Delete a specific branch.
- `GET /branches/branch-deleted-list/`: Retrieve a list of deleted branches.
- `POST /branches/branch-restore/`: Restore a deleted branch.

### Employees

- `POST /employees/employee-register/`: Register a new employee.
- `GET /employees/employee-list/`: Retrieve a list of all employees.
- `GET /employees/{emp_id}/details/`: Retrieve details of a specific employee.
- `PUT /employees/employee-update/`: Update an existing employee.
- `DELETE /employees/{emp_id}/delete/`: Delete a specific employee.
- `GET /employees/employee-deleted-list/`: Retrieve a list of deleted employees.
- `POST /employees/employee-restore/`: Restore a deleted employee.
- `GET /employees/filter/`: Filter employees by creation date.
- `GET /employees/search/`: Search for employees.


