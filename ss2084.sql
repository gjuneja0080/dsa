with all_blocked as (
    select user_id, block_reason
    from fb_blocked_users
    where date_format(block_date, '%Y-%m') = '2021-12'
    union
    select user_id, block_reason
    from fb_blocked_users
    where block_date < '2021-12-01'
    and
        (
            (date_add(block_date, interval block_duration day) > '2021-12-01' )
            or
            (block_duration is null)
        )
)
select block_reason, count(user_id) as n_users
from all_blocked
group by block_reason
