# CathWallCall Kiosk (Python + Raspberry Pi)

Starter setup for a Linux desktop Python app that runs in kiosk mode on Raspberry Pi OS.

## 1) Local development setup (Linux)

```bash
cd /home/michelle/Documents/cathwallcall
sudo apt-get install -y python3-venv
bash scripts/setup_env.sh
./run_kiosk.sh
```

## 2) Raspberry Pi OS setup

Copy this project to your Pi (example path: `/home/pi/cathwallcall`), then run:

```bash
cd /home/pi/cathwallcall
bash scripts/setup_pi.sh
bash scripts/setup_env.sh
chmod +x run_kiosk.sh scripts/setup_env.sh scripts/setup_pi.sh
```

## 3) Configure kiosk auto-start on login

Create autostart directory and install desktop entry:

```bash
mkdir -p /home/pi/.config/autostart
cp deployment/kiosk-autostart.desktop /home/pi/.config/autostart/cathwallcall.desktop
```

If your project path is not `/home/pi/cathwallcall`, edit the `Exec=` line in
`/home/pi/.config/autostart/cathwallcall.desktop`.

## 4) Optional: hide mouse cursor in kiosk mode

Add this command to your Openbox autostart file:

```bash
mkdir -p /home/pi/.config/openbox
echo "unclutter -idle 0.1 -root &" >> /home/pi/.config/openbox/autostart
```

## 5) Enable auto-login in LightDM

Edit:

```text
/etc/lightdm/lightdm.conf
```

Set:

```text
[Seat:*]
autologin-user=pi
autologin-user-timeout=0
user-session=openbox
```

Then reboot:

```bash
sudo reboot
```

## Project layout

```text
app/main.py                    # Fullscreen kiosk app entrypoint
run_kiosk.sh                   # Runtime launcher using .venv
deployment/kiosk-autostart.desktop
scripts/setup_env.sh
scripts/setup_pi.sh
requirements.txt
```

## Next customization

- Replace the Tkinter sample UI in `app/main.py` with your real application logic.
- Add your Python package dependencies to `requirements.txt`.
- For production, remove or disable ESC-exit behavior in `app/main.py`.
