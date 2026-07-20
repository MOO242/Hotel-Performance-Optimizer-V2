WITH source AS (
    SELECT *
    FROM {{ source('HPO_V2', 'DIM_HOTELS') }}
)
SELECT *
FROM source