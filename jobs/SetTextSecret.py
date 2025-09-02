from nautobot.extras.jobs import Job, StringVar, register_jobs
import os

class SetTextSecret(Job):
    class Meta:
        name = "Set Text Secret"
        description = "Writes a value to a text file in /opt/nautobot/secrets/[name].txt"
	secret_name = StringVar(description="Secret Name")
	secret_value = StringVar(description="Secret Value",secret=True)

    def run(self, *, secret_name, secret_value):
        file_path = f"/opt/nautobot/secrets/{secret_name}.txt"
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, "w") as f:
                f.write(secret_value)
            self.logger.info(f"Secret saved to {file_path}")
        except PermissionError:
            self.logger.error(f"Permission denied writing to {file_path}")
        except Exception as e:
            self.logger.error(f"Error writing to {file_path}: {str(e)}")

register_jobs(SetTextSecret)