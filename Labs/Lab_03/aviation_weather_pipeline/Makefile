.PHONY: all fetch analyze clean

analyze: fetch
	@echo "Starting analyze. Reading JSON from raw_metars -> weather_report.csv"
	./analyze_data.sh
	@echo "Finished analyze. Results are in weather_report.csv. Pipeline completed succcessfuly!"

fetch:
	@echo "Starting fetch. Saving METAR data in raw_metars"
	./fetch_metars.sh
	@echo "Finished fetch. Results are in raw_metars."

clean:
	@echo "Starting clean. Removing weather_report.csv and raw_metars"
	rm -rf weather_report.csv raw_metars
	@echo "Finished clean." 

all: analyze
