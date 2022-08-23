(
    python -m venv venv && venv/Scripts/activate
    pip -q install wfdb==3.4.0 &&
    wget -q https://www.physionet.org/static/published-projects/mitdb/mit-bih-arrhythmia-database-1.0.0.zip &&
    unzip -qo /content/mit-bih-arrhythmia-database-1.0.0.zip &&
    src/changeSignal.py && src/PanTomkinsQRS.py && src/PlottingAfterDelay.py && src/CalculatingHeartRate.py && src/PlottingWithBeatsPerMin.py
)

