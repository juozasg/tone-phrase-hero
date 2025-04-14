<script lang="ts">
	import HelpHint from './HelpHint.svelte';

	import ScoreFlash from '../ScoreFlash.svelte';
	import Answers from './Answers.svelte';

	import Score from './Score.svelte';
	import HighScore from './HighScore.svelte';
	import { addScore } from './scoreCookie.svelte';
	import Question from './Question.svelte';
	import AnswersEnharmonic from './AnswersEnharmonic.svelte';
	import { playChord } from './audio.svelte';

	let gameInitState = $state(true);

	let questionState: '1' | '2' = $state('1');

	// svelte-ignore non_reactive_update
	let score: Score;
	let scoreFlash: ScoreFlash;
	let question: Question | undefined;

	const semitone = $derived(question && question.getSemitone());
	const mood = $derived(question && question.getMood());

	function onQuestionReset() {
		if (gameInitState) {
			score!.reset();
			gameInitState = false;
		}
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

<div class="score">
	<Score bind:this={score} />
</div>

<ScoreFlash bind:this={scoreFlash} />

<HighScore />
