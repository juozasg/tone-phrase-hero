<script lang="ts">
	import HelpHint from './HelpHint.svelte';

	import ScoreFlash from './ScoreFlash.svelte';
	import Answers from './Answers.svelte';

	import Score from './Score.svelte';
	import HighScore from './HighScore.svelte';
	import { addScore } from './scoreCookie.svelte';
	import Question from './Question.svelte';
	import AnswersEnharmonic from './AnswersEnharmonic.svelte';
	import Settings from './Settings.svelte';

	let gameInitState = $state(true);

	let questionState: '1' | '2' = $state('1');

	// svelte-ignore non_reactive_update
	let score: Score | undefined = $state();
	let scoreFlash: ScoreFlash | undefined = $state();
	let question: Question | undefined = $state();

	const semitone = $derived(question && question.getSemitone());
	const mood = $derived(question && question.getMood());

	function onQuestionReset() {
		if (gameInitState) {
			score!.reset();
			gameInitState = false;
		}
		questionState = '1';
	}

	function correct() {
		score!.correct();
		scoreFlash!.addMessage('correct');

		if (score!.hasWon()) {
			addScore(score!.getTime());
			gameInitState = true;
		} else {
			question!.clickRandomizeDice();
		}
	}

	function wrong() {
		score!.wrong();
		scoreFlash!.addMessage('wrong');
		question!.clickRandomizeDice();
	}

	function onAnswered(correctAnswer: boolean) {
		if (correctAnswer) {
			if (questionState == '1') {
				questionState = '2';
			} else {
				questionState = '1';
				correct();
			}
		} else {
			questionState = '1';
			wrong();
		}
	}
</script>

<div class="container game-container">
	<div class="score">
		<Score bind:this={score} />
	</div>
	<Question {onQuestionReset} {gameInitState} bind:this={question} />

	{#if !gameInitState && semitone && mood}
		{#if questionState == '1'}
			<Answers {onAnswered} {semitone} {mood} />
		{:else if questionState == '2'}
			<AnswersEnharmonic {onAnswered} {semitone} {mood} />
		{/if}
	{/if}

	{#if gameInitState}
		<HelpHint />
	{/if}

	{#if score && score.hasWon()}
		<div class="win">Win!</div>
	{/if}

	<ScoreFlash bind:this={scoreFlash} />

	<Settings />
	<HighScore />
</div>

<style>
	.game-container {
		position: relative;
		max-width: 720px;
		/* border: 1px solid cadetblue; */
	}

	.win {
		color: green;
		font-weight: bold;
		font-size: 400%;
		display: flex;
		justify-content: center;
		align-items: center;
		margin-top: 15px;
		margin-bottom: 30px;
		font-family: Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;

	}
</style>
