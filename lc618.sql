with america as (
    select name as America, row_number() over () as rn
    from student where continent = 'America'
    order by 1
),
europe as (
    select name as Europe, row_number() over () as rn
    from student where continent = 'Europe'
    order by 1
),
asia as (
    select name as Asia, row_number() over () as rn
    from student where continent = 'Asia'
    order by 1
)

select America, Asia, Europe
from america
left join europe on america.rn = europe.rn
left join asia on america.rn = asia.rn

union all

select null as America, Asia, Europe
from asia 
left join europe on asia.rn = europe.rn
where asia.rn > (select count(*) from america)

union all

select null as America, null as Asia, Europe
from europe
where europe.rn > (select count(*) from america)
and europe.rn > (select count(*) from asia)
