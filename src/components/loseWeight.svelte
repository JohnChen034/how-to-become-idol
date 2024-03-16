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
</style>

<p style="font-family: 'IBM Plex Sans', sans-serif; font-weight: 600; font-size:50px; color:#393537;">
    to maintain their body, idols usually have to consume only 30%-60% of their bmi
</p>

<div style="display: flex; flex-direction: row;">
    <p style="width: 50%; margin-left: 10px font-family: 'IBM Plex Sans', sans-serif; font-weight: 600; font-size:20px; color:#393537;">
        On the left shows a day of food choices from Suzy Bae Sue Ji for 5 months. The total calories for her meals isonly 1300!
    </p>
    <p style="width: 50%"> on the right shows how much food 1300 calories equal to</p>
</div>


<div style="display: flex;     flex-direction: row; width: 100%; height: 450px">

    <div class="photo">
        <div
                id="img"
                alt="此处放置图片" style="margin-left: 50px;">
            <img src="loseWeight/suzy.png" style="width: 200px; height: 500px; display: flex" alt="">
        </div>

    </div>
    <div style="display: flex;     flex-direction: column;">
        <FoodChoices imgLinks={breakfastImageLinks} mealName="breakfast"></FoodChoices>
        <FoodChoices imgLinks={lunchImageLinks} mealName="lunch"></FoodChoices>
        <FoodChoices imgLinks={dinnerImageLinks} mealName="dinner"></FoodChoices>
    </div>
    <FoodCaloriesIntake></FoodCaloriesIntake>

</div>