with ranked_orders as (
    select order_date, customer_pref_delivery_date,
        rank() over (partition by customer_id order by order_date) as rnk
    from delivery
)

select round(100*(sum(case when order_date = customer_pref_delivery_date and rnk = 1 then 1 end) / sum(rnk = 1)), 2) as immediate_percentage
from ranked_orders
