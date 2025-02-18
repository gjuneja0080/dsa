WITH sold_categories AS (
    SELECT DISTINCT p.product_category
    FROM online_orders o
    JOIN online_products p ON o.product_id = p.product_id
),
total_categories AS (
    SELECT COUNT(DISTINCT category_id) AS total_count
    FROM online_product_categories
),
unsold_categories AS (
    SELECT COUNT(DISTINCT pc.category_id) AS unsold_count
    FROM online_product_categories pc
    LEFT JOIN sold_categories sc ON pc.category_id = sc.product_category
    WHERE sc.product_category IS NULL
)
SELECT 
    (uc.unsold_count * 100.0) / tc.total_count AS percentage_unsold
FROM unsold_categories uc, total_categories tc;
