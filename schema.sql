CREATE TABLE company (
  id INTEGER PRIMARY KEY,
  name VARCHAR(100) NOT NULL
);

CREATE TABLE warehouse (
  id INTEGER PRIMARY KEY,
  name VARCHAR(100),
  company_id INTEGER,
  FOREIGN KEY (company_id) REFERENCES company(id)
);

CREATE TABLE product (
  id INTEGER PRIMARY KEY,
  name VARCHAR(100),
  sku VARCHAR(50) UNIQUE,
  low_stock_threshold INTEGER
);

CREATE TABLE inventory (
  id INTEGER PRIMARY KEY,
  product_id INTEGER,
  warehouse_id INTEGER,
  quantity INTEGER,
  FOREIGN KEY (product_id) REFERENCES product(id),
  FOREIGN KEY (warehouse_id) REFERENCES warehouse(id)
);

CREATE TABLE supplier (
  id INTEGER PRIMARY KEY,
  name VARCHAR(100),
  contact_email VARCHAR(100)
);
