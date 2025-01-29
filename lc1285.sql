with v1 as (
    select log_id, row_number() over (order by log_id) as rn
    from logs
),
v2 as (
    select log_id, rn, (log_id - rn) as isles
    from v1
)
select min(log_id) as start_id, max(log_id) as end_id
from v2
group by isles
