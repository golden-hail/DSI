-------------------------------------------------------------------
--  UNION & UNION ALL
-------------------------------------------------------------------

-- UNIONS are used to append data WITHOUT DUPLICATES (filters those out)
  -- Unions need the same number of columns and same column data types

select product_area_name from grocery_db.product_areas where product_area_id in (1,2)
union
select product_area_name from grocery_db.product_areas where product_area_id in (4,5);

-- UNION ALL does NOT ignore duplicates
select product_area_name from grocery_db.product_areas where product_area_id in (1,2)
union all
select product_area_name from grocery_db.product_areas where product_area_id in (1,2)
union all
select product_area_name from grocery_db.product_areas where product_area_id in (1,2);
