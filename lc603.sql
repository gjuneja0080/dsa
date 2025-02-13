select seat_id
from cinema
where
    ((seat_id + 1) in (select seat_id from cinema where free = 1)
or
    (seat_id - 1) in (select seat_id from cinema where free = 1))
and 
    free = 1
