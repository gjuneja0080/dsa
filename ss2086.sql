with distinct_conversations as (
    select distinct least(message_sender_id, message_receiver_id) as user1,
    greatest(message_sender_id, message_receiver_id) as user2
    from whatsapp_messages
)
select count(*) as total_conversations
from distinct_conversations
