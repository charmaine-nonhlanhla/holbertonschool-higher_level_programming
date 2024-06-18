-- Query to calculate the average temperature by city in Fahrenheit
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
