const API_URL = "http://localhost:8000/predict";

// wire up toggle-row buttons
document.querySelectorAll('.toggle-row').forEach(row => {
  row.addEventListener('click', e => {
    const btn = e.target.closest('button');
    if(!btn) return;
    row.querySelectorAll('button').forEach(b => b.setAttribute('aria-pressed','false'));
    btn.setAttribute('aria-pressed','true');
  });
});

function toggleValue(field){
  const row = document.querySelector(`.toggle-row[data-field="${field}"]`);
  return row.querySelector('button[aria-pressed="true"]').dataset.value;
}

const form = document.getElementById('churnForm');
const submitBtn = document.getElementById('submitBtn');
const errorMsg = document.getElementById('errorMsg');
const result = document.getElementById('result');

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  errorMsg.style.display = 'none';
  result.classList.remove('show','visible');

  const payload = {
    gender: document.getElementById('gender').value,
    SeniorCitizen: parseInt(toggleValue('SeniorCitizen'), 10),
    Partner: toggleValue('Partner'),
    Dependents: toggleValue('Dependents'),
    tenure: parseInt(document.getElementById('tenure').value, 10),
    PhoneService: toggleValue('PhoneService'),
    MultipleLines: document.getElementById('MultipleLines').value,
    InternetService: document.getElementById('InternetService').value,
    OnlineSecurity: document.getElementById('OnlineSecurity').value,
    OnlineBackup: document.getElementById('OnlineBackup').value,
    DeviceProtection: document.getElementById('DeviceProtection').value,
    TechSupport: document.getElementById('TechSupport').value,
    StreamingTV: document.getElementById('StreamingTV').value,
    StreamingMovies: document.getElementById('StreamingMovies').value,
    Contract: document.getElementById('Contract').value,
    PaperlessBilling: toggleValue('PaperlessBilling'),
    PaymentMethod: document.getElementById('PaymentMethod').value,
    MonthlyCharges: parseFloat(document.getElementById('MonthlyCharges').value),
    TotalCharges: parseFloat(document.getElementById('TotalCharges').value)
  };

  submitBtn.disabled = true;
  submitBtn.textContent = 'Checking…';

  try {
    const res = await fetch(API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    if(!res.ok) throw new Error('Request failed: ' + res.status);
    const data = await res.json();
    renderResult(data);
  } catch (err) {
    errorMsg.style.display = 'block';
    console.error(err);
  } finally {
    submitBtn.disabled = false;
    submitBtn.textContent = 'Check signal';
  }
});

function renderResult(data){
  const prob = data.churn_probability;
  const pct = Math.round(prob * 100);
  const bars = document.querySelectorAll('#bars .bar');
  const filled = Math.max(1, Math.ceil(pct / 20));

  let color, label, desc;
  if(pct < 34){
    color = getComputedStyle(document.documentElement).getPropertyValue('--signal-strong');
    label = 'Strong signal'; desc = 'This customer looks likely to stay.';
  } else if(pct < 67){
    color = getComputedStyle(document.documentElement).getPropertyValue('--signal-mid');
    label = 'Weakening signal'; desc = 'Some risk of churn — worth a check-in.';
  } else {
    color = getComputedStyle(document.documentElement).getPropertyValue('--signal-weak');
    label = 'Signal lost'; desc = 'High churn risk — this customer may leave.';
  }

  bars.forEach((bar, i) => {
    bar.style.background = (i < filled) ? color.trim() : getComputedStyle(document.documentElement).getPropertyValue('--border').trim();
  });

  document.getElementById('resultLabel').textContent = label;
  document.getElementById('resultDesc').textContent = desc;
  document.getElementById('resultProb').textContent = pct + '%';
  document.getElementById('signalCaption').textContent = `Signal strength · ${data.prediction_label || (data.prediction ? 'Churn' : 'No churn')}`;

  result.classList.add('show');
  requestAnimationFrame(() => result.classList.add('visible'));
}