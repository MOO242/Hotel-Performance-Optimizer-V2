WITH source AS (
    SELECT *
    FROM {{ source('HPO_V2', 'FACT_RESERVATIONS') }}
)

SELECT *
FROM source