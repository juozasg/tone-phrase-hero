<script lang="ts">
	import MoodButton from './MoodButton.svelte';
	import PianoOctave from './PianoOctave.svelte';
	import RandomizeDice from './RandomizeDice.svelte';
	import { playChord } from './audio.svelte';
	import { blackSemitones, type Mood, type Semitone } from './names';
	import { settings } from './settingsCookie.svelte';

	type Props = {
		onQuestionReset: () => void;
		gameInitState: boolean;
	};
	const { onQuestionReset, gameInitState }: Props = $props();

	let randomizeDice: RandomizeDice;

	// const allChoices = ['C#', 'D#', 'F#', 'G#', 'A#'];
	const allChoices = blackSemitones;
	// const allChoices = [10];
	let unseenChoices = $state<Semitone[]>([...allChoices]);

	let semitone = $state<Semitone>();
	let mood: Mood = $state('happy');

	export const getSemitone = () => {
		return semitone;
	};
	export const getMood = () => {
		return mood;
	};

	export function matches(st: Semitone, mood: Mood) {
		return st === semitone && mood === mood;
	}

	// this will play the dice animation
	export const clickRandomizeDice = () => {
		if (randomizeDice) {
			randomizeDice.handleClick();
		}
	};

	const generateQuestion = () => {
		if (unseenChoices.length === 0) {
			unseenChoices = [...allChoices];
		}
		const randomIndex = Math.floor(Math.random() * unseenChoices.length);
		semitone = unseenChoices[randomIndex];
		unseenChoices = unseenChoices.filter((_, index) => index !== randomIndex);

		// favor chaning the mood
		const moodOdds = mood === 'happy' ? 0.3 : 0.7;
		mood = Math.random() < moodOdds ? 'happy' : 'sad';

		// console.log('generated question', semitone, mood);

		onQuestionReset();
		if (settings.playChord) {
			playChord(semitone, mood);
		}
	};

	const selectedKeys = $derived.by(() => {
		if (semitone) {
			return [semitone];
		}
		return [];
	});
</script>

<div class="question">
	<div class="piano-container">
		<PianoOctave selectedSemitones={selectedKeys} width={220} />
	</div>

	<div class="buttons-container">
		<div>
			<RandomizeDice bind:this={randomizeDice} size={100} callback={generateQuestion} />
		</div>
		<div>
			<MoodButton
				{mood}
				hidden={gameInitState || settings.hideEmoji}
				onClick={() => playChord(semitone!, mood)}
			/>
		</div>
	</div>
</div>

<style>
	.question {
		margin: 20px;
	}

	.piano-container {
		display: flex;
		justify-content: center;
		align-items: center;
	}

	.buttons-container {
		display: flex;
		justify-content: center;
		align-items: center;
		margin-top: 20px;
		gap: 10px;
		/* border: 1px solid red; */
	}

</style>
