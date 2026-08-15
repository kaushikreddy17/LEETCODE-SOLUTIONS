/* Write your T-SQL query statement below */
select *,iif(x+y>z And y+z>x And z+x>y,'Yes','No') as triangle from triangle