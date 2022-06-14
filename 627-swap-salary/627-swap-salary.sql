# Write your MySQL query statement below
UPDATE Salary
SET 
    sex = CASE sex
    WHEN sex = 'f' THEN 'f'
    ELSE 'm'
END