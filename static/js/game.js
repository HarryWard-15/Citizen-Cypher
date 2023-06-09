// Initialising HTML element groups as const so that we can iterate through them
const questionBox = document.getElementById("question");
const answers = document.getElementById("answers");
const buttons = document.querySelectorAll(".answerButton");
const gameBox = document.getElementById("gameBox");
const gameInfo = document.getElementById("gameInfo");

// List of options for each statistic with values to change each statistic by
const options = {
  sleep: [
    ["Stick to routine", 2],
    ["Make bedroom serene", 2],
    ["Relax body and mind", 3],
    ["Reduce screen usage", 2],
    ["Take relaxing bath", 2],
    ["Ensure comfy bedding", 2],
    ["Optimize sleep conditions", 2],
    ["Deep breathe for calmness", 1],
    ["Play soothing sounds", 1],
    ["Read for relaxation", 1],
    ["Oversleep", -6],
    ["Nightmares", -4],
    ["Toss and turn", -4],
    ["Late screen use", -4],
    ["Skip sleep", -8],
    ["Uncomfortable sleep", -4],
    ["Noisy sleep space", -4],
    ["Pre-bed anxiety", -2],
    ["Disturbing sounds", -2],
    ["Unsettling books", -2],
  ],
  happiness: [
    ["Read for relaxation", 1],
    ["Connect with loved ones", 4],
    ["Enjoy hobbies", 3],
    ["Cultivate gratitude", 2],
    ["Show kindness", 3],
    ["Practice positive self-talk", 2],
    ["Seek support and connection", 3],
    ["Prioritize self-care", 2],
    ["Find humor", 2],
    ["Accomplish small goals", 2],
    ["Do fulfilling activities", 3],
    ["Experience loss", -6],
    ["Have conflicts", -6],
    ["Feel betrayed", -4],
    ["Negative self-talk", -4],
    ["Feel lonely", -4],
    ["Neglect self-care", -4],
    ["Encounter unfortunate events", -6],
    ["Watch sad content", -4],
    ["Fail to achieve goals", -4],
  ],
  fitness: [
    ["Do cardio workouts", 4],
    ["Build strength", 3],
    ["Join group workouts", 4],
    ["Walk briskly", 3],
    ["Do yoga or Pilates", 2],
    ["Opt for stairs", 2],
    ["Explore new workouts", 2],
    ["Monitor progress", 2],
    ["Hydrate adequately", 1],
    ["Stretch and move", 2],
    ["Avoid exercise", -8],
    ["Feel tired", -4],
    ["Do repetitive workouts", -4],
    ["Face setbacks", -6],
    ["Lack motivation", -4],
    ["Strain during workouts", -6],
    ["Attend boring fitness classes", -4],
    ["Feel sore", -4],
    ["Get dehydrated", -2],
    ["Skip warm-up/cool-down", -2],
  ],
  saturation: [
    ["Choose balanced meals", 4],
    ["Opt for healthy snacks", 3],
    ["Eat mindfully", 2],
    ["Incorporate fiber in meals", 2],
    ["Hydrate to avoid snacks", 2],
    ["Prioritize protein intake", 3],
    ["Meal prep in advance", 2],
    ["Honor hunger signals", 2],
    ["Stick to regular meals", 2],
    ["Eat colorful produce", 2],
    ["Skip meals, stay hungry", -8],
    ["Snack unsatisfyingly", -4],
    ["Overeat mindlessly", -6],
    ["Miss essential nutrients", -4],
    ["Feel constantly thirsty", -4],
    ["Eat unhealthy processed food", -6],
    ["Lack meal planning", -4],
    ["Emotionally eat, ignore hunger", -4],
    ["Develop unhealthy eating habits", -6],
    ["Eat low-fiber, unbalanced meals", -4],
  ],
};

// Initialising a few more variables for functions to use globally.
let currentStats = [25, 25, 25, 25];
let answersArrChange = [];
let clickCount = 0;
var buttonClicked;

