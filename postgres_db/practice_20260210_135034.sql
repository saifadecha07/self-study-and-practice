-- Session: Late night coding
-- Note: W3Schools explanation is really clear.

-- Source: PostgreSQL Official Docs
-- PostgreSQL UPDATE
UPDATE customers SET contact_name = 'Alfred Schmidt', city= 'Frankfurt' WHERE customer_id = 1;

-- DELETE
DELETE FROM customers WHERE customer_name='Alfreds Futterkiste';