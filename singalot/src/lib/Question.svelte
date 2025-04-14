<script lang="ts">
	import MoodButton from './MoodButton.svelte';
	import PianoOctave from './PianoOctave.svelte';
	import RandomizeDice from './RandomizeDice.svelte';
	import { playChord } from './audio.svelte';
	import { blackSemitones, type Mood, type Semitone } from './names';

	type Props = {
		onQuestionReset: () => void;
		gameInitState: boolean
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
		playChord(semitone, mood);
	};

	const selectedKeys = $derived.by(() => {
		if (semitone) {
			return [semitone];
		}
		return [];
	});

</script>


<div class="question">
	<div class="container">
		<div class="columns">
			<div class="column randomize-column col-sm-12 col-4">
				<RandomizeDice bind:this={randomizeDice} size={100} callback={generateQuestion} />
			</div>

			<div class="piano-column column col-sm-12 col-4">
				<PianoOctave selectedSemitones={selectedKeys} width={220} />
			</div>

			<div class="column col-sm-12 col-4">
				<MoodButton mood={mood} hidden={gameInitState} onClick={() => playChord(semitone!, mood)	}/>
			</div>
		</div>
	</div>
</div>

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
