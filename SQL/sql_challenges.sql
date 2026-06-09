select * from grocery_db.customer_details;
select * from grocery_db.transactions;
select * from grocery_db.campaign_data;
select * from grocery_db.product_areas;
select * from grocery_db.loyalty_scores;

-- SQL Challenge Week 1

select
  a.customer_id,
  a.credit_score,
  sum(b.sales_cost) as total_sales
  
from
  grocery_db.customer_details a
  inner join grocery_db.transactions b on a.customer_id = b.customer_id
  
where
  a.credit_score > 0.5 and
  b.transaction_date between '2020-09-01' and '2020-09-30'

group by
  a.customer_id,
  a.credit_score
  
having
  sum(b.sales_cost) > 100;
  
-- SQL Challenge Week 2
  
select
  b.product_area_name,
  sum(a.num_items) as total_items
  
from
  grocery_db.transactions a
  full join grocery_db.product_areas b on a.product_area_id = b.product_area_id
  
group by
  b.product_area_name

order by
  total_items desc
  
limit
  3;
  
-- SQL Challenge Week 3
select * from grocery_db.customer_details;

select
  count(customer_id) as customer_count
   
from
  grocery_db.customer_details
  
where
  gender = 'M' and
  distance_from_store between 3 and 4 and
  credit_score > 0.4;
  
-- SQL Challenge Week 4

-- get the first transaction from each customer 

create temp table arg as (

select
  customer_id,
  transaction_date,
  transaction_id,
  sum(sales_cost) as munnay

from
  grocery_db.transactions
  
group by
  customer_id,
  transaction_date,
  transaction_id
  
having
  sum(sales_cost) > 100
  
order by
  customer_id,
  transaction_date
  
);

drop table arg;

select
  *
from
  arg;
  -- join at the end to customer_details, and exxcldue the non-matches left join?>? 

-- Weekly Challenge 5

-- Weekly Challenge 6
select
  customer_id,
  count(distinct(product_area_id))as unique_product_areas
  
from
  grocery_db.transactions
  
group by
  customer_id
  
having
  count(distinct(product_area_id)) > 4;
  
-- Weekly Challenge 8 ## LEARN COELESCE

select
  *
  -- a.gender,
  -- avg(b.loyalty_score) as avg_loyalty_score
  
from
  grocery_db.customer_details a 
  full join grocery_db.loyalty_scores b on a.customer_id = b;
  
-- group by gender;
  
-- Weekly Challenge 12 
select
  gender,
  avg(credit_score) as avg_credit_score

from
  grocery_db.customer_details
  
where
  distance_from_store < 2
  
group by
  gender;
