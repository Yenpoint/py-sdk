from bsv.hd import mnemonic_from_entropy, seed_from_mnemonic, master_xprv_from_seed
from bsv.hd import bip32_derive_xprvs_from_mnemonic, bip44_derive_xprvs_from_mnemonic, bip32_derive_xkeys_from_xkey
from bsv.constants import BIP32_DERIVATION_PATH, BIP44_DERIVATION_PATH

# You can set custom derivation paths in your environment variables as well
# BIP32_DERIVATION_PATH = "m/"
# BIP44_DERIVATION_PATH = "m/44'/236'/0'"

#
# HD derivation (mnemonic, master-xpublickey, master-xprivatekey)
#
entropy = 'cd9b819d9c62f0027116c1849e7d497f'

# Generate mnemonic from entropy
mnemonic: str = mnemonic_from_entropy(entropy)
print("Mnemonic:", mnemonic)

# Generate seed from mnemonic
seed = seed_from_mnemonic(mnemonic, lang='en')
print("Seed:", seed.hex())

# Generate master keys
master_xprv = master_xprv_from_seed(seed)
master_xpub = master_xprv.xpub()
print("Master xprv:", master_xprv)
print("Master xpub:", master_xpub)
print()

# Derive keys from mnemonic using BIP32
keys_from_mnemonic_by_bip32 = bip32_derive_xprvs_from_mnemonic(
    mnemonic, 0, 3, path=BIP32_DERIVATION_PATH, change=0
)

print("Keys from mnemonic by BIP32:")
print("Address 0:", keys_from_mnemonic_by_bip32[0].address())
print("Private key 1:", keys_from_mnemonic_by_bip32[1].private_key().wif())
print("Public key 2:", keys_from_mnemonic_by_bip32[2].public_key().hex())
print()

# Derive keys from xpub using BIP32
keys_from_xpub_by_bip32 = bip32_derive_xkeys_from_xkey(
    master_xpub, 0, 3, change=0
)

print("Keys from xpub by BIP32:")
print("Address 0:", keys_from_xpub_by_bip32[0].address())
print("Public key 2:", keys_from_xpub_by_bip32[2].public_key().hex())
print()

# Derive keys from mnemonic using BIP44
bip44_keys = bip44_derive_xprvs_from_mnemonic(
    mnemonic, 0, 3, path=BIP44_DERIVATION_PATH, change=0
)

print("Keys from mnemonic by BIP44:")
print("Address 0:", bip44_keys[0].address())
print("Private key 1:", bip44_keys[1].private_key().wif())
print("Public key 2:", bip44_keys[2].public_key().hex())
print()

# Loop through multiple derived keys
print("All BIP44 derived keys:")
for i, key in enumerate(bip44_keys):
    print(f"Address {i}: {key.address()}")
    print(f"Private key {i}: {key.private_key().wif()}")