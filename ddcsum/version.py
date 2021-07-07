from ddcsum import __version__

DDCSUM_VERSION = __version__
PROTOCOL_VERSION = '0.10'   # protocol version requested
NEW_SEED_VERSION = 11       # ddcsum versions >= 2.0
OLD_SEED_VERSION = 4        # ddcsum versions < 2.0

# The hash of the mnemonic seed must begin with this
SEED_PREFIX = '01'  # Electrum standard wallet
SEED_PREFIX_2FA = '101'  # extended seed for two-factor authentication
