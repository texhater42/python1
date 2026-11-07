import subprocess


def check_service_status(service_name):
    try:
        # Run 'systemctl is-active <service_name>' to check status cleanly
        result = subprocess.run(
            ["systemctl", "is-active", service_name],
            capture_output=True,
            text=True,
            check=False,  # Don't crash if the service is stopped (returns non-zero)
        )

        status = result.stdout.strip()

        if status == "active":
            print(f"✅ The service '{service_name}' is RUNNING.")
        else:
            print(
                f"❌ The service '{service_name}' is NOT running (Status: {status})."
            )

    except FileNotFoundError:
        print("Error: 'systemctl' command not found. Are you on a Linux system?")


# Let's test it against a standard Linux service
check_service_status("SplunkForwarder.service")

# Let's test it against a fake service name to see the failure message
#check_service_status("fake-service")

        