# avalanche_info

This project is designed to handle, process, and store avalanche-related data, including incidents, observations, and summaries. It integrates with external APIs to fetch avalanche data and stores it in a structured database for further analysis. Modularity and a Single point of access for scripts keep things organized and sane. This allows for me to continue to add functionality as needed such as other resources related to avalanches like weather and forecasts.  

---

## Features

- Fetch avalanche-related data from external APIs.
- Process and store avalanche incidents, observations, and summaries in a database.
- Handle spatial data (e.g., latitude/longitude) using `ST_GeomFromText` for geometry fields.
- Modular design for handling different types of avalanche data (e.g., incidents, fatal avalanches, weather, snowpack, etc).
- Error handling and logging for robust data processing. Utilizing try statements and error handling.
- Modularity also allows me to add data cleaning steps like adding the labeling of the forecasting region that the incident belonged to

---

## Project Structure

- Code set up to handle both fatal and nonfatal data as the strucutre of the response is different for both.
- Different data was collected which will then be standardized for further analysis
