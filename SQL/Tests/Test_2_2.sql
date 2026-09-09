-------------------------------------------------------------------
--  SQL TEST 2
-------------------------------------------------------------------

select * from grocery_db.customer_details;
select * from grocery_db.transactions;
select * from grocery_db.campaign_data;
select * from grocery_db.product_areas;
select * from grocery_db.loyalty_scores;

-----------------------------------------------------------------------
-- 1) How many unique transactions are there in the transactions table?
-----------------------------------------------------------------------

select
  count(distinct(transaction_id))
  
from
  grocery_db.transactions;
  
------------------------------------------------------------------------------------------
-- 2) How many customers were in each mailer_type category for the delivery club campaign?
------------------------------------------------------------------------------------------

select
  mailer_type,
  count(distinct(customer_id)),
  campaign_name
  
from 
  grocery_db.campaign_data
  
where
  campaign_name = 'delivery_club'
  
group by
  mailer_type,
  campaign_name;
  
-----------------------------------------------------------------------------------------------
-- 3) Return a list of customers who spent more than $500 and had 5 or more unique transactions
-- in the month of August 2020
-----------------------------------------------------------------------------------------------

select
  customer_id,
  count(distinct(transaction_id)) as total_trans,
  sum(sales_cost) as totes
  
from grocery_db.transactions

where 
  transaction_date between '08-01-2020' and '08-31-2020'
  
group by
  customer_id
  
having
  count(distinct(transaction_id)) >= 5 and
  sum(sales_cost) > 500;

-----------------------------------------------------------------------------------------------
-- 4) Return a list of duplicate credit scores that exist in the customer_details table
-----------------------------------------------------------------------------------------------
  
select
  credit_score,
  count(credit_score) as cs_score
  
from
  grocery_db.customer_details
  
group by
  credit_score
  
having
  count(credit_score) > 1;

----------------------------------------------------------------------------------------------
-- 5) Return the customer_id(s) for the customer(s) who has/have the 2nd highest credit score. 
-- Make sure your code would work for the Nth highest credit score as well
----------------------------------------------------------------------------------------------

with credit_scores as (

select
  customer_id,
  credit_score,
  dense_rank() over (order by credit_score desc) as cs_rank
  
from
  grocery_db.customer_details
  
where
  credit_score is not null
  
)

select
  customer_id
  
from
  credit_scores
  
where
  cs_rank = 2;
  
