-------------------------------------------------------------------
--  SQL TEST 1
-------------------------------------------------------------------

select * from grocery_db.customer_details;
select * from grocery_db.transactions;
select * from grocery_db.campaign_data;
select * from grocery_db.product_areas;
select * from grocery_db.loyalty_scores;

-------------------------------------------------------------------
-- 1) How many rows in the transactions table?
-------------------------------------------------------------------

select
  count(*)
  
from
  grocery_db.transactions;
  
-------------------------------------------------------------------
-- 2) Return the customer_id for the customer who lives the farthest away from the store:
-------------------------------------------------------------------

  -- method 1
select
  customer_id,
  distance_from_store
  
from 
  grocery_db.customer_details
  
where 
  distance_from_store is not null
  
order by
  distance_from_store DESC
  LIMIT 1;
  
  -- method 2 !!! THIS IS BETTER BECAUSE IT WILL LIST ALL CUSTOMER_IDs IN THE CASE OF A TIE 
select 
  a.customer_id
  
from
  grocery_db.customer_details a
  inner join (
    select
      max(distance_from_store) as max_dist
     from
      grocery_db.customer_details) b on a.distance_from_Store = b.max_dist;
  -- method 3, could also use RANK = 1 if a rank was created 
  
-------------------------------------------------------------------
-- 3) Return the number of unique customers in the customer_details table, split by gender
-------------------------------------------------------------------

select
  distinct  
  count(customer_id) over (partition by gender) as num_peeps,
  gender
  
from
  grocery_db.customer_details;
  
          /*
          OR (depends on how you see gender lol)
          */

select
  count(distinct(customer_id)) as num_peeps,
  gender
  
from
  grocery_db.customer_details
  
group by 
  gender;
  
-------------------------------------------------------------------------
-- 4) What were the total sales for each product area name for July 2020. 
-- Return these in the order of highest sales to lowest sales
-------------------------------------------------------------------------

--------- Tonii approach ---------  
  -- run first
create temp table lulu as (

select
  a.*,
  b.product_area_name
  
from
  grocery_db.transactions a 
  full join grocery_db.product_areas b on a.product_area_id = b.product_area_id
  
);
  -- run second
select
  distinct
  product_area_name,
  sum(sales_cost) over (partition by product_area_name) as total_sales
  
from lulu

where
  transaction_date between '07-01-2020' and '07-31-2020'

order by total_sales DESC;

--------- Answer --------- 
select
  b.product_area_name,
  sum(a.sales_cost) as total_sales
  
from
  grocery_db.transactions a
  inner join grocery_db.product_areas b on a.product_area_id = b.product_area_id
  
where
  a.transaction_date between '07-01-2020' and '07-31-2020'
  
group by
  b.product_area_name
  
order by
  total_sales desc;

--------------------------------------------------------------------------------------
-- 5) Return a list of all customer_id's that do NOT have a loyalty score 
-- (i.e. they are in the customer_details table, but not in the loyalty_scores table)
--------------------------------------------------------------------------------------

select * from grocery_db.loyalty_scores;
select * from grocery_db.customer_details;

--------- Tonii approach ---------  

select
  a.customer_id,
  b.customer_loyalty_score
  
from
    grocery_db.customer_details a 
    full join grocery_db.loyalty_scores b on a.customer_id = b.customer_id
    
where
  customer_loyalty_score is null;
  
--------- Answer ---------  

select
  distinct a.customer_id
  
from
  grocery_db.customer_details a
  left join grocery_db.loyalty_scores b on a.customer_id = b.customer_id
  
where
  b.customer_id is null;
  