// This function will choose a random question from its respective list.
// It will apply the question text to the statistic's button
// and add the delta value to an array so it can be accessed elsewhere.
function updateQuestion() {
  const sleepChanger = options.sleep[Math.floor(Math.random() * 20)];
  const happinessChanger = options.happiness[Math.floor(Math.random() * 20)];
  const fitnessChanger = options.fitness[Math.floor(Math.random() * 20)];
  const saturationChanger = options.saturation[Math.floor(Math.random() * 20)];

  const answersArr = [
    sleepChanger[0],
    happinessChanger[0],
    fitnessChanger[0],
    saturationChanger[0],
  ];
  answersArrChange = [
    sleepChanger[1],
    happinessChanger[1],
    fitnessChanger[1],
    saturationChanger[1],
  ];

  for (const child of answers.children) {
    child.innerHTML = answersArr[child.id];
  }
  updateStats(currentStats);
}

// Checks if any of the statistics has hit a value of 0 or under
// runs endGame() function if so; and if not, iterate through 
// statistics on game box and update values.
function updateStats(arr) {
  if (
    currentStats[0] <= 0 ||
    currentStats[1] <= 0 ||
    currentStats[2] <= 0 ||
    currentStats[3] <= 0
  ) {
    endGame();
  }
  let counter = 0;
  for (const el of gameBox.children) {
    el.childNodes[1].innerHTML = arr[counter];
    counter++;
  }
}

// Iterates day counter per click in game info box.
// Attempts to add last clicked option to game info box.
function updateInfo(e, diff) {
  console.log(e.target);
  let day_counter = gameInfo.childNodes[1];

  let last_action = gameInfo.childNodes[5];

  day_counter.childNodes[1].innerHTML = clickCount;
  let action;
  switch (e.target.id) {
    case "0":
      action =  "sleep";
      break;
    case "1":
      action = "happiness";
      break;
    case "2":
      action = "fitness";
      break;
    case "3":
      action = "saturation";
      break;
  };
  last_action.innerHTML = "You chose to " + e.target.innerHTML + " which gave you " + diff +" on your "+ action + " stat";
  console.log(last_action.innerHTML);
}

// Game over function
// Once a statistic hits zero, disable all buttons
// Take all statistics and convert it to a JSON string
// Also takes day counter and statistic that lead to game over and does the same.
// Calls another function to POST the day count and stat to our /game route.
function endGame() {
  buttons.forEach((button) => {
    button.classList.add("disabled");
  });

  let stats_json = JSON.stringify({
    Sleep: currentStats[0],
    Happiness: currentStats[1],
    Fitness: currentStats[2],
    Saturation: currentStats[3],
  });
  console.log("Game has ended");
  console.log(stats_json);

  let stats_obj = JSON.parse(stats_json);

  let death_stat;

  for (var key in stats_obj) {
    if (stats_obj.hasOwnProperty(key) && stats_obj[key] <= 0) {
      death_stat = key;
    }
  }

  let dbdata_json = JSON.stringify({
    death_stat: death_stat,
    days_count: clickCount,
  });
  console.log(dbdata_json);

  sendGameData(dbdata_json);
}

// POST json file to /game route.
function sendGameData(json) {
  var xhr = new XMLHttpRequest();
  var url = "/game";

  xhr.open("POST", url, true);

  xhr.setRequestHeader("Content-Type", "application/json");

  console.log(json);
  xhr.send(json);
}

let clickEvent = (e) => {
  clickCount += 1;
  const answerId = e.target.id;
  const diff = answersArrChange[answerId];
  currentStats[answerId] += diff;
  buttonClicked = e.target.innerText;
  updateInfo(e, diff);
  updateQuestion();
  console.log("click count", clickCount);

};

buttons.forEach((button) => {
  button.addEventListener("click", clickEvent);
});

updateStats(currentStats);
updateQuestion();
