with avg_cmp_sal as (
    select date_format(pay_date, '%Y-%m') as ts, avg(amount) as mom_cmp_avg
    from salary
    group by 1
),
avg_dep_sal as (
    select date_format(pay_date, '%Y-%m') as ts, department_id, avg(amount) as mom_dept_avg
    from employee join salary
    on employee.employee_id = salary.employee_id
    group by 1, 2 
)
select avg_dep_sal.ts as pay_month, department_id, 
        case
            when mom_dept_avg > mom_cmp_avg then 'higher'
            when mom_dept_avg < mom_cmp_avg then 'lower'
            else 'same'
        end as comparison
from avg_dep_sal join avg_cmp_sal
on avg_dep_sal.ts = avg_cmp_sal.ts
