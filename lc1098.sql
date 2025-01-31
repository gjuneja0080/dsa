select b.book_id, b.name
from orders o right join books b
on o.book_id = b.book_id
and dispatch_date between date_sub('2019-06-23', interval 1 year) and '2019-06-23'
where  available_from < date_sub('2019-06-23', interval 1 month)
group by b.book_id, b.name
having ifnull(sum(quantity), 0) < 10;
