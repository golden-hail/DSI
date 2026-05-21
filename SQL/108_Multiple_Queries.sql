-------------------------------------------------------------------
--  TEMP TABLES & CTE FOR MULTIPLE QUERIES
-------------------------------------------------------------------

select * from grocery_db.transactions where customer_id = 1;

-- find average transaction spent per customer 
  -- currently at product_area_id level - need summation of product_area_ids per transaction, then find the average cost
  -- good habit to DROP temp tables after use to free up memory  

-- TEMPORARY TABLES

create temp table cust_transactions as (
select
  customer_id,
  transaction_id,
  sum(sales_cost) as total_sales
  
from
  grocery_db.transactions

group by
  customer_id,
  transaction_id
);

  -- can user DROP TABLE to get rid of temp table
select * from cust_transactions;

select
  customer_id,
  avg(total_sales) as avg_transaction_sales
  
from 
  cust_transactions
  
group by
  customer_id;

-- COMMON TABLE EXPRESSION (CTE)
  -- keyword: WITH
    -- query must be in parenthesis (can run multiple queries)
  -- everything happens in temp memory
    -- downside- error in one step, whole thing ends up being removed from memory

with cust_transactions_cte as (
select
  customer_id,
  transaction_id,
  sum(sales_cost) as total_sales
  
from
  grocery_db.transactions

group by
  customer_id,
  transaction_id
),

cust_sales_cte as (
select
  customer_id,
  avg(total_sales) as avg_transaction_sales
  
from 
  cust_transactions_cte
  
group by
  customer_id
  
)

select max(avg_transaction_sales) as max_avg_sales from cust_sales_cte;
