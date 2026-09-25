CREATE TABLE customers (
    customer_id BIGSERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE customer_features (
    feature_record_id BIGSERIAL PRIMARY KEY,
    customer_id BIGINT NOT NULL,
    eqpdays INTEGER,
    months INTEGER,
    change_mou DOUBLE PRECISION,
    totmrc_mean DOUBLE PRECISION,
    mou_mean DOUBLE PRECISION,
    avgqty DOUBLE PRECISION,
    asl_flag VARCHAR(20),
    change_rev DOUBLE PRECISION,
    hnd_price DOUBLE PRECISION,
    mou_cvce_mean DOUBLE PRECISION,
    avg3mou DOUBLE PRECISION,
    uniqsubs INTEGER,
    crclscod VARCHAR(20),
    refurb_new VARCHAR(20),
    totcalls INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
);