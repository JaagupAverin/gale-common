# Gale

A Zephyr demo that shows how to set up a multi-application project with a common interface. Liberally uses the many kernel features and other utilities provided by Zephyr (some simple things are occasionally over-engineered for the sake of demonstration).

- [Common](https://github.com/JaagupAverin/gale-common) - common code and main west manifest
- [Sensor app](https://github.com/JaagupAverin/gale-sensor-app) - application demonstrating basic peripheral usage
- [Bluetooth app](https://github.com/JaagupAverin/gale-bluetooth-app) - application demonstrating basic Bluetooth usage
- [Zephyr fork](https://github.com/JaagupAverin/gale-zephyr) - Zephyr fork with project-specific adjustments

# Quickstart:

Clone repositories:

```bash
mkdir gale && cd gale
west init -m https://github.com/JaagupAverin/gale-common
west update --rebase
```

Install dependencies:

```bash
cd common
python -m venv .venv
source .venv/bin/activate
python -m pip install west ruff basedpyright
west packages pip --install
west sdk install
```
