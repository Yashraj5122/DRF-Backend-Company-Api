from django.urls import path
from myapp.views import *
urlpatterns = [
    path('companies/company-register/', register_company),
    path('companies/company-list/', list_company),
    path('companies/<int:comp_code>/details/',get_company_details),
    path('companies/company-update/', update_company),
    path('companies/<int:comp_code>/delete/', delete_company),
    path('companies/company-deleted-list/', list_deleted_company),
    path('companies/company-restore/', restore_company),

    path('branches/branch-register/', register_branch),
    path('branches/branch-list/', list_branch),
    path('branches/<int:branch_code>/details/',get_branch_details),
    path('branches/branch-update/', update_branch),
    path('branches/<int:branch_code>/delete/', delete_branch),
    path('branches/branch-deleted-list/', list_deleted_branch),
    path('branches/branch-restore/', restore_branch),

    path('employees/employee-register/', register_employee),
    path('employees/employee-list/', list_employee),
    path('employees/<int:emp_id>/details/', get_employee_details),
    path('employees/employee-update/', update_employee),
    path('employees/<int:emp_id>/delete/', delete_employee),
    path('employees/employee-deleted-list/', list_deleted_employee),
    path('employees/employee-restore/', restore_employee),

    path('companies/<int:comp_code>/branches/', get_branches_for_company),
    path('branches/<int:branch_code>/companies/', get_company_for_branches),
    path('companies/<int:comp_code>/employees/', get_employee_for_company),
    path('branches/<int:branch_code>/employees/', get_employee_for_branch),
    path('employees/<int:comp_code>/<int:branch_code>/', get_employees_by_company_and_branch),
    path('employees/filter/',get_employees_by_created_at),

    path('employees/search/', search_employees)
]
