with gad as (
    select (2 * sum(duration))/(2 * count(duration)) as global_average_duration
    from calls
),
person_country as (
    select p.id as person_id, c.name as country_name 
    from person p
    join country c 
    on substring_index(p.phone_number, '-', 1) = c.country_code
),
person_country_duration as (
    select person_id, country_name, duration
    from person_country pc
    join calls c
    on pc.person_id = c.caller_id
    union all
    select person_id, country_name, duration
    from person_country pc
    join calls c
    on pc.person_id = c.callee_id
),
avg_duration_by_country as (
    select country_name, sum(duration)/count(person_id) as avg_dur_per_country
    from person_country_duration
    group by country_name
)
select country_name as country
from avg_duration_by_country, gad
where avg_dur_per_country > global_average_duration
