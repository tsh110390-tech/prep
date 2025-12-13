const form = document.getElementById('application-form');
const statusCard = document.getElementById('status');
const resetButton = document.getElementById('reset');

const getEligibility = (income, score, cardType) => {
  let decision = 'Reviewing details';
  let limit = '$1,000';
  const cleanIncome = Number(income);

  if (score.includes('Excellent') || score.includes('Good')) {
    decision = 'Pre-qualified';
    limit = cleanIncome > 100000 ? '$10,000' : '$5,000';
  } else if (score.includes('Fair')) {
    decision = 'Conditional approval';
    limit = cleanIncome > 60000 ? '$3,000' : '$1,500';
  } else {
    decision = 'Starter offer recommended';
    limit = '$800';
  }

  const perks = {
    'Cash Back': 'Earn up to 3% on everyday categories and a $200 intro bonus.',
    'Travel Rewards': 'Collect 2x points on travel and dining with airport lounge visits.',
    Starter: 'Build credit with automatic reviews for limit increases in 6 months.'
  };

  const apr = score.includes('Excellent') ? '17.99%' : score.includes('Good') ? '19.49%' : '22.99%';

  return {
    decision,
    limit,
    apr,
    perk: perks[cardType] || 'Personalized benefits available after review.'
  };
};

const renderSummary = (data, result) => {
  statusCard.innerHTML = `
    <div class="status__row">
      <div>
        <p class="helper">Status</p>
        <p class="option__title">${result.decision}</p>
      </div>
      <span class="tag">${result.limit} limit preview</span>
    </div>
    <div class="status__row">
      <div>
        <p class="helper">Applicant</p>
        <p class="option__title">${data.fullName}</p>
        <p class="helper">${data.email} • ${data.phone}</p>
      </div>
      <div>
        <p class="helper">Estimated APR</p>
        <p class="option__title">${result.apr}</p>
      </div>
    </div>
    <div class="status__row">
      <div>
        <p class="helper">Selected card</p>
        <p class="option__title">${data.cardType}</p>
        <p class="helper">${result.perk}</p>
      </div>
      <div>
        <p class="helper">Profile</p>
        <p class="helper">Income: $${Number(data.income).toLocaleString()}</p>
        <p class="helper">Employment: ${data.employment}</p>
        <p class="helper">Credit: ${data.score}</p>
      </div>
    </div>
    <p class="helper">We'll send your next steps to ${data.email}. You can continue to complete the full application or schedule a call with our team.</p>
  `;
};

form.addEventListener('submit', (event) => {
  event.preventDefault();
  const formData = new FormData(form);
  const values = Object.fromEntries(formData.entries());
  const { fullName, email, phone, income, employment, score, cardType, consent } = values;

  if (!consent) {
    statusCard.innerHTML = '<p class="helper">Please provide consent to continue.</p>';
    return;
  }

  const result = getEligibility(income, score, cardType);
  renderSummary({ fullName, email, phone, income, employment, score, cardType }, result);
});

resetButton.addEventListener('click', () => {
  form.reset();
  statusCard.innerHTML = '<p class="helper">Complete the form to see your personalized summary.</p>';
});
