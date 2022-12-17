-- Retrieve track id, track name, album id info of
-- the Album title ‘Faceless’. (use : Subquery)
SELECT "Track"."TrackId", "Track"."Name", "Track"."AlbumId"
FROM "Track"
WHERE "Track"."AlbumId" = (
	SELECT "AlbumId" FROM "Album" WHERE "Title" = 'Faceless');
	
-- JOIN İLE YAPILMASI;
SELECT "Track"."TrackId", "Track"."Name", "Track"."AlbumId"
FROM "Track" INNER JOIN "Album" ON "Track"."AlbumId" = "Album"."AlbumId"
WHERE "Album"."Title" = 'Faceless';

-- Retrieve track id, track name, album id info of the
-- Album title ‘Faceless’ and ‘Let There Be Rock’
SELECT "Track"."TrackId", "Track"."Name", "Track"."AlbumId"
FROM "Track"
WHERE "Track"."AlbumId" IN (
	SELECT "AlbumId" FROM "Album"
	WHERE "Title" = 'Faceless' or "Title" = 'Let There Be Rock');
-- 	WHERE "Title" IN ('Faceless', 'Let There Be Rock') );
-- böyle de yazılabilirdi,

-- JOIN İLE YAPILMASI;
SELECT "Track"."TrackId", "Track"."Name", "Track"."AlbumId"
FROM "Track" JOIN "Album" ON "Track"."AlbumId" = "Album"."AlbumId"
WHERE "Album"."Title" IN ('Faceless', 'Let There Be Rock');

-- 3 tabloyu birleştirmeye örnek;
-- genre'den name, track'tan name ve album'den title getiren sorguyu yazınız?

SELECT "Genre"."Name", "Track"."Name", "Album"."Title" 
FROM "Track" 
	JOIN "Genre" ON "Track"."GenreId" = "Genre"."GenreId"
		JOIN "Album" ON "Track"."AlbumId" = "Album"."AlbumId";


-- DDL KOMUTLARI,

DROP TABLE IF EXISTS leaves;
-- var ise sil, sonra oluştur.

CREATE TABLE leaves(
id Int,
employee_id int,
employee_name varchar(30),
hire_date DATE
);
-- refresh yapınca Tables içine oluştu.

-- drop tabloyu komple siler
-- truncate tablo içini siler, tablo kalır.

-- genre içine bir satır ekleme;
-- INSERT INTO "Genre" ("GenreId","Name") VALUES (26,'Arabesk');

-- Try to insert a record in albums table with an
-- ArtistID=10000 and AlbumID=347
-- INSERT INTO "Album" ("AlbumId" , "Title","ArtistId") VALUES (349, 'Simyaci', 10001);
-- INSERT INTO "Album" ("AlbumId" ,"ArtistId") VALUES (350, 'deneme', 101);


--tablo oluştur ve sil

-- DROP TABLE IF EXISTS vacation_plan;

CREATE TABLE vacation_plan
(place_id Int PRIMARY KEY,
country "varchar",
hotel_name "varchar",
employee_id int,
vacation_length int,
budget real
-- PRIMARY KEY (place_id)
);

-- var olan tabloya city sütünu ekle
ALTER TABLE vacation_plan
ADD city "varchar";

-- DROP TABLE vacation_plan;



















	