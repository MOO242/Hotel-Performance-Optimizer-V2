# Step 1 get the revenue by day for checked out reservations.
revenue_by_day = (
    read_table("FACT_RESERVATIONS")[
        read_table("FACT_RESERVATIONS")["booking_status"] == "Checked Out"
    ]
    .groupby(["check_in_date_key", "property_id"])["room_revenue"]
    .sum()
    .reset_index()
)


# Step 2 merge revenue by day to dim_date to get the yearly total_revenue.

yearly_total_revenue = (
    revenue_by_day.merge(
        read_table("dim_date")[["date_key", "year"]],
        how="left",
        left_on=["check_in_date_key"],
        right_on=["date_key"],
    )
    .groupby("year")["room_revenue"]
    .sum()
    .reset_index()
    .rename(columns={"room_revenue": "total_revenue"})
)


# Step 3 merge fact_room_inventory to dim_date to get the total_rooms_sold per year.

yearly_rooms_sold = (
    read_table("fact_room_inventory")
    .merge(read_table("dim_date")[["date_key", "year"]], on="date_key", how="left")
    .groupby("year")["rooms_sold"]
    .sum()
    .reset_index()
    .rename(columns={"rooms_sold": "total_rooms_sold"})
)


# Step 4 merge yearly_total_revenue to yearly_rooms_sold.

yearly_adr = yearly_revenue.merge(yearly_rooms_sold, on="year", how="inner")

yearly_adr["adr"] = yearly_adr["total_revenue"] / yearly_adr["total_rooms_sold"]

yearly_adr["YOY_GROWTH_PCT"] = (yearly_adr["adr"].pct_change() * 100).round(2)


print(yearly_adr[["year", "adr", "YOY_GROWTH_PCT"]])
