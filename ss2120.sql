with trans_per_promo as (
    select promotion_id, count(*) as num_trans
    from online_orders
    group by promotion_id
),
start_date_promos as (
    select p.promotion_id, coalesce(count(units_sold), 0) as start_date_promos
    from online_sales_promotions p left join online_orders o
    on p.promotion_id = o.promotion_id
    and p.start_date = o.date
    group by p.promotion_id
),
end_date_promos as (
    select p.promotion_id, coalesce(count(units_sold), 0) as end_date_promos
    from online_sales_promotions p left join online_orders o
    on p.promotion_id = o.promotion_id
    and p.end_date = o.date
    group by p.promotion_id
)

select t.promotion_id, 100*(s.start_date_promos/t.num_trans) as start_date_percentage,
        100*(e.end_date_promos/t.num_trans) as end_date_percentage
from trans_per_promo t join start_date_promos s
    on t.promotion_id = s.promotion_id
join end_date_promos e
    on t.promotion_id = e.promotion_id
