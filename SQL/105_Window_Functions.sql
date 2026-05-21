-------------------------------------------------------------------
-- WINDOW FUNCTIONS
-------------------------------------------------------------------
-- Def: logic that opperates on a set of rows, where the set of rows is known as the "window", it then returns a value onto those rows
  -- key word OVER, then you need a partition
  

-- WINDOW FUNCTION
  -- Example: create a new column to show the total $$$ [sum(sales_cost)] spent within each transaction
    -- THEN, find the percentage of $$$ spent on each product area for each customer transaction 
select
  *,
  sum(sales_cost) over (partition by transaction_id) as transaction_total_sales,
  sales_cost / sum(sales_cost) over (partition by transaction_id) as transaction_sales_percent
  
from
  grocery_db.transactions;

-- ROW NUMBER & RANK
  -- useful for adding ordered row numbers, or ranking rows based on some criteria 
  -- and useful for putting row values into deciles or percentiles 
  
/* 
-- ROW_NUMBER: will give a unique value to each row of data in the set *even* if there are ties in the order by logic

100m time     output
  10s           1
  10s           2
  10s           3
  11s           4  
  12s           5
*/

select
  *,
  row_number() over (partition by customer_id order by transaction_date, transaction_id) as transaction_number

from
  grocery_db.transactions;

/* 
-- RANK
will give ties the same value, then skip to the next value in terms of the number of rows it has seen

100m time     output
  10s           1
  10s           1
  10s           1
  11s           4  
  12s           5
*/

select
  *,
  rank() over (partition by customer_id order by transaction_date, transaction_id) as transaction_number

from
  grocery_db.transactions;

/*
-- DENSE_RANK
will do the same as RANK, but will go to the next number in sequence after any ties
100m time     output
  10s           1
  10s           1
  10s           1
  11s           2  
  12s           3
*/

select
  *,
  dense_rank() over (partition by customer_id order by transaction_date, transaction_id) as transaction_number

from
  grocery_db.transactions;
  
-- NTILE - for deciles/percentiles etc
  -- put data into groups based on some criteria we set
  -- Example: use CASE-WHEN example of hardcoding distances to categorize shoppers, but create equally sized groups (not hardcoded distances)
  
select
  customer_id,
  customer_loyalty_score,
  ntile(3) over (order by customer_loyalty_score desc) as loyalty_category,
  ntile(10) over (order by customer_loyalty_score desc) as loyalty_category2
  
from
  grocery_db.loyalty_scores;
  
/* PRACTICE:
You have been tasked with ranking customers in terms of their distance from the store.

We only want to rank customers who have a distance_from_store value present in the data, and for those who have a gender value of 'M' or 'F'

The criteria for the ranking are:

Ranking will be in ascending order (i.e. rank 1 would be for the customer who is closest to the store)
Rankings will be split (hint: partitioned) by gender
In the case of tied rankings, we want the subsequent ranking to represent the number of rows seen rather than purely the next number (i.e. 1,1,1,4 rather than 1,1,1,2)


Your query will return four columns:

customer_id
gender
distance_from_store
distance_from_store_rank (you will create this)


Which table contains this information?

What SQL code would you need to achieve this?
*/

select
  customer_id,  
  gender,
  distance_from_store,
  rank() over (partition by gender order by distance_from_store) as distance_from_store_rank
  
from
  grocery_db.customer_details
  
where
  distance_from_store is not null and
  gender in ('M','F');

