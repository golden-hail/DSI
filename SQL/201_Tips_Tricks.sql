-------------------------------------------------------------------
--  USEFUL TIPS AND TRICKS (VOLUME 1)
-------------------------------------------------------------------

-------------------------------------------------------------------
--  Using Sub-Queries
-------------------------------------------------------------------
-- goode for smaller operations, temp tables / CTE for more complex scripts
-- Example: find the greatest profit margin using WHERE
select
  product_area_name,
  profit_margin
  
from 
  grocery_db.product_areas
  
where
  profit_margin = (select max(profit_margin) from grocery_db.product_areas);

-------------------------------------------------------------------
--  Using Lead and Lag
-------------------------------------------------------------------
/*
- window functions
- enable us to grab or reference data from prior or subsequent rows
- useful for finding change over time - useful for pulling data from a row into a current row to perform calculations

EXAMPLE: how many days between transactions do customers have?

*/

create temp table cust_trans as (
select
  distinct 
  customer_id,
  transaction_id,
  transaction_date
  
from 
  grocery_db.transactions
  
where 
  customer_id in (1,2)
);

select * from cust_trans;

select
  *,
  -- the LAG gets the prior row (prior row defined by second lag input)
  -- LEAD gets later rows of data (later row defined by second lead input)
    -- ORDER BY is important here 
  lag(transaction_date,1) over (partition by customer_id order by transaction_date, transaction_id) as transaction_date_lag1,
  lag(transaction_date,2) over (partition by customer_id order by transaction_date, transaction_id) as transaction_date_lag2,
  lead(transaction_date,1) over (partition by customer_id order by transaction_date, transaction_id) as transaction_date_lead

from cust_trans;

/*!! future bonus = see if I can come abck and count the number of days between transactions 

select
  *,
  count() over 
*/

-------------------------------------------------------------------
--  Rounding Data
-------------------------------------------------------------------

select
  *,
  round(sales_cost,1) as sales_cost_round_1,
  round(sales_cost,0) as sales_cost_round_0
  
from grocery_db.transactions

where 
  customer_id = 1;
 
-- can use neg numbers to round X places over to the left (weird...)

select
  *,
  round(sales_cost,-1) as sales_cost_round_down
  
from grocery_db.transactions

where 
  customer_id = 1;
  
-------------------------------------------------------------------
--  Random Sampling
-------------------------------------------------------------------

select
  *
  
from
  grocery_db.customer_details
  
order by
  random()
  
limit 
  100;

-------------------------------------------------------------------
--  Extracting parts of a date
-------------------------------------------------------------------

select
  distinct
  transaction_date,
  date_part('day',transaction_date) as day,
  date_part('month',transaction_date) as month,
  date_part('year',transaction_date) as year,
  date_part('dow',transaction_date) as dow
  
from
  grocery_db.transactions
  
order by
  transaction_date;

/* bonus make it say the day of the week in english
select
  distinct
  transaction_date,
  date_part('day',transaction_date) as day,
  date_part('month',transaction_date) as month,
  date_part('year',transaction_date) as year,
    case
      when date_part('dow',transaction_date) = 0 then 'Sunday'
      else date_part('dow',transaction_date) end as dow
  
from
  grocery_db.transactions
  
order by
  transaction_date;
*/

-------------------------------------------------------------------
--  Working with Scrings/Text
-------------------------------------------------------------------

select
  product_area_name,
  -- UPPER and LOWER are useful for when we want to analyze text - makes it more reliable for matches
  upper(product_area_name) as pan_upper,
  lower(product_area_name) as pan_lower,
  char_length(product_area_name) as pan_length,
  -- CONCATs (adds) text at the end of existing entries
  concat(product_area_name, ' - ', 'Department') as pan_concat,
  -- SUBSTRING: find what characters exist between certain positions in the text values
  substring(product_area_name,3,6) as pan_substring,
  -- REPEAT value in text column
  repeat(product_area_name,2) as pan_repeat
  
from
  grocery_db.product_areas;
