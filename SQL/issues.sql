select
  a.customer_id
  
from
  grocery_db.transactions a
  left join grocery_db.transactions b on a.product_area_id = b.product_area_id;
