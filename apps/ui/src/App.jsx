const systemStatus = [
  { label: 'Biometric ingest', value: 'Online', tone: 'good' },
  { label: 'Geospatial fetcher', value: 'Active', tone: 'good' },
  { label: 'RF telemetry', value: 'Monitoring', tone: 'info' },
  { label: 'Fusion recompute', value: 'Policy-gated', tone: 'warn' },
  { label: 'Audit ledger', value: 'Immutable', tone: 'good' },
];

function App() {
  return (
    <div className="app-shell">
      <header className="topbar">
        <div>
          <p className="eyebrow">Distributed data fusion platform</p>
          <h1>Shydrie</h1>
        </div>
        <span className="status-badge">Privacy-preserving</span>
      </header>

      <main className="content-grid">
        <section className="panel hero-panel">
          <h2>System overview</h2>
          <p>
            Shydrie isolates sensitive biometric telemetry, ingests environmental and RF
            streams, and recomputes only privacy-safe features across trust boundaries.
          </p>
          <div className="metrics-row">
            <div className="metric">
              <span className="metric-label">Latency</span>
              <strong>~18ms</strong>
            </div>
            <div className="metric">
              <span className="metric-label">Workers</span>
              <strong>24</strong>
            </div>
            <div className="metric">
              <span className="metric-label">Safety</span>
              <strong>Tier-0 isolated</strong>
            </div>
          </div>
        </section>

        <section className="panel">
          <h2>Runtime status</h2>
          <ul className="status-list">
            {systemStatus.map((item) => (
              <li key={item.label}>
                <span>{item.label}</span>
                <span className={`pill ${item.tone}`}>{item.value}</span>
              </li>
            ))}
          </ul>
        </section>

        <section className="panel wide">
          <h2>Core domains</h2>
          <div className="domain-grid">
            <div className="domain-card">
              <h3>Biometric</h3>
              <p>Encrypted HR/GSR/EEG streams with tokenized identity boundaries.</p>
            </div>
            <div className="domain-card">
              <h3>Geospatial</h3>
              <p>NOAA/NASA granule fetch, netCDF/HDF5 validation, and raster staging.</p>
            </div>
            <div className="domain-card">
              <h3>RF telemetry</h3>
              <p>SoapySDR acquisition, FFT processing, spectrogram generation, and signal QA.</p>
            </div>
            <div className="domain-card">
              <h3>Fusion</h3>
              <p>Policy-gated recomputation over privacy-filtered, time-aligned features.</p>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;
