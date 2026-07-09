/* ==========================================
   HEALTHCARE INTERACTIVE JAVASCRIPT ENGINE
   ========================================== */

// Global Application State
const state = {
  gender: 'men',
  dietType: 'balanced',
  age: 28,
  weight: 78,
  height: 180,
  activity: 1.55,
  goal: 'lose',
  
  // Results
  calories: 2154,
  protein: 162,
  carbs: 215,
  fats: 72,
  bmr: 1780,
  tdee: 2654,
  
  // Habits & Hydration
  waterAmount: 1.25,
  waterGoal: 3.25,
  completedHabitsCount: 0,
  totalHabitsCount: 4
};

// Data Repositories
const DIET_TEMPLATES = {
  men: {
    balanced: [
      {
        meal: 'Breakfast',
        name: 'Steak & Egg Veggie Scramble',
        desc: 'Lean sirloin strips scrambled with pasture-raised eggs, baby spinach, and red bell peppers. Served with a side of roasted sweet potato cubes.',
        pPct: 0.35, cPct: 0.35, fPct: 0.30
      },
      {
        meal: 'Lunch',
        name: 'Lemon-Herb Chicken & Quinoa Bowl',
        desc: 'Flame-grilled chicken breast over organic quinoa, roasted broccoli florets, and sliced avocado. Drizzled with extra virgin olive oil.',
        pPct: 0.30, cPct: 0.45, fPct: 0.25
      },
      {
        meal: 'Dinner',
        name: 'Pan-Seared Salmon over Wild Rice',
        desc: 'Crispy skin salmon filet rich in Omega-3, served over wild black rice, steamed asparagus spears, and a side of garlic-sautéed kale.',
        pPct: 0.35, cPct: 0.35, fPct: 0.30
      },
      {
        meal: 'Snack',
        name: 'Greek Yogurt & Mixed Nut Medley',
        desc: 'Thick unsweetened Greek yogurt topped with fresh blueberries, organic pumpkin seeds, walnuts, and a dash of ground cinnamon.',
        pPct: 0.40, cPct: 0.30, fPct: 0.30
      }
    ],
    highprotein: [
      {
        meal: 'Breakfast',
        name: 'Triple Egg White & Turkey Bacon Omelet',
        desc: 'Whipped egg whites folded with smoked turkey breast, low-fat swiss cheese, and green onions. Served with sprouted grain toast.',
        pPct: 0.45, cPct: 0.30, fPct: 0.25
      },
      {
        meal: 'Lunch',
        name: 'Ultimate Beef & Rice Muscle Bowl',
        desc: 'Extra-lean ground beef sautéed with garlic, mixed greens, and served over white basmati rice with a clean spicy tomato salsa.',
        pPct: 0.40, cPct: 0.35, fPct: 0.25
      },
      {
        meal: 'Dinner',
        name: 'Grilled Turkey Tenderloin & Asparagus',
        desc: 'Herb-marinated turkey breast grilled to tender perfection, served with roasted green asparagus, and a baked gold potato.',
        pPct: 0.45, cPct: 0.30, fPct: 0.25
      },
      {
        meal: 'Snack',
        name: 'Whey Isolate Shake & Rice Cakes',
        desc: 'Premium grass-fed chocolate whey isolate blended with unsweetened almond milk. Paired with lightly salted brown rice cakes.',
        pPct: 0.60, cPct: 0.25, fPct: 0.15
      }
    ],
    keto: [
      {
        meal: 'Breakfast',
        name: 'Bacon, Egg & Avocado Plate',
        desc: 'Thick cut hardwood smoked bacon paired with eggs fried in grass-fed butter, and half a large Hass avocado sprinkled with sea salt.',
        pPct: 0.25, cPct: 0.05, fPct: 0.70
      },
      {
        meal: 'Lunch',
        name: 'Keto Chicken Caesar Salad',
        desc: 'Crisp romaine lettuce tossed with grilled chicken thighs, shaved parmesan cheese, and a rich, home-made creamy Caesar dressing.',
        pPct: 0.25, cPct: 0.05, fPct: 0.70
      },
      {
        meal: 'Dinner',
        name: 'Garlic Butter Ribeye & Cauliflower Mash',
        desc: 'Prime ribeye steak seared in garlic-infused butter, served alongside a steaming bowl of cauliflower mash loaded with cream cheese.',
        pPct: 0.25, cPct: 0.05, fPct: 0.70
      },
      {
        meal: 'Snack',
        name: 'Macadamia Nut & Cheese Snack Pack',
        desc: 'Raw macadamia nuts paired with aged cheddar cheese cubes, providing a perfect high-fat metabolic fuel source.',
        pPct: 0.20, cPct: 0.05, fPct: 0.75
      }
    ],
    vegan: [
      {
        meal: 'Breakfast',
        name: 'High-Protein Tofu Scramble',
        desc: 'Crumbled firm organic tofu seasoned with turmeric, nutritional yeast, black salt, baby spinach, and cherry tomatoes on sourdough.',
        pPct: 0.25, cPct: 0.45, fPct: 0.30
      },
      {
        meal: 'Lunch',
        name: 'Spiced Lentil & Sweet Potato Bowl',
        desc: 'Brown lentils simmered with warm spices, roasted sweet potato wedges, steam-wilted kale, and a generous creamy tahini dressing.',
        pPct: 0.25, cPct: 0.50, fPct: 0.25
      },
      {
        meal: 'Dinner',
        name: 'Tempeh Stir-Fry with Broccoli & Cashews',
        desc: 'Marinated organic tempeh cubes pan-fried with broccoli, snap peas, and raw cashews in a ginger-tamari glaze over brown rice.',
        pPct: 0.25, cPct: 0.45, fPct: 0.30
      },
      {
        meal: 'Snack',
        name: 'Edamame Pods & Pumpkin Seeds',
        desc: 'Steamed whole edamame pods tossed with coarse sea salt, paired with a serving of toasted green pepitas.',
        pPct: 0.30, cPct: 0.40, fPct: 0.30
      }
    ]
  },
  women: {
    balanced: [
      {
        meal: 'Breakfast',
        name: 'Berry Chia Protein Smoothie Bowl',
        desc: 'Organic mixed berries, whey or plant protein, and unsweetened almond milk blended thick, topped with chia seeds and shredded coconut.',
        pPct: 0.35, cPct: 0.35, fPct: 0.30
      },
      {
        meal: 'Lunch',
        name: 'Warm Quinoa & Roast Veggie Salad',
        desc: 'Baby arugula, roasted beets, carrots, and asparagus tossed with fluffy quinoa, lean sliced chicken breast, and white balsamic vinaigrette.',
        pPct: 0.30, cPct: 0.45, fPct: 0.25
      },
      {
        meal: 'Dinner',
        name: 'Baked Atlantic Cod & Sweet Potato Mash',
        desc: 'Baked cod fillet served with sweet potato mash and sautéed baby spinach to support natural iron, calcium, and cellular health.',
        pPct: 0.35, cPct: 0.35, fPct: 0.30
      },
      {
        meal: 'Snack',
        name: 'Crisp Apple Slices & Almond Butter',
        desc: 'One organic Honeycrisp apple sliced and paired with raw almond butter for sustained fat-burning energy.',
        pPct: 0.20, cPct: 0.50, fPct: 0.30
      }
    ],
    highprotein: [
      {
        meal: 'Breakfast',
        name: 'Egg White & Spinach Breakfast Cups',
        desc: 'Bred-in-silicone egg white cups baked with baby spinach, feta cheese, and tomatoes. Served with half a toasted sprouted english muffin.',
        pPct: 0.45, cPct: 0.30, fPct: 0.25
      },
      {
        meal: 'Lunch',
        name: 'Mediterranean Tuna & Chickpea Salad',
        desc: 'Pole-caught flaked tuna, chickpeas, diced cucumber, parsley, and cherry tomatoes, tossed in fresh lemon juice and sea salt.',
        pPct: 0.40, cPct: 0.35, fPct: 0.25
      },
      {
        meal: 'Dinner',
        name: 'Herb Grilled Chicken & Broccolini',
        desc: 'Lean chicken cutlets seasoned with rosemary and garlic, grilled and served with pan-charred broccolini and a half cup of quinoa.',
        pPct: 0.45, cPct: 0.30, fPct: 0.25
      },
      {
        meal: 'Snack',
        name: 'Cottage Cheese & Strawberry Bowl',
        desc: 'High-protein low-fat cottage cheese layered with sliced fresh strawberries, chia seeds, and a drizzle of raw honey.',
        pPct: 0.50, cPct: 0.35, fPct: 0.15
      }
    ],
    keto: [
      {
        meal: 'Breakfast',
        name: 'Smoked Salmon & Cream Cheese Scramble',
        desc: 'Pasture eggs scrambled gently with smoked wild salmon and a tablespoon of cream cheese, topped with chopped chives.',
        pPct: 0.25, cPct: 0.05, fPct: 0.70
      },
      {
        meal: 'Lunch',
        name: 'Avocado Salad with Chicken & Bacon',
        desc: 'Shredded chicken breast, crispy bacon bits, celery, and diced avocado folded with organic olive-oil mayonnaise.',
        pPct: 0.25, cPct: 0.05, fPct: 0.70
      },
      {
        meal: 'Dinner',
        name: 'Baked Sea Bass with Pesto & Asparagus',
        desc: 'Fresh sea bass fillet baked with green basil pesto, served with asparagus spears sautéed in extra virgin olive oil.',
        pPct: 0.25, cPct: 0.05, fPct: 0.70
      },
      {
        meal: 'Snack',
        name: 'Nut Butter Fat Bombs or Raw Pecans',
        desc: 'A small handful of raw pecans or coconut-almond fat bombs to curb sugar cravings and maintain nutritional ketosis.',
        pPct: 0.15, cPct: 0.05, fPct: 0.80
      }
    ],
    vegan: [
      {
        meal: 'Breakfast',
        name: 'Chia Seed Coconut Pudding',
        desc: 'Chia seeds soaked in light coconut milk, sweetened with stevia, and topped with raspberries and organic hemp hearts.',
        pPct: 0.20, cPct: 0.40, fPct: 0.40
      },
      {
        meal: 'Lunch',
        name: 'Edamame & Sesame Grain Salad',
        desc: 'Shelled edamame, shredded red cabbage, shredded carrots, and quinoa tossed with a toasted sesame ginger vinaigrette.',
        pPct: 0.25, cPct: 0.45, fPct: 0.30
      },
      {
        meal: 'Dinner',
        name: 'Black Bean & Quinoa Collard Wraps',
        desc: 'Steamed collard green leaves stuffed with seasoned black beans, quinoa, roasted sweet peppers, and clean avocado mash.',
        pPct: 0.25, cPct: 0.50, fPct: 0.25
      },
      {
        meal: 'Snack',
        name: 'Hummus Plate with Cucumber & Flax Crackers',
        desc: 'Organic chickpea hummus served with fresh cucumber slices and high-fiber flax seed crackers.',
        pPct: 0.20, cPct: 0.45, fPct: 0.35
      }
    ]
  }
};

