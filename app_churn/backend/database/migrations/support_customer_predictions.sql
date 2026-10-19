ALTER TABLE predictions
ALTER COLUMN encounter_id
DROP NOT NULL;

ALTER TABLE predictions
ADD COLUMN customer_id BIGINT;

ALTER TABLE predictions ADD CONSTRAINT fk_prediction_customer FOREIGN KEY (customer_id) REFERENCES customers (customer_id);

ALTER TABLE predictions ADD CONSTRAINT prediction_entity_check CHECK (
    (
        encounter_id IS NOT NULL
        AND customer_id IS NULL
    )
    OR (
        encounter_id IS NULL
        AND customer_id IS NOT NULL
    )
);