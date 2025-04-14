<script lang="ts">
	import HelpHint from './HelpHint.svelte';

	import ScoreFlash from '../ScoreFlash.svelte';
	import Answers from './Answers.svelte';

	import Score from './Score.svelte';
	import HighScore from './HighScore.svelte';
	import { addScore } from './scoreCookie.svelte';
	import Question from './Question.svelte';
	import AnswersEnharmonic from './AnswersEnharmonic.svelte';

	let gameInitState = $state(true);

	let questionState: '1' | '2' = $state('1');

	// svelte-ignore non_reactive_update
	let score: Score;
	let scoreFlash: ScoreFlash;
	let question: Question;

	function onQuestionReset() {
		if (gameInitState) {
			gameInitState = false;
		}
	}

	// function checkGuess(key: string, mood: 'happy' | 'sad') {
	// 	if (key === randomSelectedKey && mood === randomMood) {
	// 		// alert('Correct!');
	// 		score.correct();
	// 		scoreFlash.addMessage('correct');

	// 		if (score.hasWon()) {
	// 			randomSelectedKey = undefined;
	// 			addScore(score.getTime());
	// 		} else {
	// 			randomizeDice.handleClick()
	// 		}
	// 	} else {
	// 		// alert('Try again!');
	// 		score.wrong();
	// 		scoreFlash.addMessage('wrong');
	// 		randomizeDice.handleClick()
	// 	}
	// }
</script>

<Question {onQuestionReset} bind:this={question} />

{#if !gameInitState}
	{#if questionState == '1'}
		<Answers answerOnClick={checkGuess} />
	{:else if questionState == '2'}
		<AnswersEnharmonic
			key={question.pianoKey}
			answerOnClick={checkGuess}
	{/if}
{/if}

{#if gameInitState}
	<HelpHint />
{/if}

<div class="score" style="opacity: {gameInitState ? 0 : 1}">
	<Score bind:this={score} />
</div>

<ScoreFlash bind:this={scoreFlash} />

<HighScore />
