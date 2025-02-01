with count_per_dept as (
    select dep_id, count(emp_id) as num_emps
    from employees
    group by dep_id
),
max_dept as (
    select max(num_emps) as highest_count
    from count_per_dept
)
select e.emp_name as manager_name, c.dep_id
from employees e join count_per_dept c
on e.dep_id = c.dep_id
where c.num_emps in (select highest_count from max_dept)
and e.position = 'Manager'
order by dep_id