const WORKOUT_TEMPLATES = {
  men: [
    {
      day: 'DAY 1 — ATHLETIC POWER & BUILD',
      title: 'Upper Body Push/Pull Split',
      exercises: [
        { name: 'Barbell Flat Bench Press', sets: '4 sets x 8 reps (Strength focus)' },
        { name: 'Barbell Bent-Over Row', sets: '4 sets x 8 reps (Upper back thickness)' },
        { name: 'Dumbbell Overhead Shoulder Press', sets: '3 sets x 10 reps (Shoulder stability)' },
        { name: 'Weighted Pull-Ups', sets: '3 sets x Maximum reps (Lats & core)' },
        { name: 'Incline Dumbbell Flyes', sets: '3 sets x 12 reps (Chest definition)' }
      ]
    },
    {
      day: 'DAY 2 — STRENGTH BASE & POSTERIOR',
      title: 'Lower Body Strength Split',
      exercises: [
        { name: 'Barbell Back Squats', sets: '4 sets x 6 reps (Quad & hip drive)' },
        { name: 'Romanian Deadlifts', sets: '4 sets x 8 reps (Hamstrings & glutes)' },
        { name: 'Walking Dumbbell Lunges', sets: '3 sets x 12 steps per leg (Single leg stability)' },
        { name: 'Standing Calf Raises', sets: '4 sets x 15 reps (Ankle power)' },
        { name: 'Hanging Leg Raises', sets: '3 sets x 15 reps (Core stability)' }
      ]
    },
    {
      day: 'DAY 3 — METABOLIC COND & HYBRID',
      title: 'Conditioning & Core Engine',
      exercises: [
        { name: 'Heavy Kettlebell Swings', sets: '5 sets x 20 reps (Posterior explosive power)' },
        { name: 'Dumbbell Renegade Rows', sets: '3 sets x 10 reps per side (Anti-rotational core)' },
        { name: 'Burpee to Broad Jump', sets: '4 sets x 45 seconds work / 15 seconds rest (HIIT)' },
        { name: 'Plank with Shoulder Taps', sets: '3 sets x 60 seconds (Static endurance)' },
        { name: 'Medicine Ball Slams', sets: '3 sets x 15 reps (Core output)' }
      ]
    }
  ],
  women: [
    {
      day: 'DAY 1 — POSTERIOR CHAIN & GLUTES',
      title: 'Glutes, Hips & Hamstrings',
      exercises: [
        { name: 'Barbell Hip Thrusts', sets: '4 sets x 10 reps (Glute activation & power)' },
        { name: 'Kettlebell Goblet Squats', sets: '3 sets x 12 reps (Quadriceps & hip mobility)' },
        { name: 'Dumbbell Romanian Deadlifts', sets: '4 sets x 10 reps (Hamstring conditioning)' },
        { name: 'Cable Glute Kickbacks', sets: '3 sets x 12 reps per leg (Glute medius focus)' },
        { name: 'Swiss Ball Hamstring Curls', sets: '3 sets x 15 reps (Knee joint safety)' }
      ]
    },
    {
      day: 'DAY 2 — POSTURE & UPPER SCULPT',
      title: 'Upper Posture & Core Stability',
      exercises: [
        { name: 'Wide Grip Lat Pull-Downs', sets: '3 sets x 10 reps (Back posture support)' },
        { name: 'Dumbbell Arnold Press', sets: '3 sets x 12 reps (Shoulder mobility)' },
        { name: 'Push-Ups (Incline or Floor)', sets: '3 sets x max reps (Upper body endurance)' },
        { name: 'Dumbbell Face Pulls', sets: '3 sets x 15 reps (Rear delts & rotator cuff)' },
        { name: 'Deadbugs (Slow)', sets: '3 sets x 10 control repetitions per side (Transverse core)' }
      ]
    },
    {
      day: 'DAY 3 — ATHLETIC METABOLIC FLOW',
      title: 'Interval Burn & Flexibility',
      exercises: [
        { name: 'Dumbbell Thrusters', sets: '4 sets x 45 seconds work / 15 seconds rest (Full body)' },
        { name: 'Sled Prowler Push or Jog Intervals', sets: '5 rounds x 30 seconds sprint / 30 seconds rest' },
        { name: 'Plank Commandos', sets: '3 sets x 45 seconds (Shoulder & core drive)' },
        { name: 'KB Kettlebell Deadlifts', sets: '3 sets x 12 reps (Clean hip hinge)' },
        { name: 'Dynamic Cobra-to-Down-Dog Flow', sets: '3 rounds x 5 controlled slow reps (Mobility)' }
      ]
    }
  ]
};

