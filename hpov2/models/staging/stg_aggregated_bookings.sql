WITH source AS (
    SELECT *
    FROM {{ source('HPO_V2', 'RAW_FACT_AGGREGATED_BOOKINGS') }}
)

SELECT *
FROM source