with one_friends as (
    select least(user1_id, user2_id) as user_id, greatest(user1_id, user2_id) as friend
    from friendship
    where least(user1_id, user2_id) = 1
),
friends_likes as (
    select l.user_id, friend, page_id
    from one_friends onef join likes l
    on onef.friend = l.user_id
)
select distinct page_id as recommended_page
from friends_likes where page_id not in (select page_id from likes where user_id = 1)
