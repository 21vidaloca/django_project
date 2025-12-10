@ECHO OFF

IF EXIST fisier.sql DEL fisier.sql
SET PGPASSWORD=david

ECHO Realizam procesarea tabelelor


(FOR %%t IN ("aplicatie_brand" "aplicatie_caracteristici" "aplicatie_ceasuri" "aplicatie_ceasuri_caracteristici" "aplicatie_curea" "aplicatie_mecanism" "aplicatie_oferta") DO (
    ECHO Tabelul %%t

    pg_dump --column-inserts --data-only --inserts -h localhost -U david -p 5432 -d dj2025 -t %%t >> fisier.sql 2>> erori.txt
))

SET PGPASSWORD=

