with ranked_salaries as (
    select id,
            name, 
            salary,
            departmentId,
            dense_rank() over (partition by departmentId order by salary desc) as rk
    from employee
)

select dept.name as Department, emp.name as Employee, emp.salary
from ranked_salaries emp join department dept
on emp.departmentId = dept.id
where rk <= 3
