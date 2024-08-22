import schedule
import time
from controller.auth import tickle, get_auth_status

def main():
    run_tickle_periodically()

def run_tickle_periodically(): # Run tickle every minute to prevent session timeout, recommended by IBKR
    try:
        auth_status = get_auth_status()
        if not auth_status['authenticated']:
            print("Failed to get auth status or not authenticated, exiting function")
            return

        def job():
            try:
                tickle()
                print("Tickle executed successfully")
            except Exception as e:
                print(f"Error occurred during tickle: {e}")

        schedule.every(1).minutes.do(job)

        while True:
            schedule.run_pending()
            time.sleep(60)  # Sleep for 60 seconds (1 minute)

    except Exception as e:
        print(f"Error occurred while setting up tickle: {e}")


if __name__ == "__main__":
    main()