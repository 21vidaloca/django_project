--
-- PostgreSQL database dump
--

\restrict Hh5EdGb1AMG8l88STVsaLqOnXotm8KCXfnkmCJ05dmSlHuBbQhS17DVf6AXFQkV

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatie_brand; Type: TABLE DATA; Schema: django; Owner: david
--

INSERT INTO django.aplicatie_brand (id, nume_brand, tara_origine, an_infiintare, culoare, imagine) VALUES (9, 'audemars', '', NULL, 'argintiu', 'imagini_branduri/prn15-audemars-piguet-logo-1y-2high.jpg');
INSERT INTO django.aplicatie_brand (id, nume_brand, tara_origine, an_infiintare, culoare, imagine) VALUES (7, 'atlantic', '', NULL, 'argintiu', 'imagini_branduri/The-Atlantic-logo-vector.svg.png');
INSERT INTO django.aplicatie_brand (id, nume_brand, tara_origine, an_infiintare, culoare, imagine) VALUES (6, 'fossil', '', NULL, 'argintiu', 'imagini_branduri/2023_FOSSIL_LOGO_Logo.jpg');
INSERT INTO django.aplicatie_brand (id, nume_brand, tara_origine, an_infiintare, culoare, imagine) VALUES (5, 'diesel', '', NULL, 'argintiu', 'imagini_branduri/diesel-logo.png');
INSERT INTO django.aplicatie_brand (id, nume_brand, tara_origine, an_infiintare, culoare, imagine) VALUES (4, 'rolex', '', NULL, 'argintiu', 'imagini_branduri/Logo_da_Rolex.png');
INSERT INTO django.aplicatie_brand (id, nume_brand, tara_origine, an_infiintare, culoare, imagine) VALUES (3, 'seiko', 'japonia', 1940, 'argintiu', 'imagini_branduri/Seiko-Logo-1-1024x1024.jpg');
INSERT INTO django.aplicatie_brand (id, nume_brand, tara_origine, an_infiintare, culoare, imagine) VALUES (2, 'orient', 'japonia', 1901, 'argintiu', 'imagini_branduri/orient.png');
INSERT INTO django.aplicatie_brand (id, nume_brand, tara_origine, an_infiintare, culoare, imagine) VALUES (1, 'casio', 'japonia', 1946, 'argintiu', 'imagini_branduri/casio.png');
INSERT INTO django.aplicatie_brand (id, nume_brand, tara_origine, an_infiintare, culoare, imagine) VALUES (11, 'apple', '', NULL, '#000000', 'imagini_branduri/Apple.png');
INSERT INTO django.aplicatie_brand (id, nume_brand, tara_origine, an_infiintare, culoare, imagine) VALUES (8, 'hublot', '', NULL, '#000000', 'imagini_branduri/Hublot-logo.png');
INSERT INTO django.aplicatie_brand (id, nume_brand, tara_origine, an_infiintare, culoare, imagine) VALUES (10, 'tissot', '', NULL, '#FFD700', 'imagini_branduri/Tissot-Logo.png');


--
-- Name: aplicatie_brand_id_seq; Type: SEQUENCE SET; Schema: django; Owner: david
--

SELECT pg_catalog.setval('django.aplicatie_brand_id_seq', 11, true);


--
-- PostgreSQL database dump complete
--

\unrestrict Hh5EdGb1AMG8l88STVsaLqOnXotm8KCXfnkmCJ05dmSlHuBbQhS17DVf6AXFQkV

--
-- PostgreSQL database dump
--

\restrict 0fQpdI3fYafPrtpRLDgIT0duGSjgkFDGvufuh3fojKlA7ra6RQNUI2Xn96ZnxPI

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatie_caracteristici; Type: TABLE DATA; Schema: django; Owner: david
--

INSERT INTO django.aplicatie_caracteristici (id, nume, descriere) VALUES (1, 'digital', 'abcdefg');
INSERT INTO django.aplicatie_caracteristici (id, nume, descriere) VALUES (2, 'analog', 'abdefg');


--
-- Name: aplicatie_caracteristici_id_seq; Type: SEQUENCE SET; Schema: django; Owner: david
--

SELECT pg_catalog.setval('django.aplicatie_caracteristici_id_seq', 2, true);


--
-- PostgreSQL database dump complete
--

\unrestrict 0fQpdI3fYafPrtpRLDgIT0duGSjgkFDGvufuh3fojKlA7ra6RQNUI2Xn96ZnxPI

--
-- PostgreSQL database dump
--