// Target Macro Splits
const MACRO_SPLITS = {
  balanced: { p: 0.30, c: 0.40, f: 0.30 },
  highprotein: { p: 0.40, c: 0.30, f: 0.30 },
  keto: { p: 0.25, c: 0.05, f: 0.70 },
  vegan: { p: 0.25, c: 0.50, f: 0.25 }
};

// Initial App Activation
window.addEventListener('DOMContentLoaded', () => {
  // Sync state values with form inputs on load
  document.getElementById('input-age').value = state.age;
  document.getElementById('input-weight').value = state.weight;
  document.getElementById('input-height').value = state.height;
  document.getElementById('input-activity').value = state.activity;
  
  // Attach form listener
  const form = document.getElementById('calculator-form');
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      calculateMetrics();
    });
  }

  // Draw initial state elements
  calculateMetrics();
  updateHabitsProgress();
  renderWaterProgress();
});

// Update app when gender switches
function setGender(newGender) {
  if (state.gender === newGender) return;
  state.gender = newGender;
  
  // UI Class switching
  const body = document.body;
  const btnMen = document.getElementById('btn-switch-men');
  const btnWomen = document.getElementById('btn-switch-women');
  
  if (newGender === 'men') {
    body.className = 'theme-men';
    btnMen.classList.add('active');
    btnWomen.classList.remove('active');
    
    // Modify Hero texts
    document.getElementById('hero-badge').innerText = 'PERFORMANCE & VITALITY';
    document.getElementById('hero-title').innerText = 'Sculpt Your Peak Strength & Diet';
    document.getElementById('hero-subtitle').innerText = "Elevate your daily nutrition and training routine with tailored recommendations driven by science. Engineered for your body's optimal output.";
    
    // Modify default weight/height defaults to match average male if the user hasn't typed anything other than default
    const ageInput = document.getElementById('input-age');
    const weightInput = document.getElementById('input-weight');
    const heightInput = document.getElementById('input-height');
    
    if (weightInput.value == 62 && heightInput.value == 163) {
      weightInput.value = 78;
      heightInput.value = 180;
    }
    
    // Set Water goal default for Men (3.25 Liters)
    state.waterGoal = 3.25;
  } else {
    body.className = 'theme-women';
    btnMen.classList.remove('active');
    btnWomen.classList.add('active');
    
    // Modify Hero texts
    document.getElementById('hero-badge').innerText = 'BALANCE & STRENGTH';
    document.getElementById('hero-title').innerText = 'Nourish Your Body, Align Energy';
    document.getElementById('hero-subtitle').innerText = 'Harmonize your metabolism, support bone and hormonal integrity, and tone lean muscle with custom food plans and active routines.';
    
    // Modify defaults to match average female if user has default inputs
    const weightInput = document.getElementById('input-weight');
    const heightInput = document.getElementById('input-height');
    
    if (weightInput.value == 78 && heightInput.value == 180) {
      weightInput.value = 62;
      heightInput.value = 163;
    }
    
    // Set Water goal default for Women (2.50 Liters)
    state.waterGoal = 2.50;
  }
  
  // Re-run calculations
  calculateMetrics();
}

