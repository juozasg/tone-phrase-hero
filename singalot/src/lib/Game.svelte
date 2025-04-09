<script lang="ts">
	import HelpHint from './HelpHint.svelte';

	import { page } from '$app/state';

	import ScoreFlash from '../ScoreFlash.svelte';
	import Answers from './Answers.svelte';

	import Mood from './Mood.svelte';
	import PianoOctave from './PianoOctave.svelte';
	import Randomize from './Randomize.svelte';
	import Score from './Score.svelte';
	import { onMount } from 'svelte';
	import HighScore from './HighScore.svelte';
	import { addScore } from './scoreCookie.svelte';

	const randomChoices = ['C#', 'D#', 'F#', 'G#'];
	let unseenChoices = $state<string[]>(randomChoices);

	let randomSelectedKey = $state<string>();
	let randomMood: 'happy' | 'sad' = $state('happy');

	let userIntro = $state(true);

	// svelte-ignore non_reactive_update
	let score: Score;
	let scoreFlash: ScoreFlash;
	let randomizeDice: Randomize;


	const randomize = () => {
		if (score.hasWon() || userIntro) {
			score.reset();
			scoreFlash.clear();
			userIntro = false;
			unseenChoices = randomChoices;
		}

		if (unseenChoices.length === 0) {
			unseenChoices = randomChoices;
		}
		const randomIndex = Math.floor(Math.random() * unseenChoices.length);
		randomSelectedKey = unseenChoices[randomIndex];
		unseenChoices = unseenChoices.filter((_, index) => index !== randomIndex);

		// favor chaning the mood
		const moodOdds = randomMood === 'happy' ? 0.3 : 0.7;
		randomMood = Math.random() < moodOdds ? 'happy' : 'sad';
	};

	const selectedKeys = $derived.by(() => {
		if (randomSelectedKey) {
			return [randomSelectedKey];
		}
		return [];
	});

	$effect(() => {
		if (randomMood == 'sad' && randomSelectedKey == 'F#') {
			randomMood = 'happy';
		} else if (randomMood == 'happy' && randomSelectedKey == 'D#') {
			randomMood = 'sad';
		}
	});

	function checkGuess(key: string, mood: 'happy' | 'sad') {
		if (key === randomSelectedKey && mood === randomMood) {
			// alert('Correct!');
			score.correct();
			scoreFlash.addMessage('correct');


			if (score.hasWon()) {
				randomSelectedKey = undefined;
				addScore(score.getTime());
			} else {
				randomizeDice.handleClick()
			}
		} else {
			// alert('Try again!');
			score.wrong();
			scoreFlash.addMessage('wrong');
			randomizeDice.handleClick()
		}
	}
</script>

<svelte:body
	onkeydown={(e) => {
		if (e.key === 'r' || e.key === 'R') {
			randomizeDice.handleClick()
		}
	}}
/>

<div class="question">
	<div class="container">
		<div class="columns">
			<div class="column randomize-column col-sm-12 col-4">
				<Randomize bind:this={randomizeDice} size={100} callback={randomize} />
			</div>

			<div class="piano-column column col-sm-12 col-4">
				<PianoOctave {selectedKeys} width={220} />
			</div>

			<div class="column col-sm-12 col-4">
				<Mood mood={randomMood} />
			</div>
		</div>
	</div>
</div>

{#if randomSelectedKey}
	<Answers answerOnClick={checkGuess} />
{/if}

{#if userIntro}
	<HelpHint />
{/if}

<div class="score" style="opacity: {userIntro ? 0 : 1}">
	<Score bind:this={score} />
</div>

<ScoreFlash bind:this={scoreFlash} />

<HighScore />
<style>
	.question {
		margin: 20px;
	}

	.column {
		/* border: 1px solid red; */
		display: flex;
		justify-content: center;
		align-items: center;
		margin-bottom: 20px;
	}

	.piano-column {
		padding-top: 10px;
	}

	.randomize-column {
		position: relative;
	}
</style>
