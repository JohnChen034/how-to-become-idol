<script>
    import FoodChoices from "./foodChoices.svelte";
    import FoodCaloriesIntake from "./FoodCaloriesIntake.svelte";
export let index;
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
        @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .a {
        opacity: 0;
        animation: fadeInUp 0.5s ease-out forwards;
        animation-delay: 0.5s;
    }
    .photo {
        position: relative;
        width: 20%;
    }

    .photo::after {
        position: absolute;
        content: "";
        top: 0%;
        left: 200px;
        height: 510px;
        width: 210px;
        box-shadow: inset 50px 50px 50px 0px #b37eb5, inset -50px -50px 50px 0px #b37eb5;
    }
    .suzy_container
    .weight_calc_container {
        height: 80vh;
        width: 50vw;
        gap: 20px;
        background-color: #b37eb5;
        display: flex; /* Use flexbox for positioning the child */
        justify-content: flex-start; /* Center horizontally */
        align-items: flex-start; /* Center vertically */
        flex-direction: row; /* Stack children vertically */
    }
</style>

{#if index > 9}
    <div class="a">
<p style="font-family: 'IBM Plex Sans', sans-serif; font-weight: 600; font-size:80px; color:#393537;">
    To maintain their body, idols usually have to consume only 30%-60% of their bmi
</p>

<div style="display: flex; flex-direction: row;">
    <p style="font-family: 'IBM Plex Sans', sans-serif; font-weight: 500; font-size:25px; color:#393537; width: 60%">
        The left images illustrate a day of food choices from Suzy Bae Sue Ji for 5 months. The total calories for her meals is only 1300!
    </p>
    <p style="font-family: 'IBM Plex Sans', sans-serif; font-weight: 500; font-size:25px; color:#393537; width: 30%">
        The right one shows how much food 1300 calories equal to
    </p>
</div>


<div style="display: flex;     flex-direction: row; width: 100%; height: 450px">

    <div class="photo">
        <div
                id="img"
                alt="此处放置图片">
            <img src="loseWeight/suzy.png" style="margin-left: 200px; width: 200px; height: 500px; display: flex"
                 alt="">
        </div>

    </div>
    <div style="display: flex;     flex-direction: column; margin-left: 200px; ">
        <FoodChoices imgLinks={breakfastImageLinks} mealName="breakfast"></FoodChoices>
        <FoodChoices imgLinks={lunchImageLinks} mealName="lunch"></FoodChoices>
        <FoodChoices imgLinks={dinnerImageLinks} mealName="dinner"></FoodChoices>
    </div>
    <FoodCaloriesIntake></FoodCaloriesIntake>

</div>

</div>

{/if}

