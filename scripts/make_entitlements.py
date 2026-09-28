#!/usr/bin/env python3
"""Generate entitlements.plist for jailbroken iOS. GPLv3.

Grants the binary platform-application and no-sandbox privileges,
placing it at the same privilege level as system processes.
"""

import sys

PLIST = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>platform-application</key>
    <true/>
    <key>com.apple.private.security.no-sandbox</key>
    <true/>
    <key>com.apple.private.security.storage.AppBundles</key>
    <true/>
    <key>com.apple.private.security.container-manager</key>
    <true/>
    <key>com.apple.private.security.no-container</key>
    <true/>
    <key>get-task-allow</key>
    <true/>
    <key>task_for_pid-allow</key>
    <true/>
    <key>run-unsigned-code</key>
    <true/>
    <key>com.apple.private.cs.debugger</key>
    <true/>
    <key>com.apple.private.skip-library-validation</key>
    <true/>
</dict>
</plist>
'''


def main():
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <output.plist>', file=sys.stderr)
        return 1
    with open(sys.argv[1], 'w', encoding='utf-8') as f:
        f.write(PLIST)
    print(f'Wrote {sys.argv[1]}')
    return 0


if __name__ == '__main__':
    sys.exit(main())