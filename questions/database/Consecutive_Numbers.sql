-- Write a SQL query to find all numbers that appear at least three times consecutively.

-- +----+-----+
-- | Id | Num |
-- +----+-----+
-- | 1  |  1  |
-- | 2  |  1  |
-- | 3  |  1  |
-- | 4  |  2  |
-- | 5  |  1  |
-- | 6  |  2  |
-- | 7  |  2  |
-- +----+-----+
-- For example, given the above Logs table, 1 is the only number that appears consecutively for at least three times.

-- +-----------------+
-- | ConsecutiveNums |
-- +-----------------+
-- | 1               |
-- +-----------------+


-- 普通解法
SELECT DISTINCT l1.Num FROM Logs l1
JOIN Logs l2 ON l1.Id = l2.Id - 1
JOIN Logs l3 ON l1.Id = l3.Id - 2
WHERE l1.Num = l2.Num AND l2.Num = l3.Num;


-- 高级点解法
-- 解析: http://www.cnblogs.com/grandyang/p/5354173.html
-- SELECT DISTINCT Num FROM (
--   SELECT Num, COUNT(Rank) AS Cnt FROM (
--     SELECT    Num,
--               @curRank := @curRank + IF(@prevNum = Num, 0, 1) AS rank, @prevNum := Num
--     FROM      Logs s, (SELECT @curRank := 0) r, (SELECT @prevNum := NULL) p
--     ORDER BY  ID ASC
--   ) t GROUP BY Rank HAVING Cnt >= 3 
-- ) n;


-- SELECT DISTINCT Num FROM (
-- SELECT Num, @count := IF(@pre = Num, @count + 1, 1) AS n, @pre := Num
-- FROM Logs, (SELECT @count := 0, @pre := -1) AS init
-- ) AS t WHERE t.n >= 3;

select DISTINCT Num as ConsecutiveNums from (
    select Num,@curr_count := IF(Num = @pre,@curr_count+1,1) as count_num, @pre:=Num,
    from Logs,(SELECT @pre := -1, @curr_count := 0) as InitVal
)
where count_num>=3 