// Update app when diet paradigm switches
function setDietType(newDietType) {
  state.dietType = newDietType;
  
  // Set tab classes
  const tabs = document.querySelectorAll('.diet-tab');
  tabs.forEach(tab => {
    const isMatched = tab.getAttribute('onclick').includes(newDietType);
    tab.className = isMatched ? 'diet-tab active' : 'diet-tab';
  });
  
  // Re-calculate macros and reload meals
  calculateMetrics();
}

// Perform calculations based on state and inputs
function calculateMetrics() {
  // Grab inputs from DOM
  state.age = parseInt(document.getElementById('input-age').value) || 28;
  state.weight = parseFloat(document.getElementById('input-weight').value) || 78;
  state.height = parseFloat(document.getElementById('input-height').value) || 180;
  state.activity = parseFloat(document.getElementById('input-activity').value) || 1.55;
  
  const goalRadios = document.getElementsByName('goal');
  for (let r of goalRadios) {
    if (r.checked) {
      state.goal = r.value;
      break;
    }
  }

  // Calculate BMR (Mifflin-St Jeor)
  if (state.gender === 'men') {
    state.bmr = Math.round(10 * state.weight + 6.25 * state.height - 5 * state.age + 5);
  } else {
    state.bmr = Math.round(10 * state.weight + 6.25 * state.height - 5 * state.age - 161);
  }
  
  // Calculate TDEE
  state.tdee = Math.round(state.bmr * state.activity);
  
  // Calorie adjustments based on goals
  let adjustmentText = "";
  if (state.goal === 'lose') {
    state.calories = state.tdee - 500;
    adjustmentText = "-500 kcal (Fat Loss Deficit)";
  } else if (state.goal === 'gain') {
    state.calories = state.tdee + 350;
    adjustmentText = "+350 kcal (Lean Bulk Surplus)";
  } else {
    state.calories = state.tdee;
    adjustmentText = "0 kcal (Maintenance)";
  }
  
  // Guarantee calories doesn't fall below minimum healthy levels
  const minCal = state.gender === 'men' ? 1500 : 1200;
  if (state.calories < minCal) {
    state.calories = minCal;
    adjustmentText = `Adjusted to Minimum Safe Calories (${minCal} kcal)`;
  }
  
  // Calculate exact macros based on diet template ratios
  const split = MACRO_SPLITS[state.dietType];
  
  // Gram calculations
  state.protein = Math.round((state.calories * split.p) / 4);
  state.carbs = Math.round((state.calories * split.c) / 4);
  state.fats = Math.round((state.calories * split.f) / 9);
  
  // Update DOM Outputs
  document.getElementById('calories-display').innerText = state.calories.toLocaleString();
  document.getElementById('bmr-display').innerText = `${state.bmr.toLocaleString()} kcal`;
  document.getElementById('tdee-display').innerText = `${state.tdee.toLocaleString()} kcal`;
  document.getElementById('goal-adjustment').innerText = adjustmentText;
  
  document.getElementById('legend-p-val').innerText = `${state.protein}g`;
  document.getElementById('legend-c-val').innerText = `${state.carbs}g`;
  document.getElementById('legend-f-val').innerText = `${state.fats}g`;
  
  // Generate descriptive overview text
  const direction = state.goal === 'lose' ? 'burn adipose tissue' : (state.goal === 'gain' ? 'synthesize new muscle fibers' : 'stabilize weight and energy output');
  const detailsText = `Your calculated metabolic burn is roughly ${state.tdee.toLocaleString()} calories daily. Sustaining ${state.calories.toLocaleString()} calories equips your body to ${direction} efficiently. Consuming ${state.protein}g of Protein supports biological tissue integrity.`;
  document.getElementById('calculator-summary-text').innerText = detailsText;
  
  // Update the Hero Visual preview card
  document.getElementById('visual-pill-gender').innerText = `${state.gender.toUpperCase()}'S ${state.dietType.toUpperCase()}`;
  document.getElementById('visual-title').innerText = `${state.goal.toUpperCase()} PHASE`;
  document.getElementById('visual-metric-val').innerText = state.calories.toLocaleString();
  
  document.getElementById('visual-p-val').innerText = `${state.protein}g`;
  document.getElementById('visual-c-val').innerText = `${state.carbs}g`;
  document.getElementById('visual-f-val').innerText = `${state.fats}g`;
  
  // Calculate relative bar widths
  const totalGrams = state.protein + state.carbs + state.fats;
  document.getElementById('visual-p-bar').style.width = `${(state.protein / totalGrams) * 100}%`;
  document.getElementById('visual-c-bar').style.width = `${(state.carbs / totalGrams) * 100}%`;
  document.getElementById('visual-f-bar').style.width = `${(state.fats / totalGrams) * 100}%`;
  
  // Trigger animations & rendering
  drawDonutChart();
  renderMealCards();
  renderWorkoutCards();
}

