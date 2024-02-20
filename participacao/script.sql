CREATE TABLE clientes (
  id SERIAL PRIMARY KEY,
  limite integer DEFAULT 0,
  saldo integer DEFAULT 0,
);

DO $$
BEGIN
  INSERT INTO clientes (id, limite)
  VALUES
    (1, 1000 * 100),
    (2, 800 * 100),
    (3, 10000 * 100),
    (4, 100000 * 100),
    (5, 5000 * 100);
END; $$
