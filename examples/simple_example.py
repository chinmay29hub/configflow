from configflow import ConfigFlow
import time

# Create a sample config file
with open("sample.yaml", "w") as f:
    f.write("port: 8080\ndebug: true")

# Initialize ConfigFlow
config = ConfigFlow("sample.yaml")

# Define a schema
schema = {"port": int, "debug": bool}


# Register a callback
@config.on_change
def handle_update(changed_config):
    print(f"Config updated: {changed_config}")


# Load and validate
print("Initial config:", config.load(schema=schema))

# Start watching
config.watch()

try:
    # Keep the script running
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    config.stop()
    print("Stopped watching")
