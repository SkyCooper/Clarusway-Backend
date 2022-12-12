-- select count("InvoiceId") from "Invoice";

-- SELECT count(distinct("Composer")) FROM "Track";

SELECT "Name", min("Milliseconds") FROM "Track" group by "Name";

