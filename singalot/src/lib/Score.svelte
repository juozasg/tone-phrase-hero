<script lang="ts">
	import { secondsToTime } from './util';

	let score = $state(0);
	let time = $state(0);

	export const getTime = () => time;

	const winningScore = 20;

	let initialState = $state(true);
	export const hasWon = () => score >= winningScore;

	let timer: number;

	export const reset = () => {
		score = 0;
		time = 0;
		initialState = false;
		timer = setInterval(() => {
			time += 1;
		}, 1000);
	};

	// reset();

	export const correct = () => {
		score += 1;
		if (score >= winningScore) {
			clearInterval(timer);
		}
	};

	export const wrong = () => {
		score -= 3;
		if (score < 0) {
			score = 0;
		}
	};
</script>

<div class="score-container">
	{#if !initialState}
		<div class="score">
			{#if !hasWon()}
				<p>SCORE <b>{score}/{winningScore}</b></p>
			{/if}
		</div>

		<div class="time">
			<p>TIME <b>{secondsToTime(time)}</b></p>
		</div>
	{/if}
</div>


<style>
	.score-container {
		font-size: 1rem;
		height: 22px;
		/* background-color: blanchedalmond; */
		width: 100%;
		position: relative;
		top: 3px;
	}

	.score {
		position: absolute;
		top: 0;
		left: 0;
	}

	.time {
		position: absolute;
		top: 0;
		right: 0;
	}


</style>
