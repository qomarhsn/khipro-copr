# khipro Copr Package

This repository contains the Fedora Copr RPM spec file for **khipro**, a shift-free phonetic Bangla input method for Linux.

## About Khipro

Khipro is a shift-free phonetic input method for the Bangla language. Unlike traditional input methods, Khipro's innovative shift-free design allows users to type Bangla text efficiently without using the Shift key. This m17n version brings Khipro to Linux systems through the multilingualization (m17n) library.

## Installation

To install khipro from the Copr repository:

```bash
sudo dnf copr enable qomarhsn/khipro
sudo dnf install khipro
```

After installation, you can enable the Khipro input method through your desktop environment's input method settings (IBus, fcitx, or other m17n-compatible frameworks).