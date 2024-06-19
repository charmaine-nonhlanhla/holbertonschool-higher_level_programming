-- Query to list all cities of California without using JOIN

-- Select cities of California using a subquery
SELECT *
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;

