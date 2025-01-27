# lag date and amount
# filter based on consecutive and amount
# get islands
# find islands >= 3
WITH increasing_consecutive AS (
  SELECT 
    a.customer_id, 
    a.transaction_date 
  FROM 
    Transactions a 
    JOIN Transactions b ON a.customer_id = b.customer_id 
    AND b.amount > a.amount 
    AND DATEDIFF(
      b.transaction_date, a.transaction_date
    ) = 1
), 
row_indexed as (
    select customer_id, transaction_date,
        row_number() over (partition by customer_id order by transaction_date) as rn
    from increasing_consecutive
),
islands as (
    select customer_id, transaction_date,
     date_sub(transaction_date, interval rn day) as isle_id
    from row_indexed 
),
trans_group as (
    select customer_id, min(transaction_date) as consecutive_start, count(*) as transaction_count
    from islands
    group by customer_id, isle_id
)
select customer_id, consecutive_start, date_add(consecutive_start, interval transaction_count day) as consecutive_end
from trans_group
where transaction_count > 1
order by customer_id
