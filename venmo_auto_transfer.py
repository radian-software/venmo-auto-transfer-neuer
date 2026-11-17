import os
import sys

import dotenv
import venmo_auto_cashout

dotenv.load_dotenv()

TRANSACTIONS_DB = os.environ["TRANSACTIONS_DB"]
VENMO_ACCESS_TOKEN = os.environ["VENMO_ACCESS_TOKEN"]

sys.argv[1:] = [
    f"--token={VENMO_ACCESS_TOKEN}",
    f"--transaction-db={TRANSACTIONS_DB}",
    "--allow-remaining",
]
venmo_auto_cashout.run_cli()
