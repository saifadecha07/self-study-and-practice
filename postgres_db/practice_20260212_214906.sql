-- Session: Reviewing docs before bed
-- Note: This took a while to debug, but it works now.

-- Source: PostgreSQL Official Docs
-- PostgreSQL UPDATE
UPDATE customers SET contact_name = 'Alfred Schmidt', city= 'Frankfurt' WHERE customer_id = 1;

-- DELETE
DELETE FROM customers WHERE customer_name='Alfreds Futterkiste';