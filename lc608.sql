# Write your MySQL query statement below
with root_node as (
    select id, 'Root' as type
    from tree
    where p_id is null
),
leaf_nodes as (
    select id, 'Leaf' as type
    from tree
    where id not in (select p_id from tree where p_id is not null)
    and id not in (select id from root_node)
),
leaf_root as (
    select * from root_node
    union all
    select * from leaf_nodes
)
select * from leaf_root
union all
select id, 'Inner' as type
from tree
where id not in (select id from leaf_root)
