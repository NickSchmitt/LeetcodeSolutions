# Write your MySQL query statement below
SELECT Name as 'Customers'
from Customers c
LEFT JOIN Orders o
ON c.Id = o.CustomerId
WHERE o.CustomerId IS NULL