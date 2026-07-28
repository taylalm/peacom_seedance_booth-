# Deploy — Streamlit Community Cloud

A hosted, HTTPS URL you can share with colleagues. HTTPS means the camera works.

## 1. Put the code on GitHub

Create a **new empty repo** at https://github.com/new (Private recommended — the code
has no secrets, but private is safer). Do **not** add a README/gitignore there.

Then, from the project folder:

```bash
cd /Users/bytedance/Desktop/seedance_demo_app
git branch -M main
git remote add origin https://github.com/<you>/seedance-booth.git
git push -u origin main
```

(Secrets, credentials, venv, data, gallery, and the cloudflared binary are all
gitignored — only the 24 app files get pushed.)

## 2. Create the app on Streamlit Cloud

1. Go to https://share.streamlit.io → **Sign in with GitHub** → authorize.
2. **Create app** → **Deploy a public app from GitHub** (repo can be private).
3. Fill in:
   - **Repository**: `<you>/seedance-booth`
   - **Branch**: `main`
   - **Main file path**: `app.py`
   - **Advanced settings → Python version**: **3.12**
4. **Advanced settings → Secrets**: open the local file
   **`.streamlit/secrets_cloud.toml`** (in this project), copy its entire contents,
   and paste into the Secrets box.
5. **Deploy**. First build takes ~2–3 min (installs requirements.txt).

Your URL will be like `https://<something>.streamlit.app` — share that.

## 3. ⚠️ Important limitations (read before sharing widely)

- **Temporary credentials expire.** `ARK_SESSION_TOKEN` (and the AK/SK) are STS
  creds with a short TTL. **When they expire, video generation stops** (asset/TOS
  calls fail auth). To fix: get fresh creds, update the three values
  (`ARK_AK`, `ARK_SK`, `ARK_SESSION_TOKEN`) in **Streamlit Cloud → App → Settings →
  Secrets**, and reboot the app. For a long-lived deploy, ask BytePlus for a
  non-temporary AK/SK.
- **Storage is ephemeral.** Streamlit Cloud resets the filesystem on reboot/redeploy,
  so `NOW SHOWING` (local gallery) and the leads CSV are **not durable** — they clear
  when the app restarts. Finished films are still delivered by **email link** (hosted
  on TOS), which *is* durable. If you need a persistent gallery/leads, we'd add a
  database or store them in TOS.
- **No login on the main flow.** Anyone with the URL can generate videos (spends
  tokens) and see the Guest Gallery. Fine for trusted colleagues; add an app-wide
  password before wider sharing (ask and I'll wire it).
- **Backlot** stays password-protected (`ADMIN_PASSWORD`).

## 4. Updating the deployed app

Push to `main` and Streamlit Cloud auto-redeploys:
```bash
git add -A && git commit -m "..." && git push
```

## Notes
- The corporate-proxy CA bundle (`core/netfix.py`) is macOS-only and simply no-ops on
  Streamlit Cloud's Linux (which isn't behind the proxy) — standard certs work there.
- `requirements.txt` pins: streamlit, pillow, requests, certifi, byteplus-python-sdk-v2, tos.
