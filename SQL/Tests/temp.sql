select
  a.customer_id,
  a.credit_score,
  sum(b.sales_cost) as tot_sales_sept

from
  grocery_db.customer_details a  
  full join grocery_db.transactions b on a.customer_id = b.customer_id
  
group by
  customer_id

having
  transaction_date between '09-01-2020' and '09-31-2020';
  
select * from grocery_db.transactions;
