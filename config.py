configs = config_default.configs

try:
    import config_override
    configs = merge(config, config_override.configs)
except expression:
    pass