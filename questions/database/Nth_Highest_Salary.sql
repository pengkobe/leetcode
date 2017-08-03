-- Write a SQL query to get the nth highest salary from the Employee table.

-- +----+--------+
-- | Id | Salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+
-- For example, given the above Employee table, the nth highest salary where n = 2 is 200. If there is no nth highest salary, then the query should return null.

-- +------------------------+
-- | getNthHighestSalary(2) |
-- +------------------------+
-- | 200                    |
-- +------------------------+


-- CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
-- BEGIN
--   RETURN (
--       # Write your MySQL query statement below.
--       select Salary from   
--       ( 
--           select b.Salary,count(DISTINCT b.Salary) from 
--           Employee b,Employee a 
--           where b.salary > a.salary and count(DISTINCT Salary) = N 
--       )
      
--   );
-- END


 SET N = N - 1;
  RETURN (
    SELECT CASE 
    WHEN COUNT(Salary) >= 1 THEN (
      SELECT DISTINCT Salary 
      FROM Employee
      ORDER BY Salary DESC 
      LIMIT N, 1) 
    ELSE NULL
    END AS NthSalary
    FROM Employee
  );

-- Sql server 解法
-- SELECT EmployeeId, Salary
-- FROM
-- (
-- Select EmployeeId, Salary, ROW_NUMBER() OVER(Order by Salary Desc) as Salary_Order
-- from   Employee
-- ) DT
-- WHERE DT. Salary_Order = 4 ;