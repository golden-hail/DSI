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
  customer_id
  
from grocery_db.customer_details

where
  distance_from_store is not null
  
order by 
  distance_from_store DESC
  
limit
1; 

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
  gender,  
  count(distinct(customer_id)) as total_custs

from grocery_db.customer_details

group by 
  gender;
  
-------------------------------------------------------------------------
-- 4) What were the total sales for each product area name for July 2020. 
-- Return these in the order of highest sales to lowest sales
-------------------------------------------------------------------------

select 
 b.product_area_name,
 sum(a.sales_cost) as total_sales_July
 
from grocery_db.transactions a
  left join grocery_db.product_areas b on a.product_area_id = b.product_area_id

where a.transaction_date between '2020-07-01' and '2020-07-31'

group by
  product_area_name
  
order by
sum(a.sales_cost) DESC;

--------------------------------------------------------------------------------------
-- 5) Return a list of all customer_id's that do NOT have a loyalty score 
-- (i.e. they are in the customer_details table, but not in the loyalty_scores table)
--------------------------------------------------------------------------------------

select 
  distinct a.customer_id

from grocery_db.customer_details a
left join grocery_db.loyalty_scores b on a.customer_id = b.customer_id

where b.customer_loyalty_score is null;
