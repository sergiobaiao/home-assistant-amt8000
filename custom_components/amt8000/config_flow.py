import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_PORT

DOMAIN = "amt8000"
DEFAULT_PORT = 9009

class Amt8000ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title="Intelbras AMT 8000", data=user_input)

        data_schema = vol.Schema({
            vol.Required(CONF_HOST): str,
            vol.Optional(CONF_PORT, default=DEFAULT_PORT): int,
        })
        return self.async_show_form(step_id="user", data_schema=data_schema, errors=errors)