// Custom High-Quality Canvas-Based Donut Chart Drawer
function drawDonutChart() {
  const canvas = document.getElementById('macroChart');
  if (!canvas) return;
  
  const ctx = canvas.getContext('2d');
  const width = canvas.width;
  const height = canvas.height;
  
  // Clear canvas
  ctx.clearRect(0, 0, width, height);
  
  const centerX = width / 2;
  const centerY = height / 2;
  const radius = Math.min(centerX, centerY) - 15;
  const thickness = 14;
  
  const split = MACRO_SPLITS[state.dietType];
  const data = [split.p, split.c, split.f];
  
  // Theme styling colors
  const primaryColor = getComputedStyle(document.body).getPropertyValue('--primary-color').trim();
  const colors = [
    primaryColor,  // Protein
    '#3b82f6',     // Carbs
    '#f59e0b'      // Fats
  ];
  
  let startAngle = -Math.PI / 2; // Start from top
  
  for (let i = 0; i < data.length; i++) {
    const sliceAngle = data[i] * 2 * Math.PI;
    
    // Draw outer arc
    ctx.beginPath();
    ctx.arc(centerX, centerY, radius, startAngle, startAngle + sliceAngle);
    ctx.strokeStyle = colors[i];
    ctx.lineWidth = thickness;
    ctx.lineCap = 'round';
    ctx.stroke();
    
    startAngle += sliceAngle;
  }
  
  // Draw subtle inner shadow path
  ctx.beginPath();
  ctx.arc(centerX, centerY, radius - thickness / 2 - 2, 0, 2 * Math.PI);
  ctx.strokeStyle = 'rgba(255, 255, 255, 0.03)';
  ctx.lineWidth = 1;
  ctx.stroke();
}

