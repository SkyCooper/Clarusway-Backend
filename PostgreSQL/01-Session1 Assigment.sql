-- 12 Aralık 2022, Pazartesi

-- Write a query that returns the track name using tracks table.
select "Name" from "Track";

-- Write a query that returns track name and its composer using tracks table.
select "Name", "Composer" from "Track";

-- Write a query that returns all columns of albums table.
select * from "Album";

-- Write a query that returns columns of tracks table.
select * from "Track";

-- Find the name of composers of each track using tracks table.
select "Name", "Composer" from "Track";

-- Write a query that return distinct AlbumId, MediaTypeId pair
select distinct "AlbumId", "MediaTypeId" from "Track";
select distinct ("AlbumId", "MediaTypeId") from "Track";

-- Find the track names of Jimi Hendrix.
select "Name", "Composer" from "Track" where "Composer" = 'Jimi Hendrix';

-- Find all the info of the invoices of which total amount is greater than $10.
select * from "Invoice" where "Total">10;

-- Find all the info of the invoices of which total amount is greater than $10. Just return the first 4
select * from "Invoice" where "Total">10 limit 4;

-- Find all the info of the invoices of which total amount is greater than $10.
-- Then sort them by the total amount in descending order.
select * from "Invoice" where "Total">10 order by "Total" desc;

-- Find all the info of the invoices of which billing country is not USA.
-- Then sort them by the total amount in ascending order.
select * from "Invoice" where "BillingCountry" <> 'USA' order by "Total" asc;

-- Find the newest invoice date among the invoice dates between 2009 and 2011.
SELECT * FROM "Invoice" WHERE "InvoiceDate" BETWEEN '2009-01-01' AND '2011-12-31' ORDER BY "InvoiceDate" ASC;


-- Find the first and last name of the customers who gave an order from Belgium, Norway, Canada and USA.
SELECT	"FirstName", "LastName", "Country" FROM	"Customer" WHERE "Country" IN ('Belgium', 'Norway', 'Canada', 'USA');


-- Find the track names of Bach.
select "Name", "Composer" from "Track" where "Composer" like '%Bach%';



