\restrict c4dtpAHUgwBgEDVRvYhJpZMT8ftkThYmIVB2E1WaUPxWn7r3pleEc86kg8KhI7x

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatie_ceasuri; Type: TABLE DATA; Schema: django; Owner: david
--

INSERT INTO django.aplicatie_ceasuri (id, nume_model, stoc, tip_geam, diametru_carcasa, pret, brand_id, curea_id, mecanism_id, oferta_id, poza) VALUES (13, 'hublot', 50, 'safir', 32, 3000.00, 8, NULL, NULL, NULL, 'imagini_ceasuri/hub.png');
INSERT INTO django.aplicatie_ceasuri (id, nume_model, stoc, tip_geam, diametru_carcasa, pret, brand_id, curea_id, mecanism_id, oferta_id, poza) VALUES (8, 'rolex', 15, 'safir', 35, 1500.00, 4, NULL, NULL, NULL, 'imagini_ceasuri/Rolex-Datejust-41mm.jpg');
INSERT INTO django.aplicatie_ceasuri (id, nume_model, stoc, tip_geam, diametru_carcasa, pret, brand_id, curea_id, mecanism_id, oferta_id, poza) VALUES (12, 'audemars', 45, 'safir', 40, 1200.00, 9, NULL, NULL, NULL, 'imagini_ceasuri/aud.jpg');
INSERT INTO django.aplicatie_ceasuri (id, nume_model, stoc, tip_geam, diametru_carcasa, pret, brand_id, curea_id, mecanism_id, oferta_id, poza) VALUES (5, 'seiko', 100, 'safir', 40, 1200.00, 3, NULL, NULL, NULL, 'imagini_ceasuri/seik.png');
INSERT INTO django.aplicatie_ceasuri (id, nume_model, stoc, tip_geam, diametru_carcasa, pret, brand_id, curea_id, mecanism_id, oferta_id, poza) VALUES (7, 'orient', 50, 'safir', 40, 800.00, 2, NULL, NULL, NULL, 'imagini_ceasuri/or.jpg');
INSERT INTO django.aplicatie_ceasuri (id, nume_model, stoc, tip_geam, diametru_carcasa, pret, brand_id, curea_id, mecanism_id, oferta_id, poza) VALUES (10, 'fossil', 50, 'safir', 30, 700.00, 6, NULL, NULL, NULL, 'imagini_ceasuri/fos.jpg');
INSERT INTO django.aplicatie_ceasuri (id, nume_model, stoc, tip_geam, diametru_carcasa, pret, brand_id, curea_id, mecanism_id, oferta_id, poza) VALUES (14, 'atlantic', 35, 'plastic', 32, 500.00, 7, NULL, NULL, NULL, 'imagini_ceasuri/atl.jpg');
INSERT INTO django.aplicatie_ceasuri (id, nume_model, stoc, tip_geam, diametru_carcasa, pret, brand_id, curea_id, mecanism_id, oferta_id, poza) VALUES (11, 'tissot', 25, 'safir', 40, 400.00, 10, NULL, NULL, NULL, 'imagini_ceasuri/ceas-tissot-tradition-t0636101103700_9875_1_1623243142.jpg');
INSERT INTO django.aplicatie_ceasuri (id, nume_model, stoc, tip_geam, diametru_carcasa, pret, brand_id, curea_id, mecanism_id, oferta_id, poza) VALUES (9, 'diesel', 500, 'plastic', 50, 400.00, 5, NULL, NULL, NULL, 'imagini_ceasuri/215177-dieselmegachiefchronographbluedialgunmetalionplatedmenswatch.jpg');
INSERT INTO django.aplicatie_ceasuri (id, nume_model, stoc, tip_geam, diametru_carcasa, pret, brand_id, curea_id, mecanism_id, oferta_id, poza) VALUES (16, 'casio vintage', 20, 'plastic', 30, 300.00, 1, NULL, NULL, NULL, 'imagini_ceasuri/cas.jpg');
INSERT INTO django.aplicatie_ceasuri (id, nume_model, stoc, tip_geam, diametru_carcasa, pret, brand_id, curea_id, mecanism_id, oferta_id, poza) VALUES (6, 'casio', 100, 'plastic', 30, 300.00, 1, NULL, NULL, NULL, 'imagini_ceasuri/casio-mtp-v006l-7cudf7761710.jpg');


--
-- Name: aplicatie_ceasuri_id_seq; Type: SEQUENCE SET; Schema: django; Owner: david
--

SELECT pg_catalog.setval('django.aplicatie_ceasuri_id_seq', 16, true);


--
-- PostgreSQL database dump complete
--

