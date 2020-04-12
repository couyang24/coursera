def locator(df, postal_code, country_code):
    import pgeocode
    import pandas

    nomi = pgeocode.Nominatim(country_code)
    df['lat'] = df[postal_code].apply(lambda x:nomi.query_postal_code(x).latitude)
    df['lng'] = df[postal_code].apply(lambda x:nomi.query_postal_code(x).longitude)

    return df
