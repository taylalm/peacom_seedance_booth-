# Temporary BytePlus (STS) credentials for the asset-library APIs.
# Copy this to byteplus_creds.sh (gitignored), fill it in, and `source` it
# before launching the app. STS creds EXPIRE — re-source + restart when they do.
#
#   cp byteplus_creds.example.sh byteplus_creds.sh
#   chmod 600 byteplus_creds.sh
#   # edit in your values, then:
#   source byteplus_creds.sh
#   .venv/bin/python -m streamlit run app.py

export BYTEPLUS_ACCESS_KEY=
export BYTEPLUS_SECRET_KEY=
export BYTEPLUS_SESSION_TOKEN=
export BYTEPLUS_REGION=ap-southeast-1
