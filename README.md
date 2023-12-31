# AirQualityApp

## DESCRIPTION
This package consists of a web-based visualization tool designed to display pollution levels across various states in the United States. The main features include a map visualization (`index.html`) showing different pollutants by state and a detailed state-wise trend analysis (`state-trends.html`). The tool leverages D3.js for rendering geographical data and Chart.js for trend graphs. Users can interact with the map to select different pollutants and years, and view state-specific pollution trends through an interactive line chart.

## INSTALLATION
- **Prerequisites**: Ensure you have a modern web browser installed (e.g., Chrome, Firefox, Safari).
- **Cloning and Setup**: Clone this repository to your local machine.
- **Dependencies**: No additional installations are required as the project uses links for D3.js and Chart.js.

## EXECUTION
### Running the Tool:
1. Open the terminal and navigate to the `AirQualityApp` directory.
2. In this directory, run `python3 -m http.server 8000`.
3. Open a web browser and go to `http://localhost:8000` to view the application.
4. Use the controls on the page to select different pollutants and years.
5. Click on any state to view detailed pollution trends, which will redirect you to the `state-trends.html` page.
6. On the `state-trends.html` page, use the dropdown to select different pollution or demographic trends for the chosen state.
7. Explore different features such as pollutant selection, year range, and state-specific data.

## DEMO
https://youtu.be/49PTkt9q-OM