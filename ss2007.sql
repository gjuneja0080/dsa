with country_comms as (
    select country, date_format(created_at, '%Y-%m') as yearmonth, sum(number_of_comments) as total_comments, 
    dense_rank() over 
        (partition by  date_format(created_at, '%Y-%m') order by sum(number_of_comments)) as rnk
    from fb_comments_count fcc join fb_active_users fac
    on fcc.user_id = fac.user_id
    where date_format(created_at, '%Y-%m') in ('2019-12', '2020-01')
    group by country, yearmonth
),
dec_2019 as (
    select country, rnk
    from country_comms
    where yearmonth = '2019-12'
),
jan_2020 as (
    select country, rnk
    from country_comms
    where yearmonth = '2020-01'
),
country_rank_join as (
    select d.country, d.rnk as rank_2019, j.rnk as rank_2020
    from dec_2019 d join jan_2020 j
    on d.country = j.country
)
select country
from country_rank_join
order by abs(cast(rank_2019 as signed)-cast(rank_2020 as signed)) desc
limit 1;