// Dynamic Meal Card Renderer
function renderMealCards() {
  const container = document.getElementById('meals-grid');
  if (!container) return;
  
  container.innerHTML = "";
  
  const mealsList = DIET_TEMPLATES[state.gender][state.dietType];
  
  mealsList.forEach((m) => {
    // Calculate custom calories and macros specifically for this meal card based on state
    // We allocate total calories to: Breakfast (25%), Lunch (35%), Dinner (30%), Snack (10%)
    let alloc = 0.25;
    if (m.meal === 'Lunch') alloc = 0.35;
    else if (m.meal === 'Dinner') alloc = 0.30;
    else if (m.meal === 'Snack') alloc = 0.10;
    
    const mealCal = Math.round(state.calories * alloc);
    const mealP = Math.round(state.protein * alloc);
    const mealC = Math.round(state.carbs * alloc);
    const mealF = Math.round(state.fats * alloc);
    
    const card = document.createElement('div');
    card.className = 'glass-card meal-card';
    
    card.innerHTML = `
      <span class="meal-tag">${m.meal}</span>
      <h3>${m.name}</h3>
      <p class="meal-desc">${m.desc}</p>
      <div class="meal-nutrients">
        <div class="nutri-box">
          <span class="n-val">${mealCal}</span>
          <span class="n-lbl">CAL</span>
        </div>
        <div class="nutri-box">
          <span class="n-val">${mealP}g</span>
          <span class="n-lbl">PRO</span>
        </div>
        <div class="nutri-box">
          <span class="n-val">${mealC}g</span>
          <span class="n-lbl">CARB</span>
        </div>
      </div>
    `;
    
    container.appendChild(card);
  });
}

