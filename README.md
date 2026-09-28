# ⚡ Omarchy Vicario Theme

> **A personal Omarchy desktop built around clarity, speed, and character.**

Omarchy Vicario Theme is a customized **Hyprland/Omarchy desktop environment** focused on a clean visual system, practical workflows, and a distinctive personal aesthetic.

It brings together customized configurations for Waybar, Hyprland, terminals, notifications, launchers, GTK applications, wallpapers, and other parts of the desktop.

## ✨ Features

* Hyprland configuration
* Custom Waybar configuration
* Custom weather module
* Terminal configurations for Kitty, Alacritty, and Ghostty
* Custom GTK styling
* Walker and Wofi styling
* Mako notification styling
* SwayOSD styling
* Hyprlock configuration
* Custom wallpapers
* Consistent colors and visual styling across applications

## 📁 Project Structure

```text
omarchy-vicario-theme/
├── backgrounds/          # Wallpapers
├── waybar/               # Waybar configuration and scripts
│   ├── config.jsonc
│   ├── style.css
│   └── scripts/
│       └── weather.py
├── colors.toml           # Theme colors
├── hyprland.conf         # Hyprland configuration
├── hyprlock.conf         # Lock screen configuration
├── kitty.conf             # Kitty configuration
├── ghostty.conf           # Ghostty configuration
├── alacritty.toml         # Alacritty configuration
├── gtk.css                # GTK styling
├── mako.ini               # Notification styling
├── walker.css             # Walker styling
├── wofi.css               # Wofi styling
└── ...
```

## 🌤️ Weather

The Waybar weather module uses `wttr.in` to retrieve weather information.

The default location is configurable through the `WEATHER_LOCATION` environment variable.

For example:

```bash
export WEATHER_LOCATION="Lagos"
```

The weather script can also be tested directly:

```bash
python waybar/scripts/weather.py
```

The script returns JSON for Waybar to consume.

## 📦 Dependencies

The weather script requires Python and the `requests` package.

On an Arch-based system:

```bash
sudo pacman -S python-requests
```

If using a separate Python environment such as `mise`, install the dependency into that environment:

```bash
python -m pip install requests
```

## 🚀 Installation

Once the repository is published to GitHub, Vicario can be installed through Omarchy's theme installer:

```bash
omarchy-theme-install https://github.com/YOUR_USERNAME/omarchy-vicario-theme.git
```

Replace `YOUR_USERNAME` with the GitHub account that hosts the repository.

## 🛠️ Development

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/omarchy-vicario-theme.git
cd omarchy-vicario-theme
```

Make changes to the configuration files and test them locally before committing.

## 🎨 Philosophy

Vicario is an evolving personal desktop environment.

The goal is not simply to collect configuration files, but to build a coherent system where the visual language and workflow feel consistent across the desktop.

---

**Omarchy Vicario Theme**

Built and customized by Victor.

