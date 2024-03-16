<script>
    import FoodChoices from "./foodChoices.svelte";
    import FoodCaloriesIntake from "./FoodCaloriesIntake.svelte";

    const breakfastImageLinks = [
        'loseWeight/bfFood.png',
        // Add paths to all breakfast images
    ];

    const lunchImageLinks = [
        'loseWeight/lFood.png',
        // Add paths to all breakfast images
    ];
    const dinnerImageLinks = [
        'loseWeight/dFood.png',
        // Add paths to all breakfast images
    ];
</script>

<style>
    .photo {
        position: relative;
        width: 20%;
    }

    .photo::after {
        position: absolute;
        content: "";
        top: 0%;
        left: 50px;
        height: 510px;
        width: 210px;
        box-shadow: inset 50px 50px 50px 0px lightgoldenrodyellow, inset -50px -50px 50px 0px lightgoldenrodyellow;
    }
    .suzy_container
    .weight_calc_container {
        height: 80vh;
        width: 50vw;
        gap: 20px;
        background-color: #b37eb5;
        display: flex; /* Use flexbox for positioning the child */
        justify-content: center; /* Center horizontally */
        align-items: center; /* Center vertically */
        flex-direction: column; /* Stack children vertically */
    }
</style>

<p style="font-family: 'IBM Plex Sans', sans-serif; font-weight: 600; font-size:80px; color:#393537;">
    To maintain their body, idols usually have to consume only 30%-60% of their bmi
</p>

<div class="suzy_container">
    <p style="font-family: 'IBM Plex Sans', sans-serif; font-weight: 600; font-size:35px; color:#393537;">
        The left images illustrate a day of food choices from Suzy Bae Sue Ji for 5 months. The total calories for her meals is only 1300!
    </p>
    <img src="loseWeight/suzy.png" style="width: 200px; height: 500px; display: flex" alt="">
    <FoodChoices imgLinks={breakfastImageLinks} mealName="breakfast"></FoodChoices>
    <FoodChoices imgLinks={lunchImageLinks} mealName="lunch"></FoodChoices>
    <FoodChoices imgLinks={dinnerImageLinks} mealName="dinner"></FoodChoices>
</div>

<div class="weight_calc_container">
    <p style="font-family: 'IBM Plex Sans', sans-serif; font-weight: 600; font-size:35px; color:#393537;">
        The right one shows how much food 1300 calories equal to
    </p>
    <FoodCaloriesIntake></FoodCaloriesIntake>
</div>