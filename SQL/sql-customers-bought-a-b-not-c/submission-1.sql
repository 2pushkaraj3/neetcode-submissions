-- Write your query below
select 
a.customer_id,
b.customer_name
from orders a
left join customers b on a.customer_id=b.customer_id
group by 1,2
having count(distinct case when product_name in ('A','B') then product_name end) > 1 and count(distinct case when product_name in ('C') then product_name end) = 0
order by 2