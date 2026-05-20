-------------------------------------------------------------------
-- PART 2: APPLYING SELECTION  CONDITIONS USING THE WHERE STATEMENT 
-------------------------------------------------------------------

-- THE WHERE STATEMENT
select
  *
  
from
  grocery_db.customer_details
  
where
  distance_from_store < 2;
  
-- MULTIPLE CONDITIONS 

--- and
select
  *
  
from
  grocery_db.customer_details
  
where
  distance_from_store < 2 or
  gender = 'M';

--- or
select
  *
  
from
  grocery_db.customer_details
  
where
  distance_from_store < 2 and
  gender = 'M';
  
--- OTHER OPERATORS

/*
Equal to =
Not equal to <>
Greater than/Less than/Equal < > <=
Between between
*/

select
  *
  
from 
  grocery_db.campaign_data;
  
-- in
select
  *
  
from 
  grocery_db.campaign_data

where
  mailer_type in ('Mailer1', 'Mailer2');

-- like (IE. CONTAINS)
select
  *
  
from 
  grocery_db.campaign_data

where
  mailer_type like '%Mailer%';
  
-- further notes about the string search with LIKE statement:
/* '%Mailer%' will flag and display cells from the column that contain the phrase "Mailer"
if we searched '%Mailer', it would only flag/display columns that end in 'Mailer'
if we searched 'Mailer%', it would only flag/display columns that start with 'Mailer'
*/

-- EXAMPLE --
 
select 
  customer_id,
  distance_from_store,
  gender
  
from grocery_db.customer_details

where distance_from_store <= 0.5 and
gender in ('M','F');
