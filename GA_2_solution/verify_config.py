"""
verify_config.py — Run this in your GA_2_solution folder to auto-check
whether config.py exactly matches the exam portal's assigned values.

Usage:
    cd ~/Documents/TDS_GA/GA_2_solution
    python3 verify_config.py
"""

import hashlib
import sys

try:
    import config
except ImportError:
    print("❌ Could not import config.py — run this script from inside GA_2_solution/")
    sys.exit(1)

EXPECTED_ISSUER = "https://idp.exam.local"
EXPECTED_AUDIENCE = "tds-q7lth2tf.apps.exam.local"
EXPECTED_KEY_SHA256 = "2dacfcbb8aadac6e6b58adb0c41a70df0b66ed1d2359bc5eb4020c9280cf652b"

ok = True

# 1. Check ISSUER
if config.ISSUER.strip() != EXPECTED_ISSUER:
    print(f"❌ ISSUER mismatch!\n   Expected: {EXPECTED_ISSUER!r}\n   Found:    {config.ISSUER!r}")
    ok = False
else:
    print("✅ ISSUER matches")

# 2. Check AUDIENCE
if config.AUDIENCE.strip() != EXPECTED_AUDIENCE:
    print(f"❌ AUDIENCE mismatch!\n   Expected: {EXPECTED_AUDIENCE!r}\n   Found:    {config.AUDIENCE!r}")
    ok = False
else:
    print("✅ AUDIENCE matches")

# 3. Check PUBLIC_KEY_PEM (normalize line endings before hashing)
normalized = config.PUBLIC_KEY_PEM.strip().replace("\r\n", "\n").encode()
actual_hash = hashlib.sha256(normalized).hexdigest()
if actual_hash != EXPECTED_KEY_SHA256:
    print(f"❌ PUBLIC_KEY_PEM does NOT match the portal's key!")
    print(f"   Expected SHA256: {EXPECTED_KEY_SHA256}")
    print(f"   Found SHA256:    {actual_hash}")
    print("   >>> This is very likely your bug. Re-copy the key EXACTLY from the exam portal.")
    ok = False
else:
    print("✅ PUBLIC_KEY_PEM matches exactly")

# 4. Confirm the key is even parseable (catches whitespace/format issues)
try:
    from cryptography.hazmat.primitives.serialization import load_pem_public_key
    load_pem_public_key(config.PUBLIC_KEY_PEM.strip().encode())
    print("✅ PUBLIC_KEY_PEM is valid, parseable PEM")
except ImportError:
    print("⚠️  'cryptography' package not installed locally — can't test parsing here, "
          "but make sure it's in requirements.txt for Render.")
except Exception as e:
    print(f"❌ PUBLIC_KEY_PEM failed to parse: {e}")
    ok = False

print()
if ok:
    print("🎉 config.py looks 100% correct. If /verify is still failing, the bug is "
          "likely in Render's Logs (check for 'ModuleNotFoundError: cryptography' or "
          "the actual JWT exception type) OR the deployed version on Render is stale — "
          "re-confirm with `git log -1` that your local latest commit matches Render's "
          "'Events' tab commit hash.")
else:
    print("🔧 Fix the ❌ items above in config.py, then:")
    print("   git add config.py")
    print("   git commit -m 'Fix config.py values'")
    print("   git push")