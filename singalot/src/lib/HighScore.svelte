<script lang="ts">
	import { page } from '$app/state';
	import { loadScoreCookie, sortedScores } from './scoreCookie.svelte';
	import { secondsToTime } from './util';


	loadScoreCookie();

	// const scores = 	Array.from({ length: 32 }, () => Math.floor(Math.random() * 191) + 10);

</script>

<div class="highscore">
	<b class="caption">
		<p class='high'>BEST</p>
		<p>TIMES</p>
	</b>

	{#each sortedScores() as score}
		<p class="score">{secondsToTime(score)}</p>
	{/each}
</div>

<style>
	.highscore {
		position: fixed;
		bottom: 0;
		left: 0;
		right: 0;
		background-color: #fff;
		padding: 10px;
		padding-top: 0px;
		/* border-radius: 5px; */
		box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
		/* height: 200px; */
		display: flex;
		gap: 12px;
		overflow-x: auto;
	}

	.highscore p {
		margin: 0;

		&.score {
			font-weight: 500;
			font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
			display: inline-block;
			line-height: 48px;
			position: relative;
			bottom: -3px;
			font-size: 22px;
		}
	}

	.highscore b {
		text-align: center;
		font-weight: 600;
		display: inline-block;
		margin-right: 10px;

		&.caption {
			font-size: 14px;

		}
		& .high {
			font-size: 18px;
			position: relative;
			top: 5px;
		}


	}

</style>
