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

CREATE TABLE EDA.T8314_CADASTROS
(
    name VARCHAR(100),
    status VARCHAR(100),
    mothersName VARCHAR(100),
    federalId VARCHAR(100),
    profilePicUrl VARCHAR(100),
    lastLocationDate VARCHAR(100),
    username VARCHAR(100),
    gender VARCHAR(100),
    defaultInstallments VARCHAR(100),
    avgRating VARCHAR(100),
    gpsRadius VARCHAR(100),
    lat VARCHAR(100),
    lng VARCHAR(100),
    id1 VARCHAR(100),
    fee VARCHAR(100),
    days VARCHAR(100),
    address1 VARCHAR(100),
    number VARCHAR(100),
    address2 VARCHAR(100),
    neighborhood VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    zipCode VARCHAR(100),
    country VARCHAR(100),
    addressLat VARCHAR(100),
    addressLng VARCHAR(100),
    birthDate VARCHAR(100),
    createdDate VARCHAR(100),
    completedHelpies VARCHAR(100),
    inactive VARCHAR(100),
    training VARCHAR(100),
    instantJob VARCHAR(100),
    deleted VARCHAR(100),
    superHelper VARCHAR(100),
    eligibleInstantJob VARCHAR(100),
    helperSebrae VARCHAR(100),
    trainingScore VARCHAR(100),
    approvedDate VARCHAR(100)
)