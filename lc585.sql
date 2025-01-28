with v1 as (
    select tiv_2015, tiv_2016, 
            count(concat(lat, ',', lon)) over (partition by concat(lat, ',', lon)) as total_coords,
            count(tiv_2015) over (partition by tiv_2015) as total_occs
    from insurance
)
select round(sum(tiv_2016), 2) as tiv_2016
from v1 
where total_coords = 1 and total_occs > 1
