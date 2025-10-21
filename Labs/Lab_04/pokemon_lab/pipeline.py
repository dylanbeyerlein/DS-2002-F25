import sys
from update_portfolio import main as update_portfolio_main
from generate_summary import main as generate_summary_main


def run_production_pipeline():
    print("Running production pipeline.", file=sys.stderr)
    print("ETL Step: updating portfolio...", file=sys.stderr)
    update_portfolio_main()
    print("Reporting Step: generating summary...", file=sys.stderr)
    generate_summary_main()
    print("Successfully completed production pipeline.", file=sys.stderr)


if __name__ == "__main__":
    run_production_pipeline()