// Dynamic Workout Card Renderer
function renderWorkoutCards() {
  const container = document.getElementById('workouts-grid');
  if (!container) return;
  
  container.innerHTML = "";
  
  // Set subtitle based on gender
  const desc = document.getElementById('workout-section-desc');
  if (state.gender === 'men') {
    desc.innerText = "Training blueprints specifically optimized for testosterone support, strength hypertrophy, and cardiovascular power.";
  } else {
    desc.innerText = "Training blueprints customized for female hormonal patterns, metabolic resistance, pelvic floor/core health, and muscular toning.";
  }
  
  const workouts = WORKOUT_TEMPLATES[state.gender];
  
  workouts.forEach((w) => {
    const card = document.createElement('div');
    card.className = 'glass-card workout-card';
    
    let exercisesHTML = "";
    w.exercises.forEach(ex => {
      exercisesHTML += `
        <li class="ex-item">
          <span class="ex-name">${ex.name}</span>
          <span class="ex-sets">${ex.sets}</span>
        </li>
      `;
    });
    
    card.innerHTML = `
      <span class="workout-day-pill">${w.day}</span>
      <h3>${w.title}</h3>
      <ul class="workout-exercises">
        ${exercisesHTML}
      </ul>
    `;
    
    container.appendChild(card);
  });
}

// Habits Checklist Manager
function toggleHabit(checkbox) {
  const list = document.querySelectorAll('.habits-list input[type="checkbox"]');
  let checkedCount = 0;
  
  list.forEach((cb) => {
    if (cb.checked) checkedCount++;
  });
  
  state.completedHabitsCount = checkedCount;
  state.totalHabitsCount = list.length;
  
  updateHabitsProgress();
}

function updateHabitsProgress() {
  const scoreText = document.getElementById('habits-score');
  const bar = document.getElementById('habits-progress-bar');
  
  if (!scoreText || !bar) return;
  
  const pct = Math.round((state.completedHabitsCount / state.totalHabitsCount) * 100);
  scoreText.innerText = `${pct}%`;
  bar.style.width = `${pct}%`;
}

// Water Intake Manager
function adjustWater(amount) {
  state.waterAmount = Math.max(0, state.waterAmount + amount);
  renderWaterProgress();
}

function renderWaterProgress() {
  const currentText = document.getElementById('current-water-text');
  const targetText = document.querySelector('.target-water');
  const wave = document.getElementById('water-wave-fill');
  
  if (!currentText || !wave) return;
  
  // Dynamic labels
  currentText.innerText = state.waterAmount.toFixed(2);
  targetText.innerText = `/ ${state.waterGoal.toFixed(2)} Liters`;
  
  // Calculate filled percentage
  let pct = (state.waterAmount / state.waterGoal) * 100;
  pct = Math.min(100, Math.max(0, pct));
  
  wave.style.height = `${pct}%`;
}
