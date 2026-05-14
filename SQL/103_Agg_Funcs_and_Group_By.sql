-------------------------------------------------------------------
-- AGGREGATING OUR DATA 
-------------------------------------------------------------------

-- AGGREGATION FUNCTIONS
/*
  -aggregation function examples in green  
  -example: creating a new table with aggregated data
*/
select
  sum(sales_cost) as total_sales,
  avg(sales_cost) as avg_sales,
  min(sales_cost) as min_sales,
  max(sales_cost) as max_sales,  
  count(*) as num_rows,
  count (distinct transaction_id) as num_transactions 
from
  grocery_db.transactions;


-- THE GROUP BY STATEMENT
select
  transaction_date,
  sum(sales_cost) as total_sales,
  sum(num_items) as total_items,
  count (distinct transaction_id) as num_transactions 
  
from
  grocery_db.transactions
  
group by
  transaction_date
  
order by
  transaction_date;

-- GROUPING BY MULTIPLE VARIABLES
select
  product_area_id,  
  transaction_date,
  sum(sales_cost) as total_sales,
  sum(num_items) as total_items,
  count (distinct transaction_id) as num_transactions 
  
from
  grocery_db.transactions
  
group by
  product_area_id,  
  transaction_date
  
order by
  product_area_id,  
  transaction_date;

-- THE HAVING CLAUSE
/* While WHERE sets filter conditions on the origin table..
HAVING applies to the aggregated output?

Include product areas that had at least $200,000 worth of sales
*/
select
  product_area_id,
  sum(sales_cost) as total_sales
  
from 
  grocery_db.transactions
  
group by
  product_area_id

having
  sum(sales_cost) > 200000;
  
/* Exercise:
You've been tasked with returning data that shows; for each transaction date, the number of unique customers that transacted in-store.

To make it easy for stakeholders to view, ensure the output is ordered by transaction date (earliest to latest)

Your query will return two columns:

transaction_date (ordered)
customer_count (hint: you will create this) */

select
  transaction_date, 
  count (distinct customer_id) as customer_count
  
from
  grocery_db.transactions

group by
  transaction_date
  
order by
  transaction_date;
