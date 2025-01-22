select request_at as Day, round(sum(status != 'completed') / count(*), 2) as 'Cancellation Rate'
from trips
  LEFT JOIN users AS Clients ON Trips.client_id = Clients.users_id 
  LEFT JOIN users AS Drivers ON Trips.driver_id = Drivers.users_id
where
    clients.banned='No'
and
    drivers.banned='No'
and
    request_at between '2013-10-01' and '2013-10-03'
group by day
