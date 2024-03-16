<script>
  let userCalories = 1300; // User input for desired calorie intake
  const foodCalories = {
    chickenBreast: 165, // Calories per 100g of chicken breast
    oatmeal: 389,       // Calories per 100g of oatmeal
    pizza: 266,         // Calories per 100g of pizza
    burger: 563,        // Calories per 100g of burger
  };

  // Function to calculate the amount of food in grams for the user's calorie intake
  function calculateAmount(caloriesIntake, foodCalorie) {
    return (caloriesIntake / foodCalorie);
  }

  // Calculate amounts based on the default userCalories
  let amounts = {
    chickenBreast: calculateAmount(userCalories, foodCalories.chickenBreast),
    oatmeal: calculateAmount(userCalories, foodCalories.oatmeal),
    pizza: calculateAmount(userCalories, foodCalories.pizza),
    burger: calculateAmount(userCalories, foodCalories.burger),
  };

  // Function to update amounts when user input changes
  function updateAmounts() {
    amounts = {
      chickenBreast: calculateAmount(userCalories, foodCalories.chickenBreast),
      oatmeal: calculateAmount(userCalories, foodCalories.oatmeal),
      pizza: calculateAmount(userCalories, foodCalories.pizza),
      burger: calculateAmount(userCalories, foodCalories.burger),
    };
  }
</script>

<div class="calculator">
  <h1>Calorie Intake:</h1>
  <label for="calories-input">Enter desired calorie intake:</label>
  <input
          id="calories-input"
          type="number"
          bind:value={userCalories}
          on:input={updateAmounts}
          min="0"
          placeholder="Calories"
  />

  <div class="food-list">
    <div class="food-item">
      <p>{amounts.chickenBreast.toFixed(2)} chicken breast</p>
    </div>
    <div class="food-item">
      <p>{amounts.oatmeal.toFixed(2)} bowl of OatMeal</p>
    </div>
    <div class="food-item">
      <p>{amounts.pizza.toFixed(2)} slice of Pizza</p>
    </div>
    <div class="food-item">
      <p>{amounts.burger.toFixed(2)} Big Mac</p>
    </div>
  </div>
</div>

<style>
  .calculator {
    font-family: 'Arial', sans-serif;
    width: 300px;
    /*margin: auto;*/
    background: #ffffff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    margin-left: 200px;
  }

  .food-list {
    margin-top: 20px;
  }

  .food-item {
    background-color: #f0f0f0;
    display: flex;
    justify-content: center; /* Align horizontal center */
    align-items: center; /* Align vertical center */
    text-align: center;
    margin: 10px 0;
    padding: 10px;
    border-radius: 5px;
    height: 30px;
  }

  input {
    padding: 10px;
    margin-top: 10px;
    margin-bottom: 20px;
  }

  label {
    display: block;
    margin-bottom: 5px;
  }
</style>
