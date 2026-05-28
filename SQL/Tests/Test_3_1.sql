-------------------------------------------------------------------
--  SQL TEST 3
-------------------------------------------------------------------

select * from grocery_db.customer_details;
select * from grocery_db.transactions;
select * from grocery_db.campaign_data;
select * from grocery_db.product_areas;
select * from grocery_db.loyalty_scores;

---------------------------------------------------------------
-- 1) Return a list of customers from the loyalty_scores table
-- who have a customer_loyalty_score of 0.77, 0.88, or 0.9
---------------------------------------------------------------

select
  customer_id,
  customer_loyalty_score
  
from
  grocery_db.loyalty_scores
  
where
  customer_loyalty_score in (0.77, 0.88, 0.9)
  
order by
  customer_loyalty_score;

----------------------------------------------------------------------------------
-- 2) Return the average customer_loyalty_score for customers, split by gender
----------------------------------------------------------------------------------

  --Tonii method
with gen_loyalty as (

select
  a.customer_id,
  a.customer_loyalty_score,
  b.gender
  
from
  grocery_db.loyalty_scores a
  full join grocery_db.customer_details b on a.customer_id = b.customer_id
)

select
  gender,
  avg(customer_loyalty_score)
  
from
  gen_loyalty
  
group by
  gender;
  
-- cleaner answer
select
  b.gender,
  avg(a.customer_loyalty_score) as avg_loy_score
  
from
  grocery_db.loyalty_scores a
  full join grocery_db.customer_details b on a.customer_id = b.customer_id

group by
  b.gender;
  
----------------------------------------------------------------------------------------
-- 3) Return customer_id, distance_from_store, and a new column called distance_category 
-- that tags customers who are less than 1 mile from store as "Walking Distance", 1 mile
-- or more from store as "Driving Distance" and "Unknown" for customers where we do not 
-- know their distance from the store
----------------------------------------------------------------------------------------

select
  customer_id,
  distance_from_store,
  case
    when distance_from_store < 1 then 'Walking Distance'
    when distance_from_store >= 1 then 'driving distance'
    else 'unknown' end as distance_category
    
from
  grocery_db.customer_details;
  
-----------------------------------------------------------------------------------------------
-- 4) For the 400 customers with a customer_loyalty_score, divide them up into 10 deciles, 
-- and calculate the average distance_from_store for each decile
-----------------------------------------------------------------------------------------------
with njoin as (

select
  a.customer_id,
  a.customer_loyalty_score,
  b.distance_from_store,
  ntile(10) over (order by customer_loyalty_score desc) as percentile

from 
  grocery_db.loyalty_scores a
  full join grocery_db.customer_details b on a.customer_id = b.customer_id

where
  customer_loyalty_score is not null
  
)

select
  distinct percentile,
  avg(distance_from_store) over (partition by percentile)
  
from njoin;
  
----------------------------------------------------------------------------------------------
-- 5) Return data showing, for each product_area_name - the total sales, and the percentage 
-- of overall sales that each product area makes up
----------------------------------------------------------------------------------------------
with sales as (
  
select
  b.product_area_name,
  sum(a.sales_cost) as total_sales

from 
  grocery_db.transactions a
  inner join grocery_db.product_areas b on a.product_area_id = b.product_area_id
  
group by
  b.product_area_name
 
)

select
  product_area_name,
  total_sales,
  total_sales / (select sum(total_sales) from sales) * 100 as total_sales_pc
  
from
  sales;
