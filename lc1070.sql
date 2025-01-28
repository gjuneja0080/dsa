select s.product_id, s.year as first_year, sum(s.quantity) as quantity, s.price
from sales s left join product p
on s.product_id = p.product_id
where (s.product_id, s.year) in (
    select s.product_id, min(s.year)
    from sales s 
    group by product_id
)
group by s.product_id, s.price
