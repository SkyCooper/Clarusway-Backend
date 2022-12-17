-- select count("InvoiceId") from "Invoice";
-- SELECT count(distinct("Composer")) FROM "Track";
-- SELECT "Name", min("Milliseconds") FROM "Track" group by "Name";
-- SELECT sum("Total") as fatura_toplam from "Invoice";
-- SELECT "Composer", count(*) FROM "Track" GROUP BY "Composer";
-- SELECT "Country", count(*) FROM "Customer" GROUP BY "Country";
-- SELECT "AlbumId", min("Milliseconds") FROM "Track" GROUP BY "AlbumId";
-- SELECT "BillingCountry", SUM("Total") 
-- FROM "Invoice" GROUP BY "BillingCountry";
SELECT "BillingCountry", SUM("Total") 
FROM "Invoice" GROUP BY "BillingCountry";







