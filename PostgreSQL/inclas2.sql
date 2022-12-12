-- select min(e.salary) as ENDUSUK, max(salary) as ENBUYUK, avg(salary) as ORTALAMA, count(*) as TOPLAM from employees as e;

-- select * from employees;

-- select count(distinct (job) ) as farklimesleksayisi from employees;

-- select distinct (job) as farklimesleksayisi from employees;

-- select max(hiredate) from employees;

-- select sum(salary) from employees;

-- select avg(salary) as ortalama from employees;

-- select gender, avg(salary) as ortalama
-- from employees
-- group by gender;

-- select job, count(job) as calisansayisi 
-- from employees group by job ;

-- select job, count(job) as calisansayisi 
-- from employees where salary>2500 group by job ;

/* where, group by'dan önce olacak.. */

-- select gender, max(salary) as maxucret
-- from employees
-- group by gender
-- order by maxucret desc;







































