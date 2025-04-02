from DBconn.db_connection import conn
import HandleNonFatal.NonFatalScrape as HandleNonFatal
import HandleFatal.FatalScrape as HandleFatal
import ForecastAreaLabel.ForecastLabel as ForecastLabel


# scraping fatal incidents
# HandleFatal.handle_fatal(conn)


# scraping non-fatal incidents
# HandleNonFatal.handle_non_fatal(conn)

# labeling the locations with the forecast area they are in
ForecastLabel.label_forecast_area(conn)
