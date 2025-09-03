from nautobot.apps.jobs import Job, StringVar, register_jobs
import os

class SetEnvSecret(Job):
    class Meta:
        name = "Set Env Secret"
        description = "Writes a value to environmental variable"

    secret_name = StringVar(description="Secret Name")
    secret_value = StringVar(description="Secret Value")

    def run(self, *, secret_name, secret_value):
        try:
            os.environ[secret_name]=secret_value
            self.logger.info(f"Saved to {secret_name}")
        except Exception as e:
            self.logger.error(f"Error: {str(e)}")

register_jobs(SetEnvSecret)