-------------------------------------------------------------------
-- CONDITIONAL RULES USING CASE WHEN
-------------------------------------------------------------------

-- CASE WHEN (similar to if, then, else)
  -- common use case is for true/flase flag for reporting 
  -- example: creating a table with a clo=umn for high loylaty and low loyalty customers
  
select
  customer_id,
  customer_loyalty_score,
  case when customer_loyalty_score > 0.5 then 'High Loyal' else 'Low Loyal' end as high_loyal_flag
  
from
  grocery_db.loyalty_scores;
  
-- MULTIPLE CONDITIONS
  -- Example: with high, medium, and low loyalties
  -- NOTE: CASE, WHENs go in order (like if/else)
  
select
  customer_id,
  customer_loyalty_score,
  case 
    when customer_loyalty_score > 0.6 then 'High Loyal' 
    when customer_loyalty_score > 0.33 then 'Medium Loyal' 
    else 'Low Loyal' end as high_loyal_flag
  
from
  grocery_db.loyalty_scores;
  
-- CASE WHEN + AGGREGATION
  -- EXAMPLE: New columns from transactions data table that sums uip sales for each category of sales per customer,
  -- we want a wide table with one row per customer so it's easy to look at the data from the customer_id perspective 
  -- no commas in case-whens
select 
  customer_id,
  sum(case when product_area_id = 1 then sales_cost else 0 end) as non_food_sales,
  sum(case when product_area_id = 2 then sales_cost else 0 end) as veggie_sales,
  sum(case when product_area_id = 3 then sales_cost else 0 end) as fruit_sales,
  sum(case when product_area_id = 4 then sales_cost else 0 end) as dairy_sales,
  sum(case when product_area_id = 5 then sales_cost else 0 end) as meat_sales
  
from
  grocery_db.transactions
  
group by
  customer_id;
  
/* PRACTICE:

 You've been tasked with creating a categorized version of a customer's distance from the store.

Your new column (called distance_from_store_category) will follow these rules:

If a customer lives less than 1 mile from the store there will be a value of "distance: close"
If a customer lives less than 2.5 miles from the store (but more than 1 mile) there will be a value of "distance: medium"
Otherwise, if a customer lives further than 2.5 miles from the store there will be a value of "distance: far"

Your query will return three columns:

customer_id
distance_from_store
distance_from_store_category (you will create this)

Bonus: Also ensure that any rows that are missing a value for distance_from_store are not included */

select
  customer_id,
  distance_from_store,
  case 
    when distance_from_store < 1 then 'distance: close'
    when distance_from_store < 2.5 then 'distance: medium'
    else 'distance: far' end as distance_from_store_category
    
from
  grocery_db.customer_details
  
where
  distance_from_store is not null;
  
