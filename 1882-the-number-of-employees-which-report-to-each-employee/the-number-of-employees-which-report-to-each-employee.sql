# Write your MySQL query statement below
select e1.employee_id ,e1.name,count( distinct e.employee_id) as reports_count,round(avg(e.age)) as average_age from employees e
join employees e1
    on e.reports_to=e1.employee_id
group by e1.employee_id,e1.name
order by e1.employee_id