-- Write a SQL query to find all duplicate emails in a table named Person.

-- +----+---------+
-- | Id | Email   |
-- +----+---------+
-- | 1  | a@b.com |
-- | 2  | c@d.com |
-- | 3  | a@b.com |
-- +----+---------+
-- For example, your query should return the following for the above table:

-- +---------+
-- | Email   |
-- +---------+
-- | a@b.com |
-- +---------+
-- Note: All emails are in lowercase.

## 我的答案
# Write your MySQL query statement below
select Email from (
    select Email,count(*) as nums from Person group by Email      
) a where a.nums > 1


## 标准答案
select Email
from Person
group by Email
having count(Email) > 1;