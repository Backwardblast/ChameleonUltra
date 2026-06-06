# CUv2 Stable

CUv2 Stable is a conservative downstream build based on upstream commit
`1a014f9` from May 15, 2026.

## Included changes

- PR #274: more accurate MIFARE Classic state transitions and access checks.
- PR #404: tested Jablotron LF read, emulation and T55xx support.
- PR #246: configurable long-button threshold.
- PR #434: non-interactive CLI mode and portable hardware tests.
- PRs #423-#426: MIFARE dump, dictionary and hardnested fallback fixes.
- PR #317: correct bundled tool lookup in PyInstaller builds.
- Command ID collision test and removal of duplicate firmware definitions.

## Safe flashing

Use only `ultra-dfu-app.zip` for a normal Chameleon Ultra update. This package
updates the application and does not replace the bootloader or SoftDevice.
Do not use a Lite package on an Ultra.

Keep an official `ultra-dfu-app.zip` package available before testing this
build. If the new firmware is unsuitable, enter DFU mode and install the
official package.

## Downgrade note

This build migrates the settings record from version 6 to version 7. An older
official firmware detects the newer settings version and restores default
button, BLE, animation and sleep settings. Slot data and tag dumps are stored
separately and are not wiped by this settings reset.

## Compatibility expectation

PR #274 makes MIFARE Classic emulation behave more like a physical card,
including sector authentication and access-bit handling. It may improve
compatibility with strict readers, but it cannot fix reader incompatibilities
caused by RF coupling, antenna placement or analog timing.
