from configflow import ConfigFlow
import time

# Create a sample .env file
with open(".env", "w") as f:
    f.write("PORT=8080\nDEBUG=true")

# Initialize ConfigFlow with a .env file
config = ConfigFlow(".env")  # Assuming your library supports this

# Define a schema
schema = {"PORT": int, "DEBUG": str}

# Register a callback for changes
@config.on_change
def handle_update(changed_config):
    print(f"Config updated: {changed_config}")

# Load and validate the initial config
print("Initial config:", config.load(schema=schema))

# Start watching the .env file
config.watch()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    config.stop()
    print("Stopped watching")
