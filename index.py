from DBconn.db_connection import conn
import HandleNonFatal.HandleIncident as HandleNonFatal
import HandleFatal.web_scrape as HandleFatal


# scraping fatal incidents
HandleFatal.handle_fatal(conn)


# scraping non-fatal incidents
HandleNonFatal.handle_non_fatal(conn)
