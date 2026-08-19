/* Write your T-SQL query statement below */
WITH qwe AS (
    SELECT *,
        SUM(weight) OVER (ORDER BY turn ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS asd
    FROM Queue
)
SELECT TOP 1 person_name
FROM qwe
WHERE asd <= 1000
ORDER BY turn DESC;