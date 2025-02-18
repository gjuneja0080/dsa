with ranked_promotions as (
    select promotion_id, product_id, 
    sum(units_sold) as total_units_sold,
        rank() over (partition by promotion_id order by sum(units_sold) desc) as rnk
    from online_orders
    group by 1, 2
    order by promotion_id, sum(units_sold) desc
)
select promotion_id, product_id, total_units_sold
from ranked_promotions
where rnk = 1
