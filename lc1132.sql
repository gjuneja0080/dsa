with daily_percentage as (
    select action_date,
        count(
            distinct
                case
                    when a.post_id = r.post_id then r.post_id 
                    end 
        )/count(distinct a.post_id) as daily_rate
        from actions a left join removals r
        on a.post_id = r.post_id
        where a.extra = 'spam'
        group by action_date 
)
select round(avg(daily_rate) * 100, 2) as average_daily_percent
from daily_percentage
