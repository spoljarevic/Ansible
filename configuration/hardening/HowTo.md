# Rocky Linux Hardening Playbook

`rockylinux-hardening.yml` turns a fresh Rocky Linux server into a baseline-hardened
host with a login user and podman ready for quadlets.

## Before you run it

1. Make sure `~/.ssh/ionos.pub` exists on the machine you run `ansible-playbook`
   from — it gets copied to the new user's `authorized_keys`.
2. Edit `vault.yml` and set a real password and hostname:
   ```yaml
   vault_ls_password: "your-password-here"
   vault_hostname: "your-hostname-here"
   ```
3. Encrypt it:
   ```bash
   ansible-vault encrypt vault.yml
   ```
   Already encrypted? Edit it in place instead: `ansible-vault edit vault.yml`.
4. Run the playbook:
   ```bash
   ansible-playbook -i <inventory> rockylinux-hardening.yml --ask-vault-pass
   ```
5. **Keep your current session open.** Test a fresh SSH login on port `2204`
   with the key before closing anything — password auth and root login are
   disabled by the end of the run.

## What it does

- Sets the hostname from `vault_hostname`.
- Installs `firewalld`, `fail2ban`, `chrony`, `dnf-automatic`, `podman`,
  `neovim`, and SELinux tooling (via EPEL + base repos).
- Enables and starts `chronyd`, `dnf-automatic.timer` (unattended security
  updates), and `firewalld`.
- Creates user `ls` (home dir, bash shell, sudo via `wheel`) with the vault
  password, and installs your SSH key for it.
- Opens `80/tcp`, `443/tcp`, `2204/tcp` in firewalld's public zone.
- Adds an SELinux port label so `sshd` is allowed to bind port `2204`.
- Writes a `fail2ban` jail for `sshd` (1h ban, 10m findtime, 5 retries).
- Hardens `sshd_config`: port `2204`, no root login, no password auth,
  pubkey auth only — applied via `reload` (not `restart`) so existing
  sessions survive.

## Task order matters

The key, firewall port, and SELinux context are all put in place *before*
sshd is reconfigured, so a partial run can't lock you out. sshd and fail2ban
are only reloaded — via handlers, at the very end — once their config has
been validated (`sshd -t`).

## Not covered here

Application/reverse-proxy setup via podman quadlets is a separate step —
this playbook only installs podman and opens `80`/`443`, it doesn't deploy
any containers.
