SELECT
{{dbt_utils.generate_surrogate_key(['room_id'])}} as room_key,
room_id,
room_class,
base_rate,
suite_flag,
premium_flag,
FROM {{ref('stg_rooms')}}
