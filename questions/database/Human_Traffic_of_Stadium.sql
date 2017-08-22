-- X city built a new stadium, each day many people visit it and the stats are saved as these columns: id, date, people

-- Please write a query to display the records which have 3 or more consecutive rows and the amount of people more than 100(inclusive).

-- For example, the table stadium:
-- +------+------------+-----------+
-- | id   | date       | people    |
-- +------+------------+-----------+
-- | 1    | 2017-01-01 | 10        |
-- | 2    | 2017-01-02 | 109       |
-- | 3    | 2017-01-03 | 150       |
-- | 4    | 2017-01-04 | 99        |
-- | 5    | 2017-01-05 | 145       |
-- | 6    | 2017-01-06 | 1455      |
-- | 7    | 2017-01-07 | 199       |
-- | 8    | 2017-01-08 | 188       |
-- +------+------------+-----------+
-- For the sample data above, the output is:

-- +------+------------+-----------+
-- | id   | date       | people    |
-- +------+------------+-----------+
-- | 5    | 2017-01-05 | 145       |
-- | 6    | 2017-01-06 | 1455      |
-- | 7    | 2017-01-07 | 199       |
-- | 8    | 2017-01-08 | 188       |
-- +------+------------+-----------+
-- Note:
-- Each day only have one row record, and the dates are increasing with id increasing.




# Write your MySQL query statement below
select a.* from stadium a where a.people >= 100 and
(
    (
    a.id-2 in (select b.id from stadium b where b.people >= 100) and
    a.id-1 in (select c.id from stadium c where c.people >= 100) 
    )
    or
    (
        a.id-1 in (select d.id from stadium d where d.people >= 100) and
        a.id+1 in (select e.id from stadium e where e.people >= 100) 
    )
    or
    (
        a.id+1 in (select f.id from stadium f where f.people >= 100) and
        a.id+2 in (select j.id from stadium j where j.people >= 100) 
    )
)

-- 参考答案1
-- select * from stadium a   where a.people >= 100 and 
-- (
--     (
--         a.id+1 in  (select id from stadium where people >= 100) 
--         and 
--         a.id+2 in  (select id from stadium where people >= 100) 
--     )
--     or 
--     (
--         a.id-1  in  (select id from stadium where people >= 100) 
--         and 
--         a.id+1  in  (select id from stadium where people >= 100) 
--     )
--     or 
--     (
--         a.id-1  in  (select id from stadium where people >= 100) 
--         and 
--         a.id-2  in  (select id from stadium where people >= 100) 
--     )
-- );

-- 参考答案2
-- set @rownum1:=0;
-- set @rownum2:=0;
-- select temp1.id,temp1.date,temp1.people
-- from (select count(*) as row_counts,diffnum
--     from (select t.*,t.id-t.row_num as diffnum
--             from (select a.*,
--                 @rownum1:=@rownum1+1 as row_num
--                     from (select * from stadium  where people>=100) a) t)s
-- group by diffnum) temp2
-- join
-- (select t.*,t.id-t.row_num as diffnum
--  from (select a.*,
--    @rownum2:=@rownum2+1 as row_num
--      from (select * from stadium  where people>=100) a) t) temp1
-- on (temp1.diffnum=temp2.diffnum)
-- where temp2.row_counts>=3
-- order by temp1.date