CREATE TABLE "Imovel"(
    "id" INTEGER NOT NULL,
    "Logradouro" geography(LINESTRING, 4326) NOT NULL,
    "CEP" INTEGER NOT NULL,
    "Bairro" geography(LINESTRING, 4326) NOT NULL,
    "Cidade" geography(LINESTRING, 4326) NOT NULL,
    "Numero_End" INTEGER NULL,
    "id_Proprietário" INTEGER NOT NULL
);
ALTER TABLE
    "Imovel" ADD PRIMARY KEY("id");
CREATE TABLE "Aluguel"(
    "id" INTEGER NOT NULL,
    "id_Imovel" INTEGER NOT NULL,
    "id_Inquilino" INTEGER NOT NULL
);
ALTER TABLE
    "Aluguel" ADD PRIMARY KEY("id");
CREATE TABLE "Inquilino"(
    "id" INTEGER NOT NULL,
    "Nome" geography(LINESTRING, 4326) NOT NULL,
    "Data_nascimento" DATE NOT NULL,
    "Renda_mensal" INTEGER NOT NULL
);
ALTER TABLE
    "Inquilino" ADD PRIMARY KEY("id");
CREATE TABLE "Proprietario"(
    "id" INTEGER NOT NULL,
    "Nome" geography(LINESTRING, 4326) NOT NULL,
    "Data_nascimento" DATE NOT NULL,
    "Único" BOOLEAN NOT NULL
);
ALTER TABLE
    "Proprietario" ADD PRIMARY KEY("id");
ALTER TABLE
    "Imovel" ADD CONSTRAINT "imovel_id_proprietário_foreign" FOREIGN KEY("id_Proprietário") REFERENCES "Proprietario"("id");
ALTER TABLE
    "Aluguel" ADD CONSTRAINT "aluguel_id_imovel_foreign" FOREIGN KEY("id_Imovel") REFERENCES "Imovel"("id");
ALTER TABLE
    "Aluguel" ADD CONSTRAINT "aluguel_id_inquilino_foreign" FOREIGN KEY("id_Inquilino") REFERENCES "Inquilino"("id");