\unrestrict c4dtpAHUgwBgEDVRvYhJpZMT8ftkThYmIVB2E1WaUPxWn7r3pleEc86kg8KhI7x

--
-- PostgreSQL database dump
--

\restrict CosHDHEh0A1hFb8QljLvFoBfdvRCl9lDxjgvjDzOveX18zaup0pwqPQ2jqFHFtT

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatie_ceasuri_caracteristici; Type: TABLE DATA; Schema: django; Owner: david
--



--
-- Name: aplicatie_ceasuri_caracteristici_id_seq; Type: SEQUENCE SET; Schema: django; Owner: david
--

SELECT pg_catalog.setval('django.aplicatie_ceasuri_caracteristici_id_seq', 1, false);


--
-- PostgreSQL database dump complete
--

\unrestrict CosHDHEh0A1hFb8QljLvFoBfdvRCl9lDxjgvjDzOveX18zaup0pwqPQ2jqFHFtT

--
-- PostgreSQL database dump
--

\restrict h8RfoNQeuVNfFcQsQ1ujekTMghqQDIvdeUBHDHkYR2sBwc6GK7WlahkeeN2LIcC

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatie_curea; Type: TABLE DATA; Schema: django; Owner: david
--

INSERT INTO django.aplicatie_curea (id, material_curea, latime_curea, culoare) VALUES (1, 'piele', 20, 'maro');
INSERT INTO django.aplicatie_curea (id, material_curea, latime_curea, culoare) VALUES (2, 'fibra', 15, 'negru');
INSERT INTO django.aplicatie_curea (id, material_curea, latime_curea, culoare) VALUES (3, 'inox', 12, 'argintiu');


--
-- Name: aplicatie_curea_id_seq; Type: SEQUENCE SET; Schema: django; Owner: david
--

SELECT pg_catalog.setval('django.aplicatie_curea_id_seq', 3, true);


--
-- PostgreSQL database dump complete
--

\unrestrict h8RfoNQeuVNfFcQsQ1ujekTMghqQDIvdeUBHDHkYR2sBwc6GK7WlahkeeN2LIcC

--
-- PostgreSQL database dump
--

\restrict ZOrOkUVvM3Zx5R8Jp4wUl6Rw6Rw6M3wy2gwSO1pqN608QAbcIGhSQE7LsXHBook

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatie_mecanism; Type: TABLE DATA; Schema: django; Owner: david
--

INSERT INTO django.aplicatie_mecanism (id, tip_mecanism, frecventa, precizie) VALUES (1, 'MEC', '1200', '3');
INSERT INTO django.aplicatie_mecanism (id, tip_mecanism, frecventa, precizie) VALUES (2, 'QRT', '1000', '5');
INSERT INTO django.aplicatie_mecanism (id, tip_mecanism, frecventa, precizie) VALUES (3, 'AUT', '2000', '1');


--
-- Name: aplicatie_mecanism_id_seq; Type: SEQUENCE SET; Schema: django; Owner: david
--

SELECT pg_catalog.setval('django.aplicatie_mecanism_id_seq', 3, true);


--
-- PostgreSQL database dump complete
--

\unrestrict ZOrOkUVvM3Zx5R8Jp4wUl6Rw6Rw6M3wy2gwSO1pqN608QAbcIGhSQE7LsXHBook

--
-- PostgreSQL database dump
--

\restrict aGSDuftNcf0tnZhxM3qj6RZ6bVfPIYO71ftnK7ApnIpbWb3BsevPCaQUePeCBxz

-- Dumped from database version 18.0
-- Dumped by pg_dump version 18.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: aplicatie_oferta; Type: TABLE DATA; Schema: django; Owner: david
--

INSERT INTO django.aplicatie_oferta (id, nume_oferta, data_inceput, data_sfarsit, cod_reducere) VALUES (1, 'Promotie', '2025-10-30 10:18:55.685694+02', '2025-10-30 10:18:44+02', 'IEFTIN');
INSERT INTO django.aplicatie_oferta (id, nume_oferta, data_inceput, data_sfarsit, cod_reducere) VALUES (2, 'Promotie', '2025-10-30 10:34:02.677898+02', '2025-10-30 10:33:53+02', 'REDUCERE50');


--
-- Name: aplicatie_oferta_id_seq; Type: SEQUENCE SET; Schema: django; Owner: david
--

SELECT pg_catalog.setval('django.aplicatie_oferta_id_seq', 2, true);


--
-- PostgreSQL database dump complete
--

\unrestrict aGSDuftNcf0tnZhxM3qj6RZ6bVfPIYO71ftnK7ApnIpbWb3BsevPCaQUePeCBxz

