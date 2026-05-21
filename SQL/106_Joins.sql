-------------------------------------------------------------------
-- JOINING TABLES
-------------------------------------------------------------------

select * from grocery_db.customer_details;
select * from grocery_db.loyalty_scores;

-- **INNER JOIN 
  -- ** only returns rows where the values in the joining column is found in both tables **
  -- in "from" state the tables of interest.
  -- give them each an identifier (example: a and b) 
  -- select column to join them on

select
  a.*,
  b.customer_loyalty_score

from
  grocery_db.customer_details a
  inner join grocery_db.loyalty_scores b on a.customer_id = b.customer_id;

-- **LEFT JOIN 
  -- **returns all rows from the first table and then the info that can be tagged on is, when there's no data, it comes out as blanks**
  -- RIGHT JOIN is about the same but it joins b to a instead of a to b

select
  a.*,
  b.customer_loyalty_score

from
  grocery_db.customer_details a
  left join grocery_db.loyalty_scores b on a.customer_id = b.customer_id;

-- ADDING OTHER LOGIC

select
  a.*,
  b.customer_loyalty_score

from
  grocery_db.customer_details a
  left join grocery_db.loyalty_scores b on a.customer_id = b.customer_id

where
  customer_loyalty_score > 0.5;

-- JOINING MULTIPLE TABLES

select
  a.*,
  b.customer_loyalty_score,
  c.product_area_name

from
  grocery_db.transactions a
  left join grocery_db.loyalty_scores b on a.customer_id = b.customer_id
  inner join grocery_db.product_areas c on a.product_area_id = c.product_area_id; 

-- OTHER JOIN TYPES
  -- a temp table will be created for these examples - this will exist until we break the connection, in memory 

    -- create table 1
create temp table table1 (
                   id char(1),
                   t1_col1 int,
                   t1_col2 int);

insert into table1 values ('A',1,1), ('B',1,1);

select * from table1;

      -- create table 2
create temp table table2 (
                   id char(1),
                   t2_col1 int,
                   t2_col2 int);

insert into table2 values ('A',2,2), ('C',2,2);

select * from table2;

      -- inner join with new tables
      
      select
        a.id as id_t1,
        a.t1_col1,
        a.t1_col2,
        b.id as id_t2,
        b.t2_col1,
        b.t2_col2
  
      from
        table1 a
        inner join table2 b on a.id = b.id;

      -- left join with new tables (notice the blank values)
      
      select
        a.id as id_t1,
        a.t1_col1,
        a.t1_col2,
        b.id as id_t2,
        b.t2_col1,
        b.t2_col2
  
      from
        table1 a
        left join table2 b on a.id = b.id;
        
-- OUTER JOIN
  -- left join and right join at the same time

select
  a.id as id_t1,
  a.t1_col1,
  a.t1_col2,
  b.id as id_t2,
  b.t2_col1,
  b.t2_col2
  
from
  table1 a
  full outer join table2 b on a.id = b.id;

-- CROSS JOIN *RARE USE CASE*
  -- useful if you want to populate all combos of 2 datasets
  -- all combo of products to show frequency of when purchased together
  
select
  a.id as id_t1,
  a.t1_col1,
  a.t1_col2,
  b.id as id_t2,
  b.t2_col1,
  b.t2_col2
  
from
  table1 a
  cross join table2 b;
  
/*TEST
A stakeholder wants to analyze the relationship between credit score and customer loyalty - so we need to provide them with this data.

Extract a list of customers, along with their credit score, and their customer loyalty score.

Important: The stakeholder only wants to analyze customers that do have a customer loyalty score present in our data)

Your query will return three columns:

customer_id
credit_score
customer_loyalty_score


Which tables do we need for this?

What SQL code would you need to achieve this?

Give it a go, and then scroll down for the answer!
*/

select
  a.customer_id,
  a.credit_score,
  b.customer_loyalty_score
  
from
  grocery_db.customer_details a
  inner join grocery_db.loyalty_scores b on a.customer_id = b.customer_id;
  
-- where customer_loyalty is not null <- don't need this statement with an inner join 
