# avalanche_info

This project is designed to handle, process, and store avalanche-related data, including incidents, observations, and summaries. It integrates with external APIs to fetch avalanche data and stores it in a structured database for further analysis.

---

## Features

- Fetch avalanche-related data from external APIs.
- Process and store avalanche incidents, observations, and summaries in a database.
- Handle spatial data (e.g., latitude/longitude) using `ST_GeomFromText` for geometry fields.
- Modular design for handling different types of avalanche data (e.g., incidents, non-fatal avalanches).
- Error handling and logging for robust data processing.

---

## Project Structure

- Code set up to handle both fatal and nonfatal data as the strucutre of the response is different for both.
- Different data was collected which will then be standardized for further analysis
