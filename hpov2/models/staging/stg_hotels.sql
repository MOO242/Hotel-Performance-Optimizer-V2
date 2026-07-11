WITH source AS (
    SELECT *
    FROM {{ source('HPO_V2', 'RAW_DIM_HOTELS') }}
)
SELECT *
FROM source