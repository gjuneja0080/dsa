with users_per_contest as (
    select contest_id, count(user_id) as num_users
    from register
    group by contest_id
)
select contest_id, round(100.0*(num_users/count(u.user_id)), 2) as percentage
from users_per_contest, users u
group by contest_id
order by percentage desc, contest_id asc
