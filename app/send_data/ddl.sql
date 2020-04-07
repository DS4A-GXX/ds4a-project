-- IPEA 
-- SERCODIGO;VALDATA;VALVALOR;NIVNOME;TERCODIGO
CREATE TABLE EDA.IPEA
(
    SERCODIGO VARCHAR(20),
    VALDATA TIMESTAMP,
    VALVALOR double precision,
    NIVNOME VARCHAR(100),
    TERCODIGO VARCHAR(30),
    CREATED_ON TIMESTAMP NOT NULL,
    UPDATED_ON TIMESTAMP NOT NULL DEFAULT current_timestamp
)


CREATE TABLE EDA.IPEA_TERRITORIOS
(
    NIVNOME VARCHAR(50),
    TERCODIGO VARCHAR(30),
    TERNOME VARCHAR(50),
    TERNOMEPADRAO VARCHAR(100),
    TERCAPITAL BOOLEAN,
    TERAREA double precision,
    NIVAMC BOOLEAN
)