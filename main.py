from DBconn.db_connection import conn
import HandleNonFatal.NonFatalScrape as HandleNonFatal
import HandleFatal.FatalScrape as HandleFatal


# scraping fatal incidents
# HandleFatal.handle_fatal(conn)


# scraping non-fatal incidents
HandleNonFatal.handle_non_fatal(conn)
