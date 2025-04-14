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

{#if !initialState}
	<div class="container score-container">
		<div class="columns">
			<div class="score column col-sm-12 col-3">
				{#if !hasWon()}
					<p>SCORE <b>{score}/{winningScore}</b></p>
				{/if}
			</div>

			<div class="column hide-sm col-6"></div>

			<div class="time column col-sm-12 col-3">
				<p>TIME <b>{secondsToTime(time)}</b></p>
			</div>
		</div>
	</div>
{/if}

{#if hasWon()}
	<div class="win">Win!</div>

	<!-- <HelpHint/> -->
{/if}

<style>
	.score-container {
		margin-top: 20px;
		font-size: 1rem;
	}

	.win {
		color: green;
		font-weight: bold;
		font-size: 300%;
		display: flex;
		justify-content: center;
		align-items: center;
		margin-bottom: 30px;
	}

	.time {
		@media screen and (min-width: 601px) {
			/* text-align: center; */
			text-align: right;
		}
	}

	p {
		margin-bottom: 6px;
	}
</